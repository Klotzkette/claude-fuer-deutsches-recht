# 1. ChatGPT, Codex und Claude Cowork einrichten

## 1.1. Erst den Betriebsmodus bestimmen

**Reale Computersteuerung ist ein gefährlicher Prototyp. Sie kann Mandatsdaten offenlegen und wirksame Nachrichten absenden. Beginnen Sie mit Testdaten und Testpostfächern. Die Herstellerwarnungen, insbesondere die Warnung von Anthropic vor Computersteuerung juristischer Dokumente, stehen in der [Computersteuerungsreferenz](computersteuerung-und-postfaecher.md).**

Das Plugin funktioniert im Textmodus, mit Dateizugriff und mit zusätzlich verfügbaren App-Werkzeugen. Diese Fähigkeiten werden zu Beginn tatsächlich geprüft. Die Stufen 0 bis 3 bestimmen weiter die interne Arbeitstiefe; eine reale Computersitzung benötigt zusätzlich einen begrenzten Sitzungsauftrag. Ein allgemeiner Schalter „voller Zugriff“ in einer App ersetzt weder die Reichweite des Mandats noch die Freigabe einer konkreten Außenhandlung.

Wählen Sie für einen neuen Computerlauf ausdrücklich Simulation oder realen Betrieb und nennen Sie die zulässigen Apps, Konten, Mandate, Tätigkeiten, Laufzeit sowie die verantwortliche Person. Die vorhandene Festlegung wird in derselben Sitzung übernommen. Ohne realen Auftrag werden keine produktiven Postfächer geöffnet. Geheimnisse werden nicht in den Chat eingegeben.

## 1.2. Claude Cowork und Claude Code

