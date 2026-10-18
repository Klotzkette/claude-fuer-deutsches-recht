# 1. UN-Kaufrecht: CISG

Internationale Warenverträge prüfen, gestalten und durchsetzen: Dieses Plugin begleitet Käufer und Verkäufer von widersprüchlichen Vertragsunterlagen über Lieferung und Mängelanzeige bis zum fertigen Schreiben, Vertragsnachtrag oder Schriftsatzentwurf. Zehn Fachskills bearbeiten die einzelnen Streitfragen; ein zusätzlicher Hauptskill führt den Auftrag zusammen. Kaufrecht und Transportrecht werden getrennt geprüft, auch wenn dieselbe beschädigte Ware betroffen ist.

[Hauptübersicht](../README.md) · [Plugin-Dateien](.) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/un-kaufrecht-cisg.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [English guide](#16-english-guide)

## 1.1. Mit dem konkreten Vertrag beginnen

Geben Sie Ihre Rolle, das gewünschte Arbeitsprodukt und die vorhandenen Unterlagen an. Angebot, Bestellung, AGB, unterschriebener Vertrag, Lieferschein und Korrespondenz werden zunächst auftragsbezogen gelesen. Nur entscheidende Lücken werden erfragt. Nach Ihrer Antwort wird am selben Entwurf weitergearbeitet, nicht ein neues Vollinterview begonnen.

Der Einstiegsskill heißt `cisg-kaufmandat-steuern`. Er wählt den benötigten Fachschritt und führt dessen Ergebnis in den laufenden Auftrag zurück; die übrigen Skills lassen sich auch einzeln verwenden.

Ein möglicher Auftrag: „Wir vertreten den deutschen Verkäufer. Im Angebot steht CISG-Ausschluss, in der späteren beiderseits unterschriebenen Vereinbarung dagegen CISG-Anwendung. Prüfen Sie die tatsächlich vereinbarte Regelung und entwerfen Sie die Antwort auf die Mängelanzeige des französischen Käufers.“

| Ausgangslage | Bearbeitung | Arbeitsprodukt |
| --- | --- | --- |
| Unklar, ob das UN-Kaufrecht gilt | Niederlassungen, Warenvertrag, Vertragsstaaten, Vorbehalte und ausdrückliche Abwahl prüfen | Begründete Rechtswahlprüfung und passende Vertragsregelung |
| Bestellung, AGB und Nachtrag widersprechen sich | Zugang, Einbeziehung, Vertretung und zeitliche Rangfolge klären | Ausformulierter Nachtrag oder Antwort zum Vertragsinhalt |
| Ware fehlt, ist verspätet oder beschädigt | Leistungsinhalt, Lieferklausel, Belege und Gefahrübergang zuordnen | Lieferaufforderung, Mängelanzeige oder getrennte Transportreklamation |
| Nachbesserung oder Ersatzlieferung steht an | Nutzung, Prüfbedingungen, Termine und Zumutbarkeit klären | Konkrete Nacherfüllungsvereinbarung mit Nachweisen und Fortsetzung |
| Rückzahlung, Minderung oder Deckungskauf gewünscht | Voraussetzungen, Erklärungen, Fristen und Berechnung unterscheiden | Anspruchsschreiben, Abwehrschreiben oder begründeter Vertragsbeendigungsentwurf |
| Prozess oder Schiedsverfahren angekündigt | Kaufstatut, Gerichtsstand, Schiedsbindung und Verjährung getrennt prüfen | Verfahrensbezogener Entwurf mit noch zu beschaffenden Belegen |

Eine deutsche Rechtswahl ist nicht schon eine CISG-Abwahl. Umgekehrt setzt das Plugin das UN-Kaufrecht nicht gegen einen wirksam vereinbarten Ausschluss durch. Incoterms ersetzen weder den vollständigen Kaufvertrag noch die Prüfung des Frachtvertrags. Die Angemessenheit einer Rüge- oder Aufhebungsfrist wird nicht aus einer pauschalen Tageszahl abgeleitet.

## 1.2. Plugin oder eigenständigen Prompt wählen

| Fassung / Format | Verwendung / Use | Download |
| --- | --- | --- |
| Plugin-ZIP | Zehn Fachskills, ein Hauptskill und Quellen / Ten specialist skills, one coordinating skill and references | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/un-kaufrecht-cisg.zip) |
| Portables Plugin-ZIP | Derselbe Inhalt in einem umschließenden Plugin-Ordner / Same content in a containing folder | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/un-kaufrecht-cisg-portable.zip) |
| Werkstatt-Prompt | Ausführlicher eigenständiger Arbeitsablauf vom Vertrag bis zur Dokumentproduktion / Detailed standalone workflow | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/un-kaufrecht-cisg-werkstatt.md" download>Werkstatt als Markdown / Download workshop</a> |
| Mini-Prompt / Schnellstart | Kompakter CISG-Arbeitsablauf / Compact standalone workflow | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/un-kaufrecht-cisg-schnellstart.md" download>Mini als Markdown / Download quick start</a> |
| Hauptproblem-Prompt | Einen internationalen Lieferstreit bis zum bestellten Dokument führen / Coordinate a sales dispute through to the requested document | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/un-kaufrecht-cisg-hauptproblem.md" download>Hauptproblem als Markdown / Download coordinating prompt</a> |

