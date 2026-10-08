# Startbildschirm-Applets Bieter

## Bedienprinzip

Der Startbildschirm soll in einer Antwort handlungsfähig machen: Kurzlage, rote Fristen, Dokumentenmatrix, empfohlener Output und nächste konkrete Handlung. Keine reine Beratung ohne Angebotspaket, Matrix, Checkliste, Rüge, Schriftsatzbaustein oder Uploadpaket.

## Intake-Kacheln

| Frage | Antwortfeld | Zweck |
|---|---|---|
| Was liegt vor? | Bekanntmachung, Unterlagen, LV, GAEB, XML, Excel, PDF, SAP/ERP/CRM/AVA/DMS-Export, MCP, Bieterfrage, Nachforderung nach § 56 VgV, Ausschlussschreiben, Angebotsöffnung, Preisblattfehler, Steuer-/Sozialabgabenbescheid, betroffenes Mitglied einer Bietergemeinschaft, Rüge, Nichtabhilfe, Informationsschreiben, VK-Schriftstück, Beschluss | Material und Quellsysteme sofort verwerten |
| Welche Rolle? | Bewerber, Bieter, Beigeladener, Zuschlagsprätendent, Nachunternehmer, Kanzlei | Perspektive, Adressat und Ton festlegen |
| Welcher Verfahrensstand? | Markterkundung, Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nachprüfung, OLG, Vertrag, Schadensersatz | Rechtsweg und Fristen steuern |
| Welches Ziel? | Angebot retten, Unterlagen ändern, Ausschluss angreifen, Konkurrent ausschließen, Zuschlag stoppen, Akteneinsicht, Vergleich, Kostenrisiko begrenzen | Output auf Entscheidung ausrichten |
| Welcher Output? | Schriftsatz, Rüge, Nachprüfungsantrag, Eilantrag, Tabelle, Checkliste, Memo, Angebotspaket, Uploadpaket | Nicht in Beratungstext stecken bleiben |

## Arbeitsstatus

| Friststatus | Unterlagenstand | Freigabestatus | Erstoutput |
|---|---|---|---|
| rot, gelb, grün oder offen | vollständig, lückenhaft oder ungeprüft | frei, gesperrt oder Freigabe offen | genau ein empfohlenes Arbeitsprodukt |

Unbekannte Werte als `offen` markieren. Fristen, Portalvorgaben und Angebotsinhalte niemals ergänzen, wenn der Beleg fehlt.

## Antwortstandard

```markdown
## Kurzlage
[3 Sätze: Verfahren, Stand, Ziel]

## Fallkarte
Ausfüllen nach `assets/templates/fallkarte-output-weiche.md`: Falltyp, Normenanker, Tatbestand, Darlegungslast, Quellenstatus, Rechtsfolge, Outputwunsch.

## Rote Fristen
| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|

## Arbeitsdashboard
| Applet | Wichtigster Befund | Lücke | Nächster Schritt |
|---|---|---|---|

## Output-Auswahl
Empfohlen: [Schriftsatz/Rüge/Tabelle/Checkliste/Angebotspaket/Uploadpaket]
Alternativen: [maximal zwei]
```

## Schnellwahl

| Lage | Sofort-Applet | Output |
|---|---|---|
| Unterlagen unklar | Dokumentenmatrix plus Belegmatrix | Fragenliste oder Rügevorbereitung |
| Angebotsformat unklar | Upload-/Formatexport-Check | Angebotspaket mit Freigabeliste |
| Wertung zweifelhaft | Wertungsmatrix plus Angriffslinien | Rüge oder Nachprüfungsantrag |
| Nachforderung oder Ausschlussschreiben | Eignungs-/Ausschlussmatrix plus Fristenampel | Nachreichungsplan, Rüge oder VK-Reserve |
| Bietergemeinschaft oder Steuer-/Sozialabgabenproblem | Mitglieder- und Compliance-Matrix | Austausch-/Selbstreinigungsplan |
| Zuschlag droht | Fristenampel plus VK-/OLG-Streitdashboard | Rüge, Eilantrag, Nachprüfungsantrag |
| Akteneinsicht nötig | Belegmatrix plus Geheimnisschutzprüfung | Akteneinsichtsantrag |

