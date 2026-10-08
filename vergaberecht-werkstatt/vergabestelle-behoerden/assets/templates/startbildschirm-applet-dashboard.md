# Startbildschirm-Applets Vergabestelle

## Bedienprinzip

Der Startbildschirm soll in einer Antwort arbeitsfähig machen: Kurzlage, rote Fristen, Dokumentenmatrix, empfohlener Output und nächste konkrete Handlung. Keine reine Beratung ohne Vermerk, Matrix, Checkliste, Schriftsatzbaustein oder Uploadpaket.

## Intake-Kacheln

| Frage | Antwortfeld | Zweck |
|---|---|---|
| Was liegt vor? | Bedarfsanforderung, Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel, PDF, SAP/ERP/AVA/DMS-Export, Bauwerks-/Zustandsdaten, PMS/BMS, Planungsdaten, Bestandsplan, BIM/Fachmodell, Kosten/Nachträge, Genehmigungsplattform, Netzdaten, Klima/Umwelt, Normen, MCP, Bieterfrage, Rüge, VK-Schriftstück, Beschluss | Akte, Wirklichkeitsdaten und Quellsysteme sofort sortieren |
| Welche Rolle? | Vergabestelle, Fachbereich, Justiziariat, Zentrale Vergabestelle, Fördermittelempfänger, Beigeladene | Zuständigkeit und Freigabeweg festlegen |
| Welcher Verfahrensstand? | Planung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG, Vertrag, Interimsbedarf | Rechtsweg, Dokumentation und Fristen steuern |
| Welches Ziel? | Portfolio priorisieren, Bündelung prüfen, schneller beauftragen, LV bauen, Bestangebot sichern, Risiko navigieren, Abhilfe leisten, Verfahren verteidigen, Berichtigung veröffentlichen, Kostenrisiko begrenzen | Output auf Behördenentscheidung ausrichten |
| Welcher Output? | Vermerk, Entscheidungsvorlage, Rügeerwiderung, VK-Stellungnahme, OLG-Erwiderung, Tabelle, Checkliste, Uploadpaket | Nicht in Beratungstext stecken bleiben |

## Arbeitsstatus

| Friststatus | Aktenstand | Freigabestatus | Erstoutput |
|---|---|---|---|
| rot, gelb, grün oder offen | vollständig, lückenhaft oder ungeprüft | frei, gesperrt oder Freigabe offen | genau ein empfohlenes Arbeitsprodukt |

Unbekannte Werte als `offen` markieren. Fristen, Freigaben und Akteninhalte niemals ergänzen, wenn der Beleg fehlt.

## Antwortstandard

```markdown
## Kurzlage
[3 Sätze: Verfahren, Stand, Behördenziel]

## Fallkarte
Ausfüllen nach `assets/templates/fallkarte-output-weiche.md`: Falltyp, Normenanker, Tatbestand, Beweislast, Quellenstatus, Rechtsfolge, Outputwunsch.

## Rote Fristen
| Frist | Startpunkt | Ablauf | Aktenbeleg | Sofortmaßnahme |
|---|---|---|---|---|

## Arbeitsdashboard
| Applet | Wichtigster Befund | Aktenlücke | Nächster Schritt |
|---|---|---|---|

## Output-Auswahl
Empfohlen: [Vermerk/Rügeerwiderung/VK-Stellungnahme/Tabelle/Checkliste/Uploadpaket]
Alternativen: [maximal zwei]
```

## Schnellwahl

| Lage | Sofort-Applet | Output |
|---|---|---|
| Rüge eingegangen | Fristenampel plus Belegmatrix | Rügeerwiderung oder Abhilfevermerk |
| Unterlagen fehlerhaft | Dokumentenmatrix plus Upload-/Formatexport-Check | Berichtigungs- und Uploadpaket |
| Portfolio oder mehrere Bauwerke betroffen | Wirklichkeitsdaten-Matrix plus Portfolio-Applet | Prioritätenampel, Bündelungs- und Budgetvermerk |
| Beschleunigte Beauftragung gewünscht | Wertgrenzencheck plus Marktdaten-Applet | Direktauftrags-/Abruf-/Interimsvermerk |
| Wertung angegriffen | Wertungsmatrix plus Verteidigungslinien | Wertungsvermerk oder VK-Stellungnahme |
| Zuschlag blockiert | VK-/OLG-Streitdashboard | Eil-Erwiderung und Kostenvermerk |
| Akteneinsicht verlangt | Schwärzungs- und Belegmatrix | Akteneinsichtsschreiben |

## Stabiler Großaktenmodus

