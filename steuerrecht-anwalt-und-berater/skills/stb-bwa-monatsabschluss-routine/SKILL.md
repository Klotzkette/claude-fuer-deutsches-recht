---
name: stb-bwa-monatsabschluss-routine
description: "Routine für den Monatsabschluss in der Steuerberater-Kanzlei. Anwendungsfall monatliche BWA-Erstellung in einem standardisierten 30-Tage-Zyklus mit Belegabgabe Buchung Abstimmung BWA-Versand. Schritte Belegannahme Buchung GoBD-konform OPOS-Pflege Lohnbuchung-Integration Bestand-Schaetzung Periodenabgrenzung Auswertung. Output Monatsendreport Termincontrolling Querverweis stb-routine-monatsabschluss-30-tage-zyklus."
---

# Monatsabschluss-Routine fuer den Steuerberater

## Kernsachverhalt

Die wirtschaftliche Aussagekraft einer BWA haengt entscheidend von der Disziplin des Monatsabschluss-Zyklus ab. Ohne klaren Prozess verzoegert sich die BWA, der Mandant verliert das Vertrauen, Krisensignale werden zu spaet erkannt. Dieser Skill etabliert eine reproduzierbare 30-Tage-Routine, die in DATEV oder Addison genauso funktioniert wie in Sage oder BuchhaltungsButler — mit klar zugeordneten Verantwortlichkeiten zwischen Mandant, Sachbearbeiter und Berufstraeger.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Belegvolumen, Komplexitaet, Kontenrahmen?
2. Welche Belegabgabe-Form ist vereinbart — Papier, DATEV Unternehmen Online, BuchhaltungsButler, scan-zentrum?
3. Welcher Auswertungstermin ist mit dem Mandanten verbindlich vereinbart — bis zum 15., 20., 25. des Folgemonats?
4. Wer bucht (Sachbearbeiter), wer prueft (Berufstraeger), wer versendet?
5. Liegen Lohnbuchungen aus dem Lohnprogramm rechtzeitig vor (in der Regel Monatsmitte des Folgemonats)?
6. Welche Periodenabgrenzungen werden routinemaessig gebucht (RAP, Rueckstellungen, Abschreibungen)?
7. Gibt es Sonderpflichten — Konzernanforderung, Bankreporting, fortlaufender Liquiditaetsplan?
8. Welche Eskalation bei verspaeteter Belegabgabe (Mahnung, Honorar-Aufschlag, BWA-Verschiebung)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 238, 239 HGB** — Buchfuehrungspflicht und ordnungsgemaesse Buchfuehrung.

**§§ 140, 141, 146 AO** — Aufzeichnungs- und Buchfuehrungspflichten; § 146 Abs. 1 AO Zeitgerechtigkeit der Buchungen.

**§ 90 AO** — Mitwirkungspflicht des Mandanten (Belegabgabe).

**§ 147 AO / § 257 HGB** — Aufbewahrungsfristen 6 bzw. 10 Jahre.

**§ 33 StBerG** — Aufgaben des Steuerberaters (Buchfuehrung als Hilfeleistung in Steuersachen).

**§ 35 StBVV** — Honorar fuer Buchfuehrung; Anhang 5 zur StBVV.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 (BStBl I 2019, 1269) — GoBD; Anforderungen an zeitgerechte Buchungen (regelmaessig binnen 10 Tagen; spaetestens Monatsende).
- BMF v. 25.08.2020 (DSGVO im Steuerberater-Verhaeltnis).

## Workflow

### Phase 1 — Tag 1-5 des Folgemonats: Belegabgabe und Wareneingang

- Mandant uebermittelt Belege bis spaetestens 5. des Folgemonats (digital ueber DATEV Unternehmen Online).
- Belegannahme-Kontrolle: Vollstaendigkeit Eingangsrechnungen, Ausgangsrechnungen, Bankauszuege, Kassenauszuege, Lohnauswertungen.
- Pruefung Kassenfuehrung GoBD-konform (taegliche Aufzeichnungen, Z-Bons).
- OP-Listen vom Vormonat anfordern: noch nicht bezahlte Eingangsrechnungen, ueberfaellige Ausgangsrechnungen.

### Phase 2 — Tag 5-15: Buchung Tagesarbeit

