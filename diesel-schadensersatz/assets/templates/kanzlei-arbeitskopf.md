# Kanzlei-Arbeitskopf

| Feld | Stand |
|---|---|
| Status | `[KANONISCHER_STATUS]` |
| Ampel | `[rot, gelb oder grün] - [ein fallbezogener Satz]` |
| Frist | `[TT.MM.JJJJ, Uhrzeit, Zeitzone; sonst: keine sichere Frist festgestellt]` |
| Quellenstand | `[Datum und amtliche Verifikation; sonst: Live-Prüfung offen oder keine Rechtsquelle verwendet]` |
| Arbeitsprodukt | `[genaue Bezeichnung des erzeugten oder geprüften Produkts]` |
| Nächster Schritt | `[genau eine konkrete Handlung oder genau ein Skill]` |

Zulässige Statuswerte: `BLOCKIERT`, `PRUEFUNG_NOETIG`, `STARTBEREIT`, `ARBEITSSTAND`, `FREIGABE_AUSSTEHEND`, `NICHT_VERSANDFERTIG`, `VERSANDFERTIG`, `NICHT_EINGEREICHT`, `EINGANG_UNGEKLAERT`, `EINGEREICHT`, `ERLEDIGT`.

Der Arbeitskopf ist eine Kontroll- und Begleitansicht. Er wird einem Arbeitsprodukt vorangestellt, gehört aber nie in einen Schriftsatz, eine Anlage oder eine Exportdatei. Kein Feld bleibt leer: Unbekanntes wird als offene Prüfung bezeichnet. `grün`, `VERSANDFERTIG`, `EINGEREICHT` und `ERLEDIGT` sind nur nach den jeweils vorgesehenen Kontrollen zulässig; ohne positiv kontrollierte automatisierte gerichtliche Eingangsbestätigung lautet der Status niemals `EINGEREICHT`.