## Stabiler Großaktenmodus

Ab 50 Dateien oder 250 MB zuerst nur Metadaten, Bekanntmachung und Fristdokumente erfassen. Danach in Paketen von höchstens 20 Dateien oder 100 MB arbeiten, große PDF- und Office-Dateien einzeln verarbeiten und nach jedem Paket `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine beschädigte Datei wird protokolliert; Angebot und Fristprüfung laufen mit den übrigen Dateien weiter.

## Applet-Suite

| Applet | Spalten | Sofortaktion |
|---|---|---|
| Fristenampel | Frist, Startpunkt, Ablauf, Beleg, Risiko, Sofortmaßnahme | rote Fristen zuerst berechnen und verifizieren |
| Fallkarte/Output-Weiche | Falltyp, Norm, Tatbestand, Darlegungslast, Quellenstatus, Rechtsfolge, Outputwunsch | abstrakte Beratung in Angebots-, Rüge- oder VK-Handlung übersetzen |
| Dokumentenmatrix | Dokument, Format, Version, Quelle, Pflichtinhalt, Lücke, nächster Schritt | Unterlagen und Datenformate auslesbar machen |
| Belegmatrix | Behauptung, Belegstelle, Datei, Seite/Position, Gegnerargument, Beweiswert | jede Rüge belegfähig machen |
| Angriffslinien | Fehler, Norm, Tatsache, Kausalität, Zuschlagschance, Abhilfe, Antrag | Rüge und VK-Antrag vorbereiten |
| Verteidigungslinien | Gegeneinwand, Präklusion, Dokumentationsbeleg, Wertungsspielraum, fehlende Kausalität, Replik | Erwartung der Vergabestelle vorwegnehmen |
| Wertungsmatrix | Kriterium, Gewicht, Bewertung, Abweichung, Angriffspunkt, neue Wertung | Zuschlagschance und Kausalität quantifizieren |
| Legacy-/MCP-Integrationscheck | Quellsystem, Objekt, Schlüssel, Version, Hash, Angebotsmapping, Zielsystem, Freigabe, Rückmeldung | Altsysteme und moderne Schnittstellen kontrolliert anbinden |
| Upload-/Formatexport-Check | Zielformat, Tool, Dateiname, Hash, Signatur, Portalnachweis, Freigabe | Angebot oder Schriftsatz abgabefähig machen |

## Output-Menü

| Ziel | Erstoutput | Folgeoutput |
|---|---|---|
| Unterlagen klären | Fragenliste oder Rügeentwurf | Angebotscheck und Fristenplan |
| Zuschlag stoppen | Rüge mit Belegmatrix | Nachprüfungsantrag und Eilantrag |
| Akteneinsicht erzwingen | Akteneinsichtsantrag mit Geheimnisschutzvorschlag | Replik nach Aktenauszug |
| Konkurrent angreifen | Ausschluss-/Wertungsangriff | VK-Antrag mit Anlagenverzeichnis |
| Vergleich suchen | Vergleichskorridor mit Mindestziel | Kosten- und Umsetzungsplan |
| Angebot abgeben | Format- und Uploadpaket | Portalnachweis und Freigabevermerk |

## Nutzungscheck

| Frage | Ja/Nein/Lücke |
|---|---|
| Kann der Bieter jetzt anbieten, nachfragen, rügen, hochladen oder eskalieren? |  |
| Sind Frist, Freigabeinhaber, Beleg und nächste Datei benannt? |  |
| Ist der nächste Portal-, DMS-, MCP- oder Zielsystemschritt klar? |  |
| Gibt es genau einen empfohlenen Output und höchstens zwei Alternativen? |  |