- Bankbuchungen: GVC-Kontierung (DATEV) oder Banking-Kontierung.
- Eingangsrechnungen: gegen OPOS abgleichen, USt-Behandlung (Vorsteuer, Reverse-Charge, innergemeinschaftlicher Erwerb).
- Ausgangsrechnungen: aus Faktura-Modul oder manuelle Buchung; USt-Schluessel pruefen.
- Kassenbuchung: tageweise mit Z-Bon-Verprobung.
- Lohnbuchungen aus Lohnprogramm integrieren (Loehne, Sozialabgaben, Pauschalsteuer).

### Phase 3 — Tag 15-20: Abstimmung und Periodenabgrenzung

- Kontenabstimmung: Bank gegen Bankauszug, Kasse gegen Kassenbericht, Verrechnungskonten 1590/1599 (SKR 03) bzw. entsprechende SKR-04-Konten auf null.
- Rueckstellungen monatlich anteilig: Urlaub, Tantiemen, Berufsgenossenschaft, Pruefungskosten.
- Abschreibungen monatlich oder kumuliert (1/12-Methode aus Anlagenbuchhaltung).
- Aktive und passive Rechnungsabgrenzung (Versicherung, Miete, Kfz-Steuer) auf den Monat zerlegt.
- Bestandsveraenderung: bei Handel monatliche Schaetzung (Warenroll), bei Industrie Zwischeninventur quartalsweise.

### Phase 4 — Tag 20-25: Plausibilisierung

- Pruefung Umsatzentwicklung vs. Vormonat und Vorjahres-Monat.
- Vorsteuer-Pruefung: VAT-Konten sauber, Innergemeinschaftliche Lieferungen mit Bestaetigung der USt-Id.
- USt-Voranmeldung erstellen (§ 18 UStG) — bis zum 10. des Folgemonats (ggf. Dauerfristverlaengerung).
- BWA-Vorabauswertung pruefen: Ist das Ergebnis plausibel? Materialquote, Personalquote, Sondereffekte?

### Phase 5 — Tag 25-30: BWA-Erstellung und Versand

- BWA aus DATEV/Addison/Sage erstellen mit Vorjahresvergleich und kumuliertem Jahresblock.
- Erlaeuterungstext (1-2 Seiten) ergaenzen.
- Berufstraeger-Pruefung (4-Augen-Prinzip) — Stichproben, Plausibilitaet, Krisensignale.
- BWA an Mandant versenden (DATEV Unternehmen Online, E-Mail mit verschluesseltem Anhang).
- Monatsabschluss in Mandantenakte dokumentieren mit Zeitstempel und Bearbeiter.

### Phase 6 — Nachgang: Mandantenkommunikation

- Bei Auffaelligkeiten Mandant telefonisch oder im Meeting kontaktieren.
- Termin fuer Quartalsgespraech ankuendigen (alle 3 Monate).
- Bei wiederholten Belegabgabe-Verzoegerungen Mahnschreiben mit Honoraranknuepfung (Zuschlag fuer Eilfall).

## Output

- BWA mit Vorjahresvergleich und Erlaeuterungstext.
- USt-Voranmeldung uebermittelt.
- OPOS-Listen aktualisiert.
- Mandantenakte mit Monatsabschluss-Eintrag dokumentiert.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Strategie und Praxis-Tipps

- 30-Tage-Zyklus mit klaren Deadlines (Tag 5 Belegannahme, Tag 15 Buchungsende, Tag 25 BWA fertig) durchhalten.
- Schwellenmandant: bei mehr als 200 Belegen monatlich automatische Belegeingangs-Erkennung (DATEV DUO) sinnvoll.
- Personalkosten brauchen vorgezogene Datenuebernahme — Lohnabteilung muss BWA-relevante Buchungen bis Tag 12 liefern.
- Honoraranknuepfung StBVV § 33: Buchfuehrungspauschale pro Monat, BWA-Erstellung separat als Vereinbarung.
- Bei Krisensignalen (negative BWA, Eigenkapitalerosion) automatische Eskalation an Berufstraeger (Querverweis stb-bwa-sus-bilanz-pruefung).

## Querverweise

- `stb-routine-monatsabschluss-30-tage-zyklus` — vertiefte Prozessbeschreibung.
- `stb-bwa-aufbau-grundlagen` — BWA-Struktur.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe-Checkliste.
- `stb-bwa-fehlerquellen-haeufig` — typische Fehler im Monatsabschluss.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignal-Check.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239, 257.
- AO §§ 140, 141, 146, 147.
- StBerG § 33.
- StBVV § 33 (Buchfuehrung), Anhang 5.
- BMF v. 28.11.2019, BStBl I 2019, 1269 (GoBD).
- Verifikations-Hinweis: GoBD-Update bei BMF-Anpassungen jaehrlich pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
