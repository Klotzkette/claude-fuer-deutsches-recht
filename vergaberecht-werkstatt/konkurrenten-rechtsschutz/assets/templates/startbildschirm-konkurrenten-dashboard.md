# Startbildschirm-Applets Konkurrentenrechtsschutz

## Bedienprinzip

Der Startbildschirm soll in einer Antwort streitfähig machen: Kurzlage, rote Fristen, stärkster Angriff, Belegmatrix, empfohlener Output und nächster Schriftsatz- oder Anlagenpunkt. Keine reine Beratung ohne Fristenampel, Belegmatrix, Angriffslinie, Kostenblick oder Schriftsatzbaustein.

## Intake-Kacheln

| Feld | Eingabe |
| --- | --- |
| Rolle | Konkurrent, unterlegener Bieter, ausgeschlossener Bieter, Bewerber, Nachunternehmer, Kanzlei |
| Verfahrensstand | Bekanntmachung, Angebotsphase, Wertung, § 134 GWB, Nichtabhilfe, VK, OLG, Zuschlag, Vertrag |
| Ziel | Unterlagen ändern, Frist verlängern, Zuschlag stoppen, Konkurrent ausschließen, neue Wertung, Akteneinsicht, Unwirksamkeit, Schadensersatz |
| Rote Frist | Angebotsfrist, Rügefrist, 15-Tage-Frist, Stillhaltefrist, OLG-Frist |
| Legacy-Beweisquelle | SAP/ERP/AVA/DMS, Portal, API, MCP, E-Mail, Exportlog, Hash |
| Output | Rüge, Nachprüfungsantrag, Eilantrag, Akteneinsicht, OLG-Beschwerde, Vergleichsvorschlag, Kostenmemo |

## Arbeitsstatus

| Friststatus | Belegstand | Schutzstatus | Erstoutput |
|---|---|---|---|
| rot, gelb, grün oder offen | tragfähig, lückenhaft oder ungeprüft | Zuschlag gesperrt, Zuschlag möglich oder offen | genau ein empfohlener Angriffsschritt |

Unbekannte Werte als `offen` markieren. Fristbeginn, Zuschlagschance und Akteninhalt niemals ergänzen, wenn der Beleg fehlt.

## Antwortstandard

```markdown
## Kurzlage
[3 Sätze: Verfahren, Stand, Angriffsziel]

## Fallkarte
Ausfüllen nach `assets/templates/fallkarte-output-weiche.md`: Falltyp, Normenanker, Tatbestand, Darlegungslast, Quellenstatus, Rechtsfolge, Outputwunsch.

## Rote Fristen
| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|

## Streitdashboard
| Hebel | Beleg | Risiko | Nächster Schritt |
|---|---|---|---|

## Output-Auswahl
Empfohlen: [Rüge/Nachprüfungsantrag/Eilantrag/Akteneinsicht/OLG/Kostenmemo]
Alternativen: [maximal zwei]
```

## Schnellwahl

| Lage | Sofort-Applet | Output |
|---|---|---|
| Unterlagen oder Produktvorgabe sperren Wettbewerb | Dokumentenmatrix plus Gleichwertigkeitscheck | Bieterfrage oder Rüge mit Änderungsantrag |
| Reine Preiswertung verdeckt Qualitätsfehler | Wertungsmatrix plus Preisformeltest | Rüge oder VK-Antrag auf neue Wertung |
| Konkurrent möglicherweise ungeeignet | Eignungs- und Belegmatrix | Akteneinsichts- und Ausschlussangriff |
| Nichtabhilfe liegt vor | Fristenampel plus Zulässigkeitsdreieck | Nachprüfungsantrag mit Anlagenplan |
| Zuschlag droht | Schutzstatus plus Eil-Applet | VK-Antrag und Antrag nach § 169 GWB |
| VK-Beschluss liegt vor | OLG-Reserve plus Kostenrisiko | zugleich begründete Beschwerde oder Erwiderung |

## Stabiler Großaktenmodus