Die Downloadhilfe liefert Markdown-Dateien statt einer bloßen Browseransicht. Die aktuelle Arbeitsfassung und das [fest versionierte Komponentenrelease 1.0.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/un-kaufrecht-cisg-v1.0.0) sind getrennt erkennbar. Werkstatt, Mini und Hauptproblem-Prompt werden nicht mit dem Plugin installiert. Mini und Hauptproblem bleiben jeweils unter 7.500 Zeichen und UTF-8-Bytes, einschließlich Leerzeichen und Windows-Zeilenumbrüchen.

Für einen eigenständigen Einsatz eine Markdown-Datei als Arbeitsanweisung übergeben und den Auftrag samt Unterlagen hinzufügen. Nicht alle Fassungen gleichzeitig laden. Das Plugin verwendet nur den jeweils benötigten Fachskill; der Hauptskill hält Ergebnis, offene Punkte und nächsten Dokumentenschritt zusammen. Recherchezugang, Dateiwerkzeuge und Export hängen von der verwendeten Oberfläche ab. Das Paket enthält keine eingebauten Datenbankzugänge und versendet keine Erklärungen selbständig.

## 1.3. Elf Skills einzeln herunterladen

Die folgende Übersicht ist alphabetisch. Die Arbeit folgt dem Vertrag und dem gewünschten Ergebnis, nicht der Tabellenreihenfolge. Jeder Link liefert die vollständige Markdown-Datei des jeweiligen Skills.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