Installieren Sie das Plugin über den im Konto tatsächlich verfügbaren Pluginweg. Das Komponentenrelease enthält das Plugin-ZIP; das Repository stellt zusätzlich den Marketplace bereit. Die [Anthropic-Pluginhilfe](https://support.claude.com/en/articles/13837440-use-plugins-in-claude), am 08.10.2026 geöffnet, erläutert die verschiedenen Hostoberflächen. Prüfen Sie nach dem Import die angezeigten Skills und Befehle statt ein bestimmtes Menü vorauszusetzen.

Die zwanzig Skills verbinden Einrichtung, Posteingang und Facharbeit mit dem Kanzleilauf. Neue Kanzleien beginnen mit `/kanzlei-starten`; der [Einrichtungsskill](../skills/kanzlei-gruenden-einrichten/SKILL.md) dokumentiert führende Systeme, Verantwortlichkeiten und Probemandat. Die weiteren Befehle starten unter anderem `/computerlauf`, `/kanzlei-tagesstart`, `/mandat-neu`, `/posteingang`, `/frist`, `/schriftsatz`, `/vertrag`, `/mandantenbrief`, `/zeit`, `/kanzlei-wochenabschluss`, `/rechnung`, `/zahlung`, `/uebergabe`, `/mandat-status`, `/mandat-ende` und `/freigabe`. Je nach Host erscheint ein Plugin-Präfix; ohne Befehlsmenü genügt der gleiche Auftrag als Satzanfang. Der [beA-Ablauf](bea-versand-empfang.md) verbindet Vorbereitung, Empfang und die bedingt zulässige Ausführung.

Freigegeben wird ein abgegrenzter Kanzleiordner mit einem Unterordner je Mandat. Die Helfer legen `00_Mandat`, `01_Bearbeitung`, `02_Honorar` und `03_beA_Vorbereitung` an. Python 3.10 genügt für die Kernhelfer; PDF-Werkzeuge benötigen die in der [Mandatsordner-Referenz](mandatsordner-und-cli.md) beschriebenen Pakete. Die autorisierte Einrichtung lautet beispielsweise:

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" init --akte "<Akte>" --matter-id "<ID>" --stufe 2
```

Die [Kanzleiorganisationsvorlage](../assets/kanzleiorganisation-vorlage.md) hält zuständige Menschen, Vertretung, führenden Kalender und zugelassene Dienste fest. Der Agent liest die ausgefüllte Fassung beim Tagesstart. Der [Demo-Kanzleiordner](../assets/demo-kanzlei/README.md) bietet drei fiktive Mandatsläufe ohne produktiven Postfachzugang. Die Zulässigkeit einer Umgebung für Mandatsdaten wird gesondert durch den Berufsrechtsskill geprüft.

## 1.3. Codex und ChatGPT mit Werkzeugzugriff

Das portable Paket enthält ein Agent-Plugin-Manifest. Ein Import ist nur zugesagt, soweit die konkrete Oberfläche ihn unterstützt. Prüfen Sie die angebotenen Datei-, Connector-, Browser- und Computersteuerungsfunktionen sowie deren Schemas und Berechtigungen. Nach der am 08.10.2026 geöffneten [OpenAI-Dokumentation](https://learn.chatgpt.com/docs/computer-use) bleiben Appzugriff, Betriebssystemrechte und Sandboxregeln getrennt. Das Plugin verändert diese Einstellungen nicht eigenmächtig.

Ist eine strukturierte Integration für eine erlaubte Aufgabe vorhanden, wird sie bevorzugt. Fehlt sie, kann ein erlaubtes Computerwerkzeug genutzt werden. Das Modell beobachtet dabei den tatsächlichen Zustand vor der Aktion und prüft danach das Ergebnis. Ein sichtbares Fenster beweist keinen zulässigen Zugriff auf alle Mandate. Ein Toolfehler wird nicht durch einen frei erfundenen erfolgreichen Versand ersetzt.

Der [integrierte Browser](https://learn.chatgpt.com/docs/browser) hat nach dem gelesenen Herstellertext eine Grenze bei automatisierten Datei-Uploads. Für Anhänge darf deshalb keine pauschale Uploadfähigkeit versprochen werden. Ein verbotenes Verfahren wird nicht über einen anderen Kanal umgangen. Bei fehlender Funktion übernimmt die befugte Person den betreffenden Upload oder Versand und liefert den tatsächlichen Nachweis; die übrige unabhängige Facharbeit läuft weiter.

## 1.4. ChatGPT im reinen Textmodus

Legen Sie ein Projekt an, soweit die Oberfläche Projekte unterstützt. Der Mini-Prompt `ki-native-kanzlei-schnellstart.txt` dient als Anweisung und bleibt unter 7.500 UTF-8-Bytes; die tatsächliche Eingabegrenze ist zusätzlich zu prüfen. Werkstatt, relevante Skills und Referenzen können als Projektdateien dienen. Für jedes Mandat wird der eigene Stand getrennt geführt. Mandatsdaten werden nur in eine dafür geprüfte Umgebung eingestellt.

Ohne Werkzeugzugriff führt ChatGPT keine Helfer aus und bedient keine fremden Postfächer. Es liefert ausformulierte Produkte, konkrete nächste Arbeitsschritte und den vollständigen [Mandatsstatus](mandatslauf-und-freigaben.md), ergänzt um Sitzungs- und Aktionsstand bei einer Simulation. Dateien gelten erst als gespeichert, wenn die Umgebung ihre Erzeugung bestätigt. Ein Chattext mit einem Pfad ist nur ein Exportvorschlag.

Sind Dateiausführung oder angeschlossene Apps verfügbar, kann der entsprechende Teil des Arbeitslaufs tatsächlich ausgeführt werden. Die Fähigkeit wird geprüft, nicht aus dem Produktnamen ChatGPT abgeleitet. Die Befehle funktionieren auch als Text, etwa: „Computerlauf: Simulation mit den drei Demoakten, nur Posteingang und Entwürfe“ oder „Tagesstart: Hier sind die Mandatsstände und die neuen Schreiben“.

## 1.5. Vom Entwurf zur beobachteten Ausführung

[mandatslauf.py](../scripts/mandatslauf.py) führt die fachlichen Produkte und Gates. [computerlauf.py](../scripts/computerlauf.py) führt den begrenzten Sitzungsauftrag und konkrete Aktionen; lesen Sie seine tatsächliche Hilfe und die [CLI-Referenz](computerlauf-cli.md). Beide Helfer sind lokale Journalwerkzeuge, keine Mail- oder beA-Transportdienste und keine Authentifizierung der eingetragenen Personen.

Der Ablauf lautet: Cockpit lesen, Eingang sichern, Akte und Frist bestimmen, Fachprodukt erstellen, konkrete Nachricht und Anlagen zur Entscheidung vorlegen, vorhandene menschliche Freigabe dokumentieren, genau die erlaubte Handlung über ein verfügbares Werkzeug ausführen, Ergebnis und gesonderten Eingangsnachweis kontrollieren, Zeit und Rechnungsentwurf fortführen, ins Cockpit zurückkehren. Der Agent wartet nur an der betroffenen Abhängigkeit. Eine fehlende Versandfreigabe stoppt nicht alle anderen Akten.

Outlook oder Gmail können bei passenden Werkzeugen und Berechtigungen tatsächlich verwendet werden; realer Versand setzt im Prototyp Stufe 3 voraus; beA verlangt zusätzlich den in der beA-Referenz bestimmten zulässigen Signatur- und Übermittlungsweg. Nach einem unklaren Versandversuch erfolgt zuerst ein Abgleich, niemals blindes erneutes Senden. Der Nutzer kann eine laufende Sitzung jederzeit beenden. Eine erneute Sitzung übernimmt offene Versuche, statt sie durch einen Neustart verschwinden zu lassen.

## 1.6. Erprobung und Aussagegrenzen

Ein sinnvoller erster Durchlauf nutzt ausschließlich den Demoordner und eine Simulation. Danach werden in einer getrennten Testumgebung Kontowechsel, falscher Empfängervorschlag, manipulierte Anlagenanweisung, Ablauf der Sitzung, Timeout und Wiederaufnahme erprobt. Bestehende produktive Konten sind kein Ersatz für eine sichere Testumgebung. Im Prüfbericht wird zwischen lokaler Journalprüfung, Textsimulation und tatsächlich beobachtetem Hostlauf unterschieden.

Keine Dokumentation behauptet allein durch das Vorhandensein eines Plugins einen erfolgreichen Liveversand, eine rechtswirksame beA-Einreichung oder eine dauerhafte Postfachüberwachung. Für letztere wäre ein gesondert beauftragter und tatsächlich eingerichteter Lauf mit Vertretung, Überwachung und Ausfallregel nötig. Der Rechtsstand der fachlichen Ausgangsfassung ist der 8. Oktober 2026; tragende Quellen werden im konkreten Mandat aktuell überprüft.
