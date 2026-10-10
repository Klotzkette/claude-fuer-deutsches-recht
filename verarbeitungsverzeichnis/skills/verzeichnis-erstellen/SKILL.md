---
name: verzeichnis-erstellen
description: Erstellt aus geprüften Angaben ein versioniertes Verzeichnis mit getrennten Verantwortlichen- und Auftragsverarbeiteransichten. Ordnet Mindestangaben, Zusatzprüfungen, Quellen und offene Aufgaben eindeutigen Tätigkeiten zu.
---

# Ein prüfbares Verarbeitungsverzeichnis erstellen

## 1. Zweck und Anwendungsfall

Führen Sie die erhobenen Tätigkeiten zu einem nutzbaren Verzeichnis zusammen. Das Ergebnis soll den tatsächlichen Stand wiedergeben und später gezielt änderbar bleiben. Eine schön formatierte Tabelle ist nur dann brauchbar, wenn sie richtige Rollen, nachvollziehbare Zwecke und erkennbare Lücken enthält. Erstellen Sie zunächst die belegbaren Einträge und lassen Sie einzelne offene Punkte die übrige Arbeit nicht blockieren.

Der Skill erstellt sowohl den führenden Registerbestand als auch verständliche Datenblätter. Verantwortlichen- und Auftragsverarbeiterpflichten werden getrennt dargestellt. Zusatzfelder wie Rechtsgrundlage, interne Priorität und DSFA-Vorprüfung unterstützen die Arbeit, dürfen aber nicht sämtlich als ausdrücklich vorgeschriebene Mindestfelder des Artikels 30 bezeichnet werden.

## 2. Eingaben

Lesen Sie `erhebung`, vorhandene Registerdateien, `rechts-und-loeschpruefung` und `dienstleisterpruefung`. Ermitteln Sie die führende Dateifassung samt Registerkennung und Revision. Bei erstmaliger Erstellung werden Unternehmen, Kontakt, gegebenenfalls Vertreter und Datenschutzbeauftragter erfasst. Erfinden Sie keine Kontaktperson, wenn diese noch nicht benannt ist.

Für jede Tätigkeit benötigen Sie stabile Kennung, Titel, Rolle, fachlich zuständige Person, Quellen und Bearbeitungsstand. Geplante Prozesse erhalten einen klaren Hinweis und werden nicht durch einen technischen Aktivitätsstatus als materiell freigegeben dargestellt. Lesen Sie das [Datenmodell](../../references/datenmodell.md), bevor Sie Felder importieren oder ein eigenes Dateischema behaupten.

## 3. Ablauf und Checkliste

### 3.1. Eine führende Fassung festlegen

Verwenden Sie die kanonische JSON-Datei des Helfers [vvt.py](../../scripts/vvt.py). Excel ist die bearbeitbare Austauschansicht; Word dient der verständlichen Ausgabe und XML dem strukturierten Export. Behaupten Sie keinen automatischen Rückimport von Word oder XML, wenn der Helfer ihn nicht anbietet. Prüfen Sie die verfügbaren Unterbefehle über die tatsächlich ausgeführte Hilfe.

Legen Sie einen klaren Arbeitsordner mit Register, Quellen und Ausgaben an, soweit der Auftrag dies umfasst. Bewahren Sie Vorgängerfassungen oder vorhandene Sicherungen. Die Schreibrechte sollten auf berechtigte Bearbeiter beschränkt sein; ein gemeinsam verwendetes Dateisystem ist keine echte Mehrbenutzerdatenbank. Bei gleichzeitigem Bearbeiten sind Änderungen anhand der Revision abzugleichen.

### 3.2. Mindestangaben des Verantwortlichen befüllen

Artikel 30 Absatz 1 DSGVO verlangt den Verantwortlichenkontakt sowie gegebenenfalls Angaben zu gemeinsam Verantwortlichen, Vertreter und Datenschutzbeauftragtem. Ordnen Sie der Tätigkeit die konkreten Zwecke, Kategorien betroffener Personen und personenbezogener Daten sowie Empfängerkategorien zu. Empfänger im Drittland beziehungsweise internationale Organisationen dürfen nicht in einer pauschalen Kategorie verschwinden.

Erfassen Sie gegebenenfalls Drittlandsübermittlungen mit dem betroffenen Land oder der internationalen Organisation. Die besondere Garantiedokumentation bei Artikel 49 Absatz 1 Unterabsatz 2 ist im Wortlaut ausdrücklich genannt. Eine darüber hinausgehende Transferprüfung wird sinnvollerweise verknüpft, aber als ergänzender Nachweis erklärt. Löschfristen und allgemeine technische sowie organisatorische Maßnahmen sind nach dem Gesetz „wenn möglich“ aufzunehmen; behandeln Sie dies nicht als beliebige Auslassungsoption. Dokumentieren Sie, warum eine Angabe noch fehlt und wie sie beschafft wird.

### 3.3. Auftragsverarbeitung eigenständig abbilden

Artikel 30 Absatz 2 DSGVO betrifft Kategorien von im Auftrag durchgeführten Verarbeitungen. Erfassen Sie Namen und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, für den er tätig ist, gegebenenfalls Vertreter und Datenschutzbeauftragten. Die Verarbeitungskategorien müssen dem jeweiligen Auftraggeber zugeordnet bleiben. Eine Liste „alle Kunden“ ohne bestimmbare Kontakte erfüllt diesen Zweck nicht.