Ab 50 Dateien oder 250 MB zuerst nur Metadaten und Fristdokumente erfassen. Danach in Paketen von höchstens 20 Dateien oder 100 MB arbeiten, große PDF- und Office-Dateien einzeln verarbeiten und nach jedem Paket `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine beschädigte Datei wird protokolliert; der übrige Fall läuft weiter.

## Applet-Suite

| Applet | Spalten | Sofortaktion |
|---|---|---|
| Fristenampel | Frist, Startpunkt, Ablauf, Beleg, Risiko, Sofortmaßnahme | rote Fristen zuerst berechnen und verifizieren |
| Fallkarte/Output-Weiche | Falltyp, Norm, Tatbestand, Beweislast, Quellenstatus, Rechtsfolge, Outputwunsch | abstrakte Beratung in eine Behördenentscheidung übersetzen |
| Dokumentenmatrix | Dokument, Format, Version, Quelle, Pflichtinhalt, Lücke, Aktenstelle | Vergabeakte und Datenformate prüffähig machen |
| Belegmatrix | Entscheidung, Aktenstelle, Datei, Seite/Position, Begründung, Nachweiswert | jede Behördenentscheidung belegfähig machen |
| Wirklichkeitsdaten-Matrix | Quelle, Objekt, Befund, Datenqualität, Vergabefolge, Fachfreigabe, Szenario | Bedarf, Bündelung, LV, Budget und Kriterien aus realen Daten ableiten |
| Portfolio-Applet | Objekt, Zustand, Ausfallwirkung, Korridor, Budget, Priorität, Bündelung | Maßnahmen priorisieren und Haushalts-/Loslogik vorbereiten |
| Beschleunigungs-Applet | Wert, Schwelle, Landeswertgrenze, Anbieterfeld, Dringlichkeit, Binnenmarktrelevanz | Direktauftrag, Rahmenabruf, Interimsbedarf oder Verfahrenserleichterung aktenfest prüfen |
| Mobilitäts-/Tragfähigkeits-Applet | Bauwerk, Netz, Korridor, Tragfähigkeit, Sperrfenster, Nutzungsrisiko | LV, Eignung, Ausführungszeit und Risikoverteilung an realer Nutzbarkeit ausrichten |
| Varianten-Applet | Einzelvergabe, Bündelung, Rahmen, ÖPP, CAPEX, Fertigteil/Serie, Lebenszyklus | Beschaffungsvariante und Bestwertungslogik vergleichbar machen |
| Angriffslinien | Rügepunkt, Tatsache, Norm, behauptete Kausalität, begehrte Abhilfe, Eilrisiko | Bieterangriff sauber erfassen |
| Verteidigungslinien | Aktenbeleg, Wertungsspielraum, Gleichbehandlung, Transparenz, Präklusion, Heilung | VK-Stellungnahme und Abhilfeentscheidung vorbereiten |
| Wertungsmatrix | Kriterium, Gewicht, Bewertung, Dokumentation, Fehlerverdacht, Reparaturpfad | Wertung überprüfbar und verteidigbar machen |
| Legacy-/MCP-Integrationscheck | Quellsystem, Objekt, Schlüssel, Version, Hash, Mapping, Zielsystem, Freigabe, Rückmeldung | Altsysteme und moderne Schnittstellen kontrolliert anbinden |
| Upload-/Formatexport-Check | Zielformat, Portal, Feldliste, Dateiname, Hash, Freigabe, Nachweis | Bekanntmachung, Berichtigung oder Unterlagenpaket veröffentlichungsfähig machen |

## Output-Menü

| Ziel | Erstoutput | Folgeoutput |
|---|---|---|
| Unterlagen reparieren | Abhilfevermerk mit Korrekturliste | Berichtigungs- und Uploadpaket |
| Portfolio priorisieren | Quellen- und Szenariomatrix | Bündelungs-, Budget- und Losvermerk |
| Beschaffung beschleunigen | Wertgrenzen-, Markt- und Dringlichkeitsmatrix | Direktauftrags-, Abruf- oder Interimsvermerk |
| Mobilität/Tragfähigkeit absichern | Korridor- und Tragfähigkeitsmatrix | LV-Risikoblatt und Kriterienvermerk |
| ÖPP/CAPEX/Fertigteil prüfen | Varianten- und Lebenszyklusmatrix | Gremienvorlage und Gleichwertigkeitscheck |
| Rüge beantworten | Rügeerwiderung mit Belegmatrix | Nichtabhilfevermerk oder Berichtigung |
| Zuschlag sichern | Fristen- und Risikovermerk | Vergabekammer-Stellungnahme |
| Akteneinsicht steuern | Schwärzungsmatrix und Geheimnisakte | VK-Schreiben und Bieteranhörung |
| Vergleich suchen | Vergleichskorridor mit Gremienfreigabe | Umsetzungs- und Kostenplan |
| Amtsblatt/Portal bedienen | eForms-/TED-/DVAL-/Portalauftrag | Uploadnachweis und Aktenvermerk |

## Nutzungscheck

| Frage | Ja/Nein/Lücke |
|---|---|
| Kann die Vergabestelle jetzt entscheiden, ob sie abhilft, verteidigt, berichtigt oder zuschlägt? |  |
| Sind Frist, Freigabeinhaber, Aktenbeleg und nächste Datei benannt? |  |
| Ist der nächste Portal-, DMS-, MCP- oder Amtsblatt-Schritt klar? |  |
| Gibt es genau einen empfohlenen Output und höchstens zwei Alternativen? |  |
