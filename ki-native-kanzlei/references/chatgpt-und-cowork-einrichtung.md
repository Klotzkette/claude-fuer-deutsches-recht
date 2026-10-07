# 1. ChatGPT und Claude Cowork einrichten

## 1.1. Claude Cowork und Claude Code

Das Plugin-ZIP des Komponentenreleases wird in Claude Cowork über die Pluginverwaltung hochgeladen oder in Claude Code über den Marketplace dieses Repositorys installiert. Danach stehen die achtzehn Skills und die Befehle aus dem Ordner `commands` zur Verfügung: `/kanzlei-tagesstart`, `/mandat-neu`, `/posteingang`, `/frist`, `/schriftsatz`, `/vertrag`, `/mandantenbrief`, `/zeit`, `/kanzlei-wochenabschluss`, `/rechnung`, `/zahlung`, `/uebergabe`, `/mandat-status`, `/mandat-ende` und `/freigabe`. Jeder Befehl startet einen Ablauf aus der [Kanzleialltag-Referenz](kanzleialltag-workflows.md).

Für die Arbeit wird ein Kanzleiordner freigegeben, in dem jedes Mandat einen Unterordner hat. Die Helfer im Ordner `scripts` legen darin `00_Mandat` (Journal und Mandatslauf), `01_Bearbeitung` (Arbeitsprodukte), `02_Honorar` (Honoraransichten) und `03_beA_Vorbereitung` (Versandpakete) an. Python 3.10 genügt; die PDF-Werkzeuge für beA-Pakete benötigen die in der Mandatsordner-Referenz genannten Pakete. Die Freigabestufe wird beim Anlegen des Mandatslaufs mit `mandatslauf.py init --stufe` gesetzt. Für den Beginn empfiehlt sich Stufe 1 oder 2.

Vor dem ersten echten Mandat legt die Kanzlei schriftlich fest, wer welche Gates freigeben darf, wer Vertretung hat, welcher Kalender führend ist und welche externen Dienste nach § 43e BRAO zugelassen sind. Diese Festlegung gehört als Datei in den Kanzleiordner, etwa `Kanzleiorganisation.md`; eine ausformulierte [Vorlage](../assets/kanzleiorganisation-vorlage.md) liegt dem Plugin bei, und die Maschine liest die ausgefüllte Datei beim Tagesstart. Zum Ausprobieren enthält das Plugin einen [Demo-Kanzleiordner](../assets/demo-kanzlei/README.md) mit drei fiktiven Mandatsläufen; `python3 scripts/mandatslauf.py cockpit --kanzlei assets/demo-kanzlei --format md` zeigt das Cockpit. Die Zulässigkeit der eingesetzten KI-Umgebung selbst prüft der Skill anwaltsberufsrecht-pruefen vor der ersten Übermittlung von Mandatsdaten.

## 1.2. ChatGPT

In ChatGPT wird ein Projekt angelegt. In die Projektanweisungen kommt der Mini-Prompt (`ki-native-kanzlei-schnellstart.txt`); er bleibt unter der Grenze für Anweisungen. Als Projektdateien werden der Werkstatt-Prompt, diese Referenzen (Kanzleialltag, Mandatslauf und Freigaben, Arbeitsweise, Rechtsquellen, Zitierweise) und bei Bedarf einzelne Skills hochgeladen. Für jedes Mandat entsteht ein eigener Chat im Projekt; Mandatsunterlagen werden nur nach der berufsrechtlichen Prüfung der Umgebung eingestellt.

ChatGPT führt ohne lokalen Dateizugriff keine Helfer aus. Der Mandatslauf wird deshalb als Textblock am Ende jeder Antwort geführt: Phase, führende Fassungen mit Datei und Stand, Fristobjekte mit Zustand, Honorarstand, Zeitstand, offene Gates und offene Fragen. Beim nächsten Schritt liest das Modell diesen Block wieder ein. Erzeugte Dateien werden als Download geliefert und von der Kanzlei in den Mandatsordner gelegt. Steht in der ChatGPT-Umgebung eine Code-Ausführung mit Dateien zur Verfügung, können `kanzlei.py`, `fristen.py`, `mandatslauf.py` und `xrechnung.py` hochgeladen und dort ausgeführt werden; die Ergebnisse sind dann ebenfalls herunterzuladen.

Die Befehle aus Claude Cowork werden in ChatGPT als Sätze verwendet, zum Beispiel: „Tagesstart: Hier sind die Statusblöcke der fünf Mandate und der heutige Posteingang“, „Neue Anfrage: …“, „Frist: Versäumnisurteil mit Zustellungsurkunde anbei“ oder „Freigabe G3, RAin Dr. Ahrens, Klage Fassung 04“.

## 1.3. Codex

Das portable Paket enthält ein Manifest für Agent-Plugins. Ob und wie es in einem ChatGPT- oder Codex-Konto importiert werden kann, hängt von der Freischaltung des Kontos ab. Ist der Import möglich, arbeiten Skills und Helfer wie in Claude Code; sonst gilt der Weg über das ChatGPT-Projekt.

## 1.4. Grenzen in allen Umgebungen

Keine Umgebung wird durch das Plugin zu einem Dienst, der selbständig einreicht, versendet, bucht, zahlt, meldet oder löscht. Kalender, beA, Buchhaltung und Bank bleiben Systeme der Kanzlei. Das Plugin bereitet die Produkte für diese Systeme vor und dokumentiert Freigaben und Nachweise. Rechtsstand der Skills ist der 7. Oktober 2026; tragende Normen und Entscheidungen werden im konkreten Mandat am amtlichen Text geprüft.