### 1.3.1. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`cisg-anwendung-rechtswahl-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-anwendung-rechtswahl-pruefen/SKILL.md) | Klärt Anwendbarkeit, Abwahl und ergänzendes Recht beim internationalen Warenkauf und erstellt eine begründete Mandatsauskunft oder eindeutige Rechtswahlklausel. Prüft Artikel 1 bis 13 CISG und Vertragsstaatenvorbehalte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-anwendung-rechtswahl-pruefen/SKILL.md) |
| [`cisg-gefahr-transport-abgrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-gefahr-transport-abgrenzen/SKILL.md) | Trennt kaufrechtliche Gefahr nach Artikeln 66 bis 70 CISG, Incoterms-Kosten und Eigentum vom eigenständigen Transportanspruch nach CMR. Erstellt getrennte Verkäufer- und Frachtführeranschreiben mit passenden Vorbehalten und Fristen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-gefahr-transport-abgrenzen/SKILL.md) |
| [`cisg-kaufmandat-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-kaufmandat-steuern/SKILL.md) | Führt internationale Warenkaufmandate für Käufer oder Verkäufer vom Lesen der Unterlagen über gezielte Rückfragen zum fertigen Brief, Vertragsnachtrag oder Gutachten. Hauptskill für zehn Fachskills zum UN-Kaufrecht CISG. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-kaufmandat-steuern/SKILL.md) |
| [`cisg-kaufpreis-abnahme-durchsetzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-kaufpreis-abnahme-durchsetzen/SKILL.md) | Erstellt Zahlungs- und Abnahmeaufforderungen oder Käufererwiderungen nach Artikeln 53 bis 65 CISG. Prüft Fälligkeit, Dokumente, Untersuchung, Nachfrist, Spezifikation und Verkäuferaufhebung statt einer pauschalen Mahnung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-kaufpreis-abnahme-durchsetzen/SKILL.md) |
| [`cisg-leistungsgefahr-ratenlieferung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-leistungsgefahr-ratenlieferung-steuern/SKILL.md) | Prüft drohende Nichterfüllung, Leistungsaussetzung und Ratenlieferungen nach Artikeln 71 bis 73 CISG. Verfasst konkrete Sicherungsaufforderungen und begrenzte Aufhebungserklärungen ohne vorschnellen Vertragsabbruch. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-leistungsgefahr-ratenlieferung-steuern/SKILL.md) |
| [`cisg-lieferung-vertragsmaessigkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-lieferung-vertragsmaessigkeit-pruefen/SKILL.md) | Prüft Lieferung, Dokumente, Qualität, Verpackung und Rechte Dritter nach Artikeln 30 bis 37 und 41 bis 42 CISG. Verknüpft Sollbeschaffenheit, Gefahrzeitpunkt und technische Belege und erstellt eine konkrete Leistungsaufforderung oder Ein... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-lieferung-vertragsmaessigkeit-pruefen/SKILL.md) |
| [`cisg-nacherfuellung-aufhebung-waehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-nacherfuellung-aufhebung-waehlen/SKILL.md) | Wählt für Käufer und Verkäufer zwischen Nachbesserung, Ersatzlieferung, Minderung und Vertragsaufhebung. Prüft Artikel 25 bis 28 und 45 bis 52 CISG, konkrete Heilungsangebote und eigenständige Aufhebungsfristen vor einem Deckungskauf. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-nacherfuellung-aufhebung-waehlen/SKILL.md) |
| [`cisg-rueckabwicklung-fristen-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-rueckabwicklung-fristen-sichern/SKILL.md) | Gestaltet Rückgabe, Kaufpreiserstattung, Erhaltung und Verwertung nach Artikeln 81 bis 88 CISG und prüft externe Verjährung. Trennt Mängelanzeige, Aufhebungsfrist, CMR-Frist und Verjährung in einem konkreten Abwicklungsdokument. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-rueckabwicklung-fristen-sichern/SKILL.md) |
| [`cisg-schadensersatz-zinsen-berechnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-schadensersatz-zinsen-berechnen/SKILL.md) | Beziffert Schaden, Deckungskauf, Marktpreisdifferenz und Zinsen nach Artikeln 74 bis 80 CISG. Prüft Vorhersehbarkeit, Schadensminderung, Befreiung und Mitverursachung und erstellt eine belegte Forderung oder Abwehrrechnung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-schadensersatz-zinsen-berechnen/SKILL.md) |
| [`cisg-untersuchung-maengelruege-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-untersuchung-maengelruege-sichern/SKILL.md) | Sichert Untersuchung, konkrete Mängelanzeige und Übermittlungsbelege nach Artikeln 38 bis 44 CISG. Prüft erkennbare und verdeckte Fehler, Verkäuferkenntnis und Entschuldigung und erstellt eine fertige Rüge oder begründete Rügeeinwendung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-untersuchung-maengelruege-sichern/SKILL.md) |
| [`cisg-vertrag-agb-klauselkollision-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-vertrag-agb-klauselkollision-klaeren/SKILL.md) | Prüft Angebot, Annahme, AGB-Einbeziehung, widersprüchliche CISG-Abwahl und spätere Bestätigung. Entwickelt nach Artikel 8 sowie Artikeln 14 bis 24 und 29 CISG den belegbaren Vertragsinhalt sowie fertige Klarstellungs- und Nachtragsklauseln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/skills/cisg-vertrag-agb-klauselkollision-klaeren/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