Ab 50 Dateien oder 250 MB zuerst nur Metadaten, Fristdokumente und Zugangsbelege erfassen. Danach in Paketen von höchstens 20 Dateien oder 100 MB arbeiten, große PDF- und Office-Dateien einzeln verarbeiten und nach jedem Paket `Datei | Hash | Status | Ergebnis | Fehler | nächster Lauf` fortschreiben. Eine beschädigte Datei wird als Beweislücke protokolliert; die übrigen Angriffe laufen weiter.

## Applet-Suite

| Applet | Spalten | Sofortaktion |
|---|---|---|
| Fristenampel | Frist, Startpunkt, Ablauf, Beleg, Risiko, Sofortmaßnahme | Präklusion und Zuschlagsrisiko zuerst sichern |
| Fallkarte/Output-Weiche | Falltyp, Norm, Tatbestand, Darlegungslast, Quellenstatus, Rechtsfolge, Outputwunsch | Verdacht in konkrete Angriffslinie und Antrag übersetzen |
| Dokumentenmatrix | Dokument, Version, Quelle, Zugang, Pflichtinhalt, Widerspruch, Akteneinsichtslücke | Streitstoff und fehlende Vergabeakte trennen |
| Belegmatrix | Behauptung, Datei, Seite/Position, Zeitstempel, Hash, Beweiswert | jeden Angriff belegfähig machen |
| Angriffslinien | Fehler, Norm, Tatsache, Kausalität, Zuschlagschance, Abhilfe, Antrag | Rüge und VK-Antrag vorbereiten |
| Verteidigungslinien | erwarteter Einwand, Präklusion, Wertungsspielraum, Dokumentationsbeleg, Kausalität, Replik | Gegenposition der Vergabestelle vorwegnehmen |
| Wertungsmatrix | Kriterium, Gewicht, veröffentlichter Maßstab, Wertung, Fehler, Zuschlagschance | Angriff auf Preisautomatismus oder Qualitätswertung quantifizieren |
| Legacy-/MCP-Beweiscluster | Quellsystem, Objekt, Schlüssel, Version, Hash, Angriff, Freigabe, Rückmeldung | Altsysteme und Portalbelege streitfest anbinden |
| Akteneinsicht/Schwärzung | Zielakte, Geheimnis, Schwärzung, Replikbedarf, Antrag | Einsicht erzwingen und Geheimnisschutz vorbereiten |
| Versand-/Zustellcheck | Adressat, Kanal, Frist, Signatur, Anlagen, Hash, Quittung | Rüge und Schriftsatz nachweisbar zustellen |
| Kostenrisiko | Streitwert, Gebühr, Anwaltsbedarf, Vergleichskorridor, Rücknahmefenster | Eskalation wirtschaftlich steuern |

## Output-Menü

| Ziel | Erstoutput | Folgeoutput |
|---|---|---|
| Unterlagen ändern | Rüge mit Belegmatrix | Nichtabhilfe-Reaktion oder VK-Antrag |
| Zuschlag stoppen | Eilantrag/Zuschlagssperre | Nachprüfungsantrag mit Anlagen |
| Konkurrent ausschließen | Ausschlussangriff | Akteneinsicht und Wertungsreplik |
| Neue Wertung erzwingen | Wertungsangriff | VK-Antrag und Vergleichskorridor |
| Vertrag angreifen | De-facto-/§-135-Memo | Unwirksamkeitsantrag oder Kostenmemo |
| OLG vorbereiten | Beschwerdebriefing | Anlagen- und Fristenpaket |

## Nutzungscheck

| Frage | Ja/Nein/Lücke |
|---|---|
| Kann der Konkurrent jetzt rügen, den VK-Antrag stellen, Zuschlag stoppen oder Akteneinsicht beantragen? |  |
| Sind Frist, Beleg, Angriffsziel und Anlagenpfad benannt? |  |
| Ist der nächste Portal-, DMS-, MCP- oder Gerichtsschritt klar? |  |
| Gibt es genau einen empfohlenen Output und höchstens zwei Alternativen? |  |
