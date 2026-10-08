# Computerlauf: technische Prüfung am 8. Oktober 2026

## 1. Ergebnis und geprüfter Umfang

Der neue [Computerlauf-Helfer](../../../ki-native-kanzlei/scripts/computerlauf.py) führt Sitzungen und einzelne Aktionsmanifeste mit getrennten Freigaben, Ausführungsversuchen, Ergebnissen und Empfangsprüfungen. Die [CLI-Referenz](../../../ki-native-kanzlei/references/computerlauf-cli.md) erläutert Schema, konkrete Aufrufe und Grenzen. Die bestehende Freigabestufensystematik wird nicht ersetzt; der Modus `simulation` oder `live` kommt als davon getrennte Eigenschaft hinzu.

**Ergebnis: 35 automatisierte Tests und eine reproduzierbare Offline-Demo mit 22 Schritten bestanden. Es wurde kein Konto geöffnet, keine Nachricht versandt und kein beA-Zugang eingerichtet.** Die Demo verwendet ausschließlich erfundene Konten, Personen, Zustimmungen, Routenvermerke und Ausgangsbelege. Der Wert `live` bezeichnet in dieser lokalen Zustandsprobe keine tatsächlich angebundene Transportfunktion.

## 2. Wesentliche Prüfungen

| Bereich | Konkrete Prüfung | Ergebnis |
| --- | --- | --- |
| Datei- und Empfängerbindung | Geänderte Betreffdatei, Nachricht, Anlage, CC/BCC oder Freigabebeleg verhindern den Start. | Bestanden |
| Scope | Fremdes Konto, falsche App, nicht zugelassene Domain, unbekanntes Mandat, absolute Pfade, Pfadwechsel nach außen und symbolische Links werden abgewiesen. | Bestanden |
| Geheimnisse | Zusätzliche JSON-Felder `pin`, `software_token` und `password` werden abgewiesen und nicht journalisiert. Freitext ist dadurch kein Geheimnisfilter. | Bestanden |
| Sitzung | Simulation startet nicht; Stufe 2 versendet nicht; Lesen einer konkret bezeichneten Nachricht ist auf Stufe 2 möglich; Ablauf und Stopp verhindern neue Starts. | Bestanden |
| Wiederholung | Erneuter Start derselben Aktion sowie gleicher Versandinhalt unter neuer Kennung werden gesperrt; bloße Reihenfolgeänderungen von Empfängern oder Anhängen öffnen keinen neuen Versuch. | Bestanden |
| Unklarer Ausgang | Timeout beziehungsweise unklarer Ausgang erlaubt keinen weiteren Versuch. Ein belegter Nichteintritt verlangt vor Wiederholung eine neue konkrete Freigabe. | Bestanden |
| Parallelität | Zwei tatsächlich gleichzeitig gestartete Unterprozesse erzeugen genau einen erfolgreichen Start und einen Versuch. | Bestanden |
| Absturz | Eine Reservierung zwischen `.attempt` und Journalaktualisierung sperrt Starts auch unter anderer Aktionskennung und verhindert einen Sitzungswechsel. Dokumentierte Klärung erhält die Historie. | Bestanden |
| beA | Persönliche Route liefert `wartet_auf_mensch`; eine andere Person darf die persönliche Ausführung nicht bestätigen. eEB kann nicht über eine Mail-App an der persönlichen Prototypregel vorbeigeführt werden. | Bestanden |
| Empfang | Ergebnis und Empfangsprüfung bleiben getrennt. Negative Empfangsbelege öffnen eine bereits ausgeführte Aktion nicht erneut. | Bestanden |
| Sitzungswechsel | Abgeschlossene Aktionen bleiben erhalten. Später gelesene Empfangsbelege beziehen sich weiterhin auf das ursprüngliche Mandatsverzeichnis. | Bestanden |
| Fehlerhafter Zustand | Ein defektes Journal wird abgewiesen und nicht überschrieben. | Bestanden |

Bei der Implementierung wurden insbesondere ein Umgehungsweg über eine neue Aktionskennung nach unvollständig journalisierter Reservierung und eine falsche spätere Belegauflösung bei geändertem Mandatsverzeichnis durch Gegenproben festgestellt und beseitigt. Die Reservierungsprüfung gilt nun vor jedem neuen Start und vor dem Sitzungswechsel. Ein veränderter rein interner Routenvermerk erzeugt ebenfalls keinen neuen Nachrichteninhalt für die Doppelversandprüfung.

## 3. Reproduktion

Vom Repository-Wurzelverzeichnis aus:

```sh
python3 scripts/test-ki-native-kanzlei-computerlauf.py
python3 quality/ki-native-kanzlei/agentisch-2026-10-08/computerlauf-demo.py --out /tmp/kk339/computerlauf-neue-probe
```

Das Ausgabeverzeichnis der Demo muss neu oder leer sein. Das [Probeskript](computerlauf-demo.py) legt die vollständigen Eingabe-JSONs, ein fiktives Mandatsverzeichnis und `protokoll.json` mit Eingaben, Rückgabecodes, Ergebnissen und Fehlermeldungen an. Es überschreibt keine bestehende Probe. Der hier geprüfte Lauf liegt als [vollständiges Protokoll](computerlauf-demo-protokoll.json) bei; der ursprüngliche lokale Pfad war `/tmp/kk339/computerlauf-demo-final/protokoll.json`.

Die 22 Schritte zeigen zuerst eine gesperrte Simulation, dann eine ausschließlich lokal protokollierte Rechnung über ein fiktives Outlook-Konto und schließlich eine persönliche beA-Route. Die zweite Outlook-Ausführung wird abgewiesen. Der beA-Versuch wartet auf die fiktive Ada Ahrens; eine Bestätigung durch den fiktiven Bertram Brecht wird abgewiesen. Die richtige fiktive Bestätigung dokumentiert anschließend lediglich den Übungszustand. Am Ende ist die Sitzung gestoppt. Alle drei erwarteten Abbrüche treten ein.

## 4. Grenzen der Aussage

Die Tests belegen lokale Zustandsübergänge und ausgewählte Konsistenzsperren. Sie prüfen keine tatsächliche Outlook-, Gmail-, Cowork-, Codex- oder beA-Integration, keine Zulässigkeit eines konkreten Geheimniszugangs, keine Identität einer bestätigenden Person und keine Wirksamkeit einer Signatur oder Einreichung. Der Helfer setzt keine fachlichen Mandatslauf-Gates automatisch auf freigegeben und erzeugt keine Transportberechtigung.

Der Computerlauf ist kooperativ. Personen mit Schreibrechten können Dateien und Programm ändern; mehrere unabhängig angelegte Journale teilen keine Doppelversandhistorie. Das Sperrverfahren schützt gleichzeitig kooperierende lokale Prozesse, nicht gegen absichtliche Umgehung oder einen kompromittierten Rechner. Originale werden vom Helfer nicht verändert; vor dem realen Hostschritt müssen die tatsächliche Vorschau, die richtige Sitzung und die unveränderte Fassung erneut übereinstimmen. Eine bereits laufende Hostaktion lässt sich durch einen Journaleintrag nicht zurückholen.
