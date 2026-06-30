# Clean-Entwurf Checkliste

## Status

Vorzulegen vor jedem Versand eines Clean-Entwurfs an Mieter oder Vermieter. Erstellt durch RA Klotzkette, Stand 18.05.2026.

## Pflicht-Prüfungen

- [ ] **Parteienrubrum vollständig:** Vermieter (BSAG inkl. Anschrift, Vorstand, Handelsregister Bremen HRB 24501), Mieter (Scherflein GmbH inkl. Anschrift, Registerdaten, USt-IdNr., Geschäftsführer).
- [ ] **Mietobjekt:** Adresse, Fläche (18 qm Verkauf + 6 qm Lager), Lage im Haltestellenbereich (Bahnsteig West), Nutzungsbeschreibung übereinstimmend mit Term Sheet.
- [ ] **Mietzins:** Kaltmiete (1.450,00 EUR), Nebenkostenpauschale (320,00 EUR), Gesamtmiete (1.770,00 EUR) - jeweils in Ziffern UND in Worten ("eintausendvierhundertfuenfzig Euro").
- [ ] **Umsatzsteueroption:** Klausel zur Option nach § 9 UStG eingefügt; Vorsteuerbescheinigung Scherflein liegt vor (Anlage 4).
- [ ] **Kaution:** Drei Bruttomonatsmieten (5.310,00 EUR oder mit USt 6.318,90 EUR) - klarstellen, ob brutto oder netto.
- [ ] **Laufzeit:** Festmietzeit 01.07.2026 bis 30.06.2031 (fünf Jahre) eindeutig; Verlängerungsoption 2 x 3 Jahre konsistent mit Term Sheet (NICHT 2 x 2 wie in Vorlage).
- [ ] **Kündigungsrechte:** Ordentlich nach Ende Festzeit + Optionen; ausserordentlich nach Gesetz; keine versteckten Sonderkündigungsrechte.
- [ ] **Sonderbedingungen eingebaut:** Konkurrenzschutz § 8a, Sortimentsbindung § 8b, Fettabscheider § 10a, Abfall zweimal pro Woche § 10 Abs. 3, Rückbau § 14 mit Ausnahme genehmigte Einbauten.
- [ ] **Anlagen verzeichnet:** Lageplan, Grundriss mit Flaechenmass, Übergabeprotokoll-Muster, Vorsteuerbescheinigung, Liste vorab genehmigter Einbauten.

## Form-Prüfungen

- [ ] Alle Klammerstellen `<< ... >>` ersetzt - mit `grep` über das DOCX prüfen.
- [ ] Schriftbild durchgängig (Calibri 11, Überschriften Calibri 12 bold, einheitliche Absatzformatierung).
- [ ] Seitenzahlen, Fusszeile mit Aktenzeichen VAF-2026-BSAG-007.
- [ ] Unterschriftenblock für beide Seiten mit Ort, Datum, Name, Funktion.
- [ ] Keine Track-Changes-Reste, keine internen Kommentare.

## Inhalt-Prüfungen

- [ ] Mietzweck (Imbiss/Zeitungen/Lotto) und Sortimentsbindung widerspruchsfrei.
- [ ] Konkurrenzschutz-Klausel deckt sich mit den Antworten der BSAG (Umfang, Ausnahmen).
- [ ] Wertsicherungsklausel - nur falls vereinbart; bei diesem Vertrag aktuell NICHT vereinbart, daher streichen.
- [ ] Schriftformklausel: jede Änderung schriftlich, auch der Änderungsvorbehalt selbst (BGH zur doppelten Schriftformklausel beachten).
- [ ] Gerichtsstand und anwendbares Recht (Bremen, deutsches Recht).

## Pruefung Mandanteninteressen

- [ ] Rückfragen aus `03_rueckfragen_bsag.md` beantwortet und im Entwurf umgesetzt.
- [ ] Risiken (Konkurrenzschutz-Ausnahmen, Rückbauumfang) im Mandantenbrief angesprochen.
- [ ] Bei Abweichungen vom Term Sheet erfolgt schriftlicher Hinweis im Versandschreiben.

## Track Changes

- [ ] Track-Changes-Fassung NICHT erstellen, sofern nicht ausdrücklich angefordert. Mandantenbrief bzw. BSAG-Antwort dokumentieren.
- [ ] Bei Anforderung: Vergleichsdokument gegen die generische BSAG-Vorlage erstellen, alle Änderungen sichtbar, jede Klausel kommentiert.

## Versand

- [ ] Clean-Entwurf als PDF und DOCX an BSAG und Scherflein GmbH.
- [ ] Kopie Aktenexemplar in `claude-fuer-deutsches-recht/testakten/vertragsausfueller-bsag-kiosk-huckelriede/clean_entwurf/`.
- [ ] Fristenlauf für Rueckaeusserung (sieben Tage) im Fristenkalender setzen.
- [ ] Erst nach Freigabe beider Seiten: Unterschriftstermin koordinieren (Notar nicht zwingend, gewerbliches Mietverhältnis).