Auch hier sind gegebenenfalls Drittlandsübermittlungen und, wenn möglich, eine allgemeine TOM-Beschreibung zu erfassen. Verlangen Sie zusätzliche Angaben zur Unterstützung des Auftraggebers nur dort, wo sie sachlich nötig sind. Verwechseln Sie dessen Zwecke und Rechtsgrundlagen nicht mit eigenen Erlaubnistatbeständen des Auftragsverarbeiters. Eigene Werbung, Abrechnung oder Personalverwaltung bleiben getrennte Verantwortlichentätigkeiten.

### 3.4. Beschreibungen brauchbar formulieren

Schreiben Sie Zwecke als konkrete betriebliche Tätigkeit: „Das Unternehmen verwendet Kundenkontakt- und Auftragsdaten, um bestellte Reparaturen zu planen, auszuführen und abzurechnen.“ Vermeiden Sie Leerformeln wie „Geschäftszweck“ oder „gesetzliche Pflichten“. Kategorien sollen zugleich verständlich und hinreichend genau sein; einzelne Diagnosen, vollständige Kontonummern oder tatsächliche Kundennamen sind für das abstrakte Verzeichnis meist unnötig.

Beschreiben Sie TOM allgemein genug für das Verzeichnis und verlinken Sie vertiefte, zugangsbeschränkte Sicherheitsdokumente. Eine erfundene Aussage zu Verschlüsselung, Wiederherstellung oder Zugriffskontrolle ist schlechter als eine sichtbare Nachweislücke. Löschangaben nennen Datenkategorie, auslösendes Ereignis und begründeten Zeitraum beziehungsweise den noch zu klärenden Punkt. Mehrere Zwecke dürfen unterschiedliche Löschlogiken erfordern.

### 3.5. Quellen und offene Felder erhalten

Ein leeres Feld bedeutet „noch nicht erhoben“. Ein ausdrücklich unbekannter Sachverhalt ist als solcher zu beschreiben. „Nicht einschlägig“ setzt eine nachvollziehbare Begründung voraus. Die technische Vollständigkeitsprüfung erkennt formale Lücken, kann aber die Wahrheit langer Freitexte nicht bestätigen. Bezeichnen Sie technisch fehlerfreie Datensätze daher nicht allein deshalb als rechtskonform.

Geben Sie jedem wesentlichen Satz einen nachvollziehbaren Beleg oder einen klaren Vorläufigkeitsvermerk. Ein Quellenverweis sollte Dokumenttitel, Stand, konkrete Stelle und bei Bedarf Dateihash enthalten. Vertrauliche Unterlagen werden nicht automatisch mit jeder Registerausgabe verteilt. Die Geschäftsführung kann einen zusammenfassenden Bericht erhalten, während detaillierte technische Maßnahmen intern beschränkt bleiben.

### 3.6. Prüfung, Änderung und Freigabe trennen

Lassen Sie [Risiken und DSFA](../risiken-dsfa-pruefen/SKILL.md) die identifizierten Tätigkeiten anhand desselben Sachstands beurteilen. Eine dokumentierte Entscheidung wird an den Sachstand gebunden; Änderungen an relevanten Feldern führen zu erneuter Prüfung statt stiller Fortschreibung. Status „geplant“, „aktiv“, „pausiert“ oder „beendet“ beschreibt den Betrieb und ist keine Genehmigung. Die menschliche Entscheidung muss im nachvollziehbaren Prüfvermerk stehen.

Übergeben Sie `register` an [Änderungen nachhalten](../aenderungen-nachhalten/SKILL.md) und [Verzeichnis ausgeben](../verzeichnis-ausgeben/SKILL.md). Die Rückgabe enthält Importbefund, neue Revision oder fertige Ausgabedateien. Änderungen aus nachgereichten Interviews gehen wieder in die Erhebung; fachliche Lücken verschwinden nicht durch einen Export.

## 4. Quellenpflicht

Artikel 30 DSGVO ist die Grundlage der beiden unterschiedlichen Verzeichnistypen. Die geöffneten Normen und DSK-Hinweise stehen in [Rechtsquellen](../../references/rechtsquellen.md). Halten Sie [Zitierweise](../../references/zitierweise.md) ein. Das technische Datenmodell ist eine eigene Umsetzung und kein amtlich vorgeschriebenes Format. Auf Anfrage ist das Verzeichnis der zuständigen Aufsichtsbehörde bereitzustellen; eine laufende öffentliche Veröffentlichung folgt daraus nicht.

## 5. Ausgabeformat

Liefern Sie die Registerdatei, rollengetrennte Übersichten und eine verständliche Lückenliste. Beschreibungstexte, Prüfvermerke und Anschreiben sind vollständig ausformuliert; reine Schlagwortgerüste sind kein fertiges Produkt. Formatierte Berichte verwenden Times New Roman, 11 pt und dezimale Gliederung. Breite Tabellen werden in sinnvoll verbundene Ansichten aufgeteilt.

Nennen Sie Registerkennung, Revision, Stand, Speicherort und verbleibende fachliche Vorbehalte. Bestätigen Sie eine Datei nur, wenn sie tatsächlich erzeugt und geöffnet oder technisch überprüft wurde. Der erfolgte Export ist von einer externen Vorlage zu unterscheiden.

## 6. Beispiele

Eine Firma verwaltet eigene Beschäftigte und verarbeitet Supportdaten für Kunden. Sie erstellen getrennte Einträge nach Artikel 30 Absatz 1 und Absatz 2 mit gemeinsamem Organisationsstamm, aber verschiedenen fachlichen Mindestangaben. Der Kundenkontakt bleibt je Auftraggeber zugeordnet.

Ein Löschkonzept fehlt. Sie tragen keinen üblichen Fantasiezeitraum ein, sondern halten Datenkategorien und vorhandene Vertragsangaben fest, dokumentieren die offene Fristprüfung und liefern das übrige Verzeichnis bereits verwendbar aus.