## 1.4. Drei internationale Handelsakten / Three sales cases

Jeder Fall enthält Geschäftsunterlagen, keine Musterlösung. Gesamt-PDF, flaches Einzel-PDF-ZIP und flaches Originalformat-ZIP bilden denselben Bestand ab. Word-Dokumente, E-Mails mit tatsächlichen Anlagen, Zahlenlisten und Gesprächsnotizen bleiben einzeln auswertbar. Beide ZIPs enthalten eine `README.txt` mit dem Warnhinweis; die PDFs enthalten keine zusätzliche Warnseite.

### 1.4.1. Pumpenlieferung Bremen–Lyon: widersprüchliche Vertragsbedingungen

Ein deutscher Pumpenlieferant und ein französischer Käufer tauschen unterschiedliche Einkaufs- und Verkaufsbedingungen aus. Spätere Vertragsunterlagen, Unterzeichnungen und E-Mails zeigen, welche Fassungen tatsächlich verhandelt wurden. Liefer- und Reklamationsbelege erlauben die Weiterarbeit über die Rechtswahlfrage hinaus. [Aktenordner und Unterlagen](../testakten/cisg-klauselkollision-pumpen-bremen-lyon/).

German–French pump sale: conflicting standard terms, later agreements and delivery correspondence. Determine the contractual sequence from the documents rather than assuming either party's account is correct.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/cisg-klauselkollision-pumpen-bremen-lyon/gesamt-pdf/cisg-klauselkollision-pumpen-bremen-lyon_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-klauselkollision-pumpen-bremen-lyon-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-klauselkollision-pumpen-bremen-lyon.zip) |

### 1.4.2. Sensoren Turin–Ulm: Kaufvertrag und Transport

Empfindliche Sensoren werden auf der Straße von Italien nach Deutschland transportiert. Kaufvertrag, Transportauftrag, Übergabeunterlagen, Prüfungen und Korrespondenz mit dem Versicherer betreffen unterschiedliche Beteiligte und Zeitpunkte. Die Beschädigung lässt sich nicht allein aus dem Ablieferungsbeleg zuordnen. [Aktenordner und Unterlagen](../testakten/cisg-transportschaden-sensoren-ulm-turin/).

Italian–German sensor shipment: distinguish the sales contract, carrier's custody, packaging evidence and insurance correspondence. The same loss does not imply identical claims or notice requirements against every party.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/cisg-transportschaden-sensoren-ulm-turin/gesamt-pdf/cisg-transportschaden-sensoren-ulm-turin_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-transportschaden-sensoren-ulm-turin-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-transportschaden-sensoren-ulm-turin.zip) |

### 1.4.3. Maschinenlieferung Brno–Leipzig: Leistung, Nachbesserung und Ersatzbeschaffung

Eine Produktionsmaschine erreicht beim Käufer nicht die erwartete Leistung. Spezifikation, Inbetriebnahme, Betriebsdaten, Serviceangebote und Ersatzbeschaffungskorrespondenz dokumentieren verschiedene Erklärungen und Handlungsoptionen. Ob und wie der Vertrag fortgesetzt oder beendet wird, bleibt der Bearbeitung überlassen. [Aktenordner und Unterlagen](../testakten/cisg-maschinenlieferung-nachbesserung-leipzig-brno/).

