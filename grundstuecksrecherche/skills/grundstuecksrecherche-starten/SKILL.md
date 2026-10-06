---
name: grundstuecksrecherche-starten
description: Startet die lokale Grundstücksrecherche-App und begleitet Stadtsuche, verifizierte NRW-Katasterauswahl oder manuelle Flurstückserfassung. Erklärt fehlende Ausführungs- oder Browsermöglichkeiten ohne eine Einbettung vorzutäuschen.
---

# 1. Grundstücksrecherche starten

## 1.1. Zweck und Anwendungsfall

Öffnen Sie die lokale App für die Suche nach Grundstücken in einer deutschen Stadt. Arbeiten Sie in deutscher Sie-Form. Die App ist der Arbeitsort; erzeugen Sie keine eigenständigen Begleitprompts.

## 1.2. Eingaben

Benötigt wird das vollständige Plugin-Verzeichnis. Prüfen Sie, ob die Oberfläche Codeausführung und eine erreichbare Browser- oder App-Vorschau anbietet. Alternativ liefern Sie die portable Website als ZIP; der Empfänger benötigt dafür nur einen aktuellen Browser. Die App beginnt ohne vorausgewählte Stadt. Übernehmen Sie eine ausdrücklich genannte Stadt erst für den konkreten Auftrag; fragen Sie sonst: „In welcher Stadt möchten Sie recherchieren?“

## 1.3. Ablauf

1. Lesen Sie die [Startanleitung](../../README.md). Prüfen Sie, ob lokaler Serverstart und Browserzugriff erlaubt und verfügbar sind. Bieten Sie immer auch an: „Ich kann Ihnen die Website als ZIP geben. Sie entpacken den Ordner und öffnen index.html.“ Behaupten Sie keine native Einbettung, wenn die aktuelle Oberfläche nur einen Download oder eine externe Browserseite unterstützt.
2. Für den App-Betrieb starten Sie im Plugin-Verzeichnis nach Einrichtung einer virtuellen Umgebung und Installation von `app/requirements.txt` den Befehl `python3 app/server.py --port 8765`. Verwenden Sie bei belegtem Port einen freien Port. Öffnen Sie die tatsächlich erreichbare lokale URL; ein gestarteter Prozess allein beweist noch keine funktionierende App. Wenn nur die Website gewünscht ist oder eine Serverausführung fehlt, gehen Sie unmittelbar zu Schritt 6; verlangen Sie dafür keine Serverinstallation beim Nutzer.
3. Lassen Sie die Stadt bestätigen, bei Mehrdeutigkeit mit Bundesland oder Kreis. Suchen Sie amtliche Quellen für diese Stadt. Bundesweite Quellensuche bedeutet nicht bundesweit verfügbare Katasterabfrage.
4. Nutzen Sie für NRW den amtlichen Katasterdienst. Übernehmen Sie nur tatsächlich zurückgelieferte Flurstückskennzeichen und Geometrien als verifiziert, mit Quelle und Abrufstand. Eine Hintergrundkarte oder ein Kartenklick genügt nicht. Bei fehlender Abdeckung oder Dienstausfall erfassen Sie Gemarkung, Flur und Flurstück manuell; kennzeichnen Sie diese Angaben als ungeprüft und halten Sie ihre Herkunft fest.
5. Leiten Sie keine Eigentümer aus offenen Karten ab. Halten Sie Eigentümerdaten und Mandatsunterlagen aus öffentlichen Suchanfragen heraus. Öffnen Sie `examples/nrw-muenster/reference/index.html` nur auf ausdrücklichen Wunsch; verändern Sie die Referenz nicht und laden Sie sie nicht als Startfall.

6. Für den Website-Download verwenden Sie in der App `Vorgang` → `Website als ZIP herunterladen` oder nach Installation der Abhängigkeiten `python3 app/portable.py grundstuecksrecherche-website.zip`. Ohne Codeausführung bieten Sie das [veröffentlichte Website-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundstuecksrecherche-website.zip) an; prüfen Sie dessen Erreichbarkeit, soweit Ihr Werkzeug dies erlaubt. Nennen Sie einen nicht überprüften oder noch ausstehenden Release-Download ausdrücklich so. Stellen Sie nur tatsächlich erzeugte oder veröffentlichte Dateien als vorhanden dar. Der Download darf nicht nur auf den Python-Quellcode oder die alte Münster-Referenz verweisen. Absender, Empfänger, Flurstücksauswahl und Begründungen nur nach ausdrücklicher Auswahl einschließen; ohne diese Auswahl bleibt der Export frei von Vorgangsdaten.
7. Erklären Sie den Unterschied knapp: `index.html` funktioniert ohne Server; Livekarten und neue Abfragen brauchen Internet und zulässigen Browserzugriff. Für vollständige Quellen- und Zuständigkeitsrecherche bleibt die App-Laufzeit erforderlich. Bei Ausfällen mit vorhandenem oder importiertem Vorgang und manuellen Angaben weiterarbeiten, statt die Browsersicherheit abzuschalten. Die Website kann aus geänderten Eingaben erneut vier echte DOCX-Entwürfe erzeugen.

## 1.4. Quellenpflicht

Verwenden Sie [Rechtsquellen](../../references/rechtsquellen.md) für fachliche Grenzen und `references/zitierweise.md` des Repositorys für rechtliche Nachweise, soweit verfügbar. Bestätigen Sie entscheidende Angaben anhand amtlicher Quellen oder bereitgestellter Belege. Stellen Sie fehlende oder gescheiterte Abfragen als solche dar.

## 1.5. Ausgabeformat

Liefern Sie die erreichbare App-URL oder das erzeugte Website-ZIP mit dem Hinweis „entpacken und index.html öffnen“ sowie den erfassten Ort und Auswahlstand. Trennen Sie bestätigte Katastertreffer und manuelle Angaben. Ein begleitender Vermerk erfüllt die Ausformulierungspflicht: vollständige Sätze, keine Skelette oder Halbsätze; formatierte Dokumente soweit möglich in Times New Roman 11 pt und ausschließlich dezimal gegliedert. Versprechen Sie keinen Export, den Sie nicht erzeugt haben.

## 1.6. Beispiele

„Starten Sie die Recherche für Köln.“ Öffnen Sie die App, bestätigen Sie den Ort und prüfen Sie den NRW-Katasterdienst. „Ich suche in Leipzig.“ Ermitteln Sie die dortigen amtlichen Angebote; bei fehlender passender Kartenabfrage bieten Sie die manuelle Erfassung an, ohne NRW-Treffer zu übertragen.
