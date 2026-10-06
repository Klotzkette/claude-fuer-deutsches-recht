---
name: grundstuecksrecherche-starten
description: Startet die lokale Grundstücksrecherche-App und begleitet Stadtsuche, verifizierte NRW-Katasterauswahl oder manuelle Flurstückserfassung. Erklärt fehlende Ausführungs- oder Browsermöglichkeiten ohne eine Einbettung vorzutäuschen.
---

# 1. Grundstücksrecherche starten

## 1.1. Zweck und Anwendungsfall

Öffnen Sie die lokale App für die Suche nach Grundstücken in einer deutschen Stadt. Arbeiten Sie in deutscher Sie-Form. Die App ist der Arbeitsort; erzeugen Sie keine eigenständigen Begleitprompts.

## 1.2. Eingaben

Benötigt werden das vollständige Plugin-Verzeichnis, erlaubte Codeausführung und Browserzugriff. Die App beginnt ohne vorausgewählte Stadt. Übernehmen Sie eine ausdrücklich genannte Stadt erst für den konkreten Auftrag; fragen Sie sonst: „In welcher Stadt möchten Sie recherchieren?“

## 1.3. Ablauf

1. Lesen Sie die [Startanleitung](../../README.md). Prüfen Sie, ob lokaler Serverstart und Browserzugriff erlaubt und verfügbar sind. Fehlt eine Möglichkeit, benennen Sie diese und den lokalen Startweg; behaupten Sie keine laufende App oder native Cowork-Einbettung.
2. Starten Sie im Plugin-Verzeichnis nach Einrichtung einer virtuellen Umgebung und Installation von `app/requirements.txt` den Befehl `python3 app/server.py --port 8765`. Verwenden Sie bei belegtem Port einen freien Port. Öffnen Sie die tatsächlich erreichbare lokale URL; ein gestarteter Prozess allein beweist noch keine funktionierende App.
3. Lassen Sie die Stadt bestätigen, bei Mehrdeutigkeit mit Bundesland oder Kreis. Suchen Sie amtliche Quellen für diese Stadt. Bundesweite Quellensuche bedeutet nicht bundesweit verfügbare Katasterabfrage.
4. Nutzen Sie für NRW den amtlichen Katasterdienst. Übernehmen Sie nur tatsächlich zurückgelieferte Flurstückskennzeichen und Geometrien als verifiziert, mit Quelle und Abrufstand. Eine Hintergrundkarte oder ein Kartenklick genügt nicht. Bei fehlender Abdeckung oder Dienstausfall erfassen Sie Gemarkung, Flur und Flurstück manuell; kennzeichnen Sie diese Angaben als ungeprüft und halten Sie ihre Herkunft fest.
5. Leiten Sie keine Eigentümer aus offenen Karten ab. Halten Sie Eigentümerdaten und Mandatsunterlagen aus öffentlichen Suchanfragen heraus. Öffnen Sie `examples/nrw-muenster/reference/index.html` nur auf ausdrücklichen Wunsch; verändern Sie die Referenz nicht und laden Sie sie nicht als Startfall.

## 1.4. Quellenpflicht

Verwenden Sie [Rechtsquellen](../../references/rechtsquellen.md) für fachliche Grenzen und `references/zitierweise.md` des Repositorys für rechtliche Nachweise, soweit verfügbar. Bestätigen Sie entscheidende Angaben anhand amtlicher Quellen oder bereitgestellter Belege. Stellen Sie fehlende oder gescheiterte Abfragen als solche dar.

## 1.5. Ausgabeformat

Liefern Sie die erreichbare App-URL oder die konkrete Ausführungsgrenze sowie den erfassten Ort und Auswahlstand. Trennen Sie bestätigte Katastertreffer und manuelle Angaben. Ein begleitender Vermerk erfüllt die Ausformulierungspflicht: vollständige Sätze, keine Skelette oder Halbsätze; formatierte Dokumente soweit möglich in Times New Roman 11 pt und ausschließlich dezimal gegliedert. Versprechen Sie keinen Export, den Sie nicht erzeugt haben.

## 1.6. Beispiele

„Starten Sie die Recherche für Köln.“ Öffnen Sie die App, bestätigen Sie den Ort und prüfen Sie den NRW-Katasterdienst. „Ich suche in Leipzig.“ Ermitteln Sie die dortigen amtlichen Angebote; bei fehlender passender Kartenabfrage bieten Sie die manuelle Erfassung an, ohne NRW-Treffer zu übertragen.