Czech–German machinery sale: compare the agreed specification, operating conditions, attempted cure and substitute-purchase evidence before drafting the next step.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Download |
| --- | --- |
| Gesamt-PDF / Combined PDF | [Gesamte Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/refs/heads/main/testakten/cisg-maschinenlieferung-nachbesserung-leipzig-brno/gesamt-pdf/cisg-maschinenlieferung-nachbesserung-leipzig-brno_gesamt.pdf) |
| Einzel-PDFs / Individual PDFs | [Einzel-PDF-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-maschinenlieferung-nachbesserung-leipzig-brno-einzelpdfs.zip) |
| Originalunterlagen / Native documents | [Originalformat-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/un-kaufrecht-cisg-v1.0.0/testakte-cisg-maschinenlieferung-nachbesserung-leipzig-brno.zip) |

## 1.5. Quellen, Prüfstand und Grenzen

Redaktioneller Stand: 18.10.2026. Das <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=un-kaufrecht-cisg/references/rechtsprechung.md" download>Quellenverzeichnis als Markdown</a> unterscheidet geprüfte Normtexte und Entscheidungsgründe von Pressemitteilung, kurzer Zulassungsmitteilung und noch zu recherchierendem Folgeverfahren. Entscheidungen aus 2001 und 2002 bleiben ältere Leitentscheidungen; neuere Entscheidungen aus 2025 und 2026 werden mit ihrer konkreten Aussagegrenze eingeordnet. Insbesondere ist eine im Einzelfall verspätete Vertragsaufhebung keine allgemeine Sechswochenfrist. Ein nur zugelassenes Revisionsverfahren belegt noch keinen abschließenden materiellen Rechtssatz.

Das individuelle Qualitätsprofil deckt alle elf Skills ab. Es enthält redaktionelle Prüffälle, keine behaupteten Modellläufe und keine Erfolgsquote. Paket-, Dateiformat- und Inhaltsabgleich ersetzen keinen Live-Test in einer bestimmten Oberfläche. Fehlender Quellenzugang wird kenntlich gemacht; eine ungeprüfte Antwort darf nicht als verifizierte Rechtslage ausgegeben werden.

Dieses experimentelle Arbeitsmittel ist keine Rechtsberatung, keine rechtliche Zertifizierung und keine Garantie eines bestimmten Ergebnisses. Vor Verwendung eines Entwurfs sind Tatsachen, geltendes Recht, Vertretung, Fristen und notwendige Freigaben zu prüfen. Die Werkzeuge können Dokumente vorbereiten, aber keine wirksame Erklärung, Zustellung oder gerichtliche Einreichung allein durch deren Erstellung bewirken.

## 1.6. English Guide

This standalone CISG plugin supports cross-border sales work for buyers and sellers. Ten specialist skills and one coordinating skill cover applicability, exclusion, contract terms, delivery, examination and notice, cure, avoidance, damages and the transport interface. The coordinating skill continues the same draft after targeted questions; it does not restart intake or substitute a document inventory for the requested work.

Choose the plugin or one of the three standalone Markdown prompts in section 1.2. Provide the relevant contracts, your role and the document you need. A choice of German law is not itself a CISG exclusion. Conversely, an effective exclusion must not be ignored. Sales remedies, cargo claims, insurance, jurisdiction and limitation need separate legal analysis. Drafting is not sending or filing.

Section 1.3 offers each of the eleven skills as an individual download. Section 1.4 provides three files of business documents in combined-PDF, flat individual-PDF ZIP and flat native-document ZIP formats. The native files include Word, email, CSV and text rather than Markdown-only summaries. Both ZIP variants carry the bilingual warning in a root-level `README.txt`; PDF notices appear immediately above the download tables.

The workshop is the detailed standalone alternative. The quick-start and coordinating prompts each remain below 7,500 characters and UTF-8 bytes, including spaces and Windows line endings. Standalone prompts and case materials are not installed with the plugin. Host support and available research, file and export tools must be checked in the actual environment. The source register states which decisions were read, what they support and what they do not decide. This is an experimental working aid, not legal advice or a universal compatibility guarantee.
