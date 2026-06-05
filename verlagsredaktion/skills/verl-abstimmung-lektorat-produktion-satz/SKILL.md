---
name: verl-abstimmung-lektorat-produktion-satz
description: "Verl Abstimmung Lektorat Produktion Satz: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verl Abstimmung Lektorat Produktion Satz

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Verl Abstimmung Lektorat Produktion Satz** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verl-abstimmung-mit-lektorat-format` | Klaert Lektorats- und Redaktionsstandards: wer ist fuer welchen Pruefschritt zustaendig wie wird uebergeben Track-Changes Stand Versionierung Eskalationsregeln. |
| `verl-abstimmung-mit-produktion-satz-druck` | Klaert die Schnittstelle zur Produktion: Satzdaten Format Bildaufloesung Schriftrechte Fahnenlauf Druckfreigabe Online-Auslieferung und Reklamationswege. |
| `verl-abstimmung-mit-rechtsabteilung-pruefung` | Inhouse-Legal-Check vor Veroeffentlichung: strukturierte Abstimmung mit Justiziariat zu Aeusserungsrecht, Persoenlichkeitsrecht, Urheberrecht, Wettbewerbsrecht und Datenschutz. |
| `verl-abstimmung-mit-vertrieb-marketing` | Briefing fuer Vertrieb und Marketing zu einem Verlagsprodukt: Zielgruppe Kernnutzen Vergleichstitel Preisarchitektur und Material fuer Katalog Webseite Veranstaltungen. |
| `verl-audio-transkript-zu-fachbeitrag` | Destilliert einen Audio-Vortrag oder ein freies Diktat zu einem zitierfaehigen Fachbeitrag fuer juristische Fachzeitschriften und Sammelbaende. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Verl Abstimmung Lektorat Produktion Satz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verl-abstimmung-mit-lektorat-format`

**Fokus:** Klaert Lektorats- und Redaktionsstandards: wer ist fuer welchen Pruefschritt zustaendig wie wird uebergeben Track-Changes Stand Versionierung Eskalationsregeln.

# Abstimmung Lektorat / Redaktion (Format-Klaerung)

## Worum geht es konkret

Lektorat und Redaktion arbeiten am selben Manuskript, oft parallel. Ohne klare Schnittstelle entstehen Doppelarbeit, widerspruechliche Eingriffe und Versionschaos. Dieser Skill klaert die Schnittstelle: Zustaendigkeiten, Versionierungsregeln, Track-Changes-Konventionen, Eskalationswege.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, wenn Lektorat und Redaktion neu aufgestellt sind, ein neues Manuskript-Tool eingefuehrt wird oder Konflikte aufkommen. Klaeren Sie:

1. Welche Lektoratsdienste (intern, freie Lektorinnen, beides)?
2. Welche Tools (Word Track Changes, LaTeX-Diff, CMS)?
3. Welche Versionierungslogik?
4. Welche Eskalation bei inhaltlichen Lektoratseingriffen?

## Material- bzw. Sachrahmen

- Aktueller Lektoratsleitfaden / Style Guide.
- Workflow-Diagramm (falls vorhanden).
- Liste der typischen Reibungspunkte.

## Praxisleitfaden / Schritt fuer Schritt

1. **Schnittstelle festlegen.**
 - **Redaktion:** inhaltliche Beurteilung, Annahme/Ablehnung, Heftslot, Beitragsformat.
 - **Lektorat:** Sprache, Stil, Format, Zitiernorm, Konsistenz, ggf. Korrekturlauf.
2. **Uebergabeprotokoll.** Jede Uebergabe mit Datum, Bearbeiter, Versionsstand, was gemacht wurde, was noch offen ist.
3. **Versionierungsregeln.** Dateiname `Autor-Titel_vN_status.docx` mit klarem Status (`eingang`, `lekt1`, `lekt2`, `red1`, `freigabe`, `druck`).
4. **Track-Changes-Konvention.** Wer schaltet TC ein/aus? Wer kommentiert? Wer akzeptiert? Bei Word: jeweils Autorinnenname in den Einstellungen.
5. **Inhaltliche Eingriffe.** Lektorat darf nicht inhaltlich umstellen ohne Ruecksprache Redaktion. Markierung "INH:" als Vorschlag.
6. **Eskalation.** Wenn Redaktion und Lektorat verschiedene Meinungen haben, dokumentiert in Kommentaren, Entscheidung Schriftleitung.
7. **Schluss-Uebergabe** mit Pruefliste (Format, Zitate, Stil, Konsistenz).

## Trade-off-Matrix

| Pfad | A: Strikte Zustaendigkeitstrennung | B: Hybride Arbeitsweise | Empfehlung |
|------|-------------------------------------|--------------------------|------------|
| Klarheit | hoch | mittel | A bei groesserem Verlag |
| Flexibilitaet | gering | hoch | B bei kleinem Team |
| Konflikthaeufigkeit | gering | mittel | A schuetzt vor Drift |

## Praxistipps der alten Redaktion

- "Track-Changes ist ein Versprechen: jeder Strich wird gesehen. Wer es nicht respektiert, baut Schattenversionen."
- Versionsstaende immer im Dateinamen - Word-Versionierungs-Funktion ist nicht zuverlaessig.
- Inhaltliche Lektoratseingriffe in Kommentaren begruenden - das schuetzt die Schriftleitungsentscheidung.
- Wenn das Lektorat extern (Freelancer) ist: NDA und Hauseigene Stilkatalog vorab.
- Konflikte werden in der Akte dokumentiert - sonst sind sie nach drei Wochen vergessen.

## Mustertexte / Vorlagen

**Uebergabeprotokoll (Vorlage):**

```
Uebergabeprotokoll
Manuskript: Mueller, "Plattformhaftung" / NJW 14/2026
Datum: 12.06.2026
Von: Lektorat (Frau Schmidt)
An: Redaktion (Herr Lehmann)
Versionsstand: Mueller-Plattform_v3_lekt1.docx
Geleistet:
- Format-Check (siehe Befund)
- Zitiernorm-Check (siehe Befund)
- Sprachlektorat (Track-Changes)
- 7 inhaltliche Vorschlaege als Kommentare markiert (INH:)
Offen:
- Aussagensicherheits-Pruefung (Mandantenfrage S. 12) - bei Redaktion
- Bildrechte fuer 2 Schaubilder
```

**Eskalations-Notiz:**

> Sehr geehrte Schriftleitung, wir bitten um Klaerung zu drei inhaltlichen Differenzen zwischen Lektorat und Redaktion bei Mueller "[Titel]":
>
> 1. S. 7: Lektorat schlaegt Glaettung "innovativ" -> "neuartig" vor; Redaktion will Autorenstimme respektieren.
> 2. S. 18: Lektorat sieht Mandantenbezug als zu duenn anonymisiert; Redaktion sieht ausreichend.
> 3. S. 23: Lektorat schlaegt Streichung der Spitze gegen BAFin vor; Redaktion sieht durch Belege gedeckt.
>
> Bitte um Entscheidung bis 19.06.2026 (Heftschluss).

**Versionsstand-Schema:**

```
Mueller-Plattform_v1_eingang.docx (vom Autor)
Mueller-Plattform_v2_lekt0.docx (nach Format-Check)
Mueller-Plattform_v3_lekt1.docx (nach Sprachlektorat)
Mueller-Plattform_v4_red1.docx (nach Redaktion)
Mueller-Plattform_v5_aut.docx (Autor-Rueckmeldung)
Mueller-Plattform_v6_freigabe.docx (alle Aenderungen akzeptiert)
Mueller-Plattform_v7_druck.docx (an Produktion)
```

## Typische Fehler / Pitfalls

- Track-Changes ausgeschaltet ohne Hinweis - Schattenversionen.
- Inhaltliche Lektoratseingriffe ohne Ruecksprache.
- Versionsstand nur in Word-Eigenschaften, nicht im Dateinamen.
- Externe Lektorinnen ohne NDA.
- Konfliktdokumentation fehlt - alte Streits werden neu gefuehrt.

## Querverweise

- `verl-formatvorlage-check-autor-manuskript` - Format-Check vor Lektorat.
- `verl-zitierweise-pruefung-zeitschrift-jus-njw` - Zitat-Pruefung.
- `verl-redaktionelle-rueckmeldung-formulieren` - Stil der Rueckmeldung.
- `lektorat-struktur-redaktion` - Strukturlektorat.
- `verl-jourfix-vorbereiten-protokoll` - Jourfix-Werkzeug.

## Quellen Stand 06/2026

- Allgemeine Workflow- und Kollaborationsstandards: keine spezifische juristische Quelle.
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024.
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.
- Moellers, Juristische Arbeitstechnik, 11. Aufl. 2023.
- Plachta, Editionswissenschaft, 4. Aufl. 2020 (zu Versionierungsdisziplin).

## 2. `verl-abstimmung-mit-produktion-satz-druck`

**Fokus:** Klaert die Schnittstelle zur Produktion: Satzdaten Format Bildaufloesung Schriftrechte Fahnenlauf Druckfreigabe Online-Auslieferung und Reklamationswege.

# Abstimmung Produktion / Satz / Druck

## Worum geht es konkret

Nach der inhaltlichen und sprachlichen Freigabe geht das Manuskript in die Produktion: Satz, Layout, Korrekturfahnen, Druckfreigabe, Druck, Auslieferung. Auch wenn diese Schritte oft an externe Dienstleister gehen, bleibt die Redaktion verantwortlich fuer Termintreue und Endqualitaet. Dieser Skill beschreibt die saubere Produktionsschnittstelle.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn bei der Uebergabe an die Produktion und bei Reklamationen. Klaeren Sie:

1. Inhouse-Satz oder externer Setzer?
2. Welches Druckverfahren (Offset, Digital, Print-on-Demand)?
3. Welche Bilddaten-Qualitaet (300 dpi+ fuer Print)?
4. Welche Schriftrechte (Lizenz der Setzschrift, OFL?)?

## Material- bzw. Sachrahmen

- Freigegebenes Manuskript (alle Aenderungen akzeptiert).
- Bilddateien in Druckqualitaet, separat.
- Layoutvorgaben (Style Guide Print).
- Druckschrift mit Lizenznachweis.
- Termine (Druckfreigabe, Druck, Auslieferung).

## Praxisleitfaden / Schritt fuer Schritt

1. **Uebergabe-Paket fuer Setzer:**
 - Manuskript als .docx (freigegeben, alle Aenderungen akzeptiert).
 - Bilder als separate Dateien in 300+ dpi.
 - Tabellen ggf. separat als .xlsx.
 - Style-Anweisungen / Vorlage.
 - Inhaltsverzeichnis / Stichwortverzeichnis.
2. **Erste Satzfahne pruefen** mit `satzfahne-korrekturlauf`.
3. **Korrekturen markieren** im PDF (Adobe Acrobat-Kommentare oder ausgedruckt mit Korrekturzeichen).
4. **Zweite Fahne** auf Vollstaendigkeit der Korrekturen pruefen.
5. **Druckfreigabe** schriftlich, mit Versionsstand und Datum.
6. **Druckueberwachung.** Stichprobe aus Druck, Termin pruefen.
7. **Auslieferung.** Verlag, Buchhandel, Online-Lizenz aktivieren.
8. **Reklamationen.** Defekte, Druckfehler, Setzfehler dokumentieren und an Setzer / Drucker melden.

## Trade-off-Matrix

| Pfad | A: Inhouse-Satz | B: Externer Setzer | Empfehlung |
|------|-----------------|---------------------|------------|
| Kosten pro Druck | hoch (Personal) | mittel | B im Regelfall |
| Kontrolle | hoch | mittel | A bei sensiblen Produkten |
| Termintreue | hoch | mittel | beide brauchen Eskalation |
| Datenschutz | gut | abhaengig von AVV | A bei Mandantendaten |

## Praxistipps der alten Redaktion

- "Druckfreigabe ist eine Unterschrift, nicht ein Mailsatz. Wird im Streitfall gebraucht."
- Bilder im Manuskript eingebunden sind fuer Setzer minderwertig - immer separat in 300+ dpi.
- Tabellen mit komplexer Struktur als .xlsx zusaetzlich liefern, nicht nur als Word-Tabelle.
- Schriftrechte pruefen - bei kommerziellen Druckereien Standardschriften verfuegbar, bei Sonderschriften Lizenznachweis.
- Bei Loseblattwerk: Ergaenzungslieferungen brauchen ueberlappende Termine und klare Versionskontrolle.

## Mustertexte / Vorlagen

**Uebergabe-Checkliste Produktion:**

```
[ ] Manuskript freigegeben (Versionsstand: ____)
[ ] Alle Aenderungen akzeptiert (Track-Changes leer)
[ ] Bilder separat in 300+ dpi
[ ] Bildquellen / Credits geprueft (siehe bildrechte-grafiken-tabellen)
[ ] Tabellen als .xlsx separat
[ ] Inhaltsverzeichnis / Stichwortverzeichnis
[ ] Impressum, Titelei, Backmatter
[ ] Druckschrift / Lizenz geprueft
[ ] Termine eingetragen (Satz, Korrektur 1, Korrektur 2, Druckfreigabe, Druck, Auslieferung)
[ ] Ansprechpartner Verlag und Setzer benannt
```

**Druckfreigabe-Vorlage:**

> Verlag [Name] erteilt fuer das Werk
> Mueller, "Praxiskommentar Plattformhaftung", 1. Auflage 2027
> Versionsstand: v9_freigabe_2026-12-15.pdf
> die Druckfreigabe.
>
> Druckumfang: 480 Seiten + Vorsatz/Nachsatz
> Auflage: 1.500 Exemplare
> Auslieferung: 03.03.2027
>
> Datum: 15.12.2026
> Unterschrift: _______________________
> Funktion: Verlagsleitung

**Anschreiben Setzer:**

> Sehr geehrte Frau Setzerin, wir uebergeben hiermit das freigegebene Manuskript Mueller "Praxiskommentar Plattformhaftung" zur Satzbearbeitung (siehe Anlagen). Layoutvorgaben gemaess Verlagsstyleguide, Druckschrift Stempel Garamond mit Hauslizenz. Erste Satzfahne erwarten wir bis 30.07.2026. Bei Rueckfragen ...

## Typische Fehler / Pitfalls

- Bilder im Word, nicht separat - Druckqualitaet schlecht.
- Druckfreigabe ohne Versionsstand - im Streitfall nicht beweisbar.
- Schriftrechte uebersehen - Drucker reklamiert.
- Termine zu eng, kein Puffer fuer zweite Korrekturfahne.
- Reklamationen ohne Dokumentation - bei nachstehender Auflage gleicher Fehler.

## Querverweise

- `satzfahne-korrekturlauf` - Korrekturlauf der Fahne.
- `produktionsuebergabe-checkliste` - Produktionsuebergabe-Skill.
- `bildrechte-grafiken-tabellen` - Bildrechte.
- `verl-abstimmung-mit-lektorat-format` - Lektorats-Schnittstelle vor Produktion.
- `verl-buchprojekt-bauleiter` - Buchprojekt-Bauleiter.

## Quellen Stand 06/2026

- Verlagsgesetz, [https://www.gesetze-im-internet.de/verlg/](https://www.gesetze-im-internet.de/verlg/).
- UrhG §§ 31 ff. fuer Schriftnutzungsrechte.
- DIN 16511 (Korrekturzeichen).
- ISO 12647 (Druckfarbsteuerung Offset).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024.
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.

## 3. `verl-abstimmung-mit-rechtsabteilung-pruefung`

**Fokus:** Inhouse-Legal-Check vor Veroeffentlichung: strukturierte Abstimmung mit Justiziariat zu Aeusserungsrecht, Persoenlichkeitsrecht, Urheberrecht, Wettbewerbsrecht und Datenschutz.

# Inhouse-Legal-Check vor Veroeffentlichung

## Worum geht es konkret

Vor Drucklegung oder Onlineschaltung muss bei rechtssensiblen Beitraegen das Justiziariat des Verlags eingebunden werden. Das betrifft insbesondere: namentliche Berichte ueber Verfahrensbeteiligte, scharfe Urteilskritik, Praxisberichte mit Mandantenbezug, Beitraege zu Streitthemen mit grossen Marktteilnehmern, KI-erstellte Inhalte. Der Skill liefert einen Vorlagenpfad, der dem Justiziariat in 15 Minuten Pruefbarkeit verschafft.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welcher Beitrag (Aufsatz, Anmerkung, Kommentierung, Blog, Newsletter, Pressetext)?
2. Welche Personen oder Unternehmen werden namentlich genannt?
3. Werden Aktenzeichen, Verfahrensdetails oder vertrauliche Sachverhalte verwendet?
4. Liegen Bild- oder Tabellenrechte vor (Lizenz, Schoepfungshoehe, Public Domain)?
5. Ist ein Faktencheck-Datum dokumentiert?
6. Wird Wettbewerbsbezug (vergleichende Werbung, Aussagen ueber Konkurrenten) hergestellt?
7. Welche Frist gibt die Redaktion dem Justiziariat?

## Rechtlicher und sachlicher Rahmen

- KUG §§ 22, 23 - Bildnisrecht; Einwilligung erforderlich, Ausnahmen fuer Personen der Zeitgeschichte.
- BGB §§ 823, 824, 1004 analog - Schutz des allgemeinen Persoenlichkeitsrechts und der Kreditgefaehrdung.
- StGB §§ 185-187 - Beleidigung, ueble Nachrede, Verleumdung als strafrechtliche Grenze.
- Art. 5 GG - Meinungs- und Pressefreiheit als Abwaegungsmassstab.
- UrhG §§ 51, 51a - Zitatrecht, Karikatur/Parodie/Pastiche.
- DSGVO Art. 6, 17, 85 - Datenverarbeitung im journalistischen Privileg.
- UWG §§ 6, 7 - vergleichende Werbung, Belaestigung; bei Marketingtexten relevant.
- DDG (Digitale-Dienste-Gesetz) als Nachfolger des TMG seit 2024; § 5 DDG Impressumspflicht, § 18 MStV journalistische Sorgfalt fuer Telemedien mit journalistisch-redaktioneller Pragung.

## Praxisleitfaden / Schritt fuer Schritt

1. **Vorselektion durch Redaktion.** Ein Pruefkanon laeuft jedem Beitrag voraus. Bei "Ja" zu einem der folgenden Punkte: Justiziariat einschalten.
 - Namentliche Berichterstattung ueber lebende Personen mit kritischer Bewertung.
 - Aktenzeichen aus laufenden Verfahren mit identifizierender Wirkung.
 - Behauptungen ueber konkrete Pflichtverletzungen, Unwirksamkeiten von AGB Dritter, Verstoesse gegen Berufsrecht.
 - Bildmaterial ohne klare Lizenz oder ohne Personenrechte.
 - Sponsored Content, Affiliate-Links, vergleichende Aussagen.
2. **Pruefpaket schnueren.** Manuskriptfassung mit Stand, Quellenliste, ggf. Bildlizenzen, ggf. Anonymisierungsentscheidungen, gewuenschte Online- und Printtermine.
3. **Pruefauftrag schreiben.** Nicht "schaut mal druber", sondern konkrete Fragen: "Ist Passage S. 3 Abs. 2 zulaessige Werturteil oder unwahre Tatsachenbehauptung?"
4. **Frist setzen.** Mindestens fuenf Werktage vor Imprimatur; bei Brennthemen 24 Stunden mit explizitem Hinweis.
5. **Rueckmeldung schriftlich.** "Freigabe", "Freigabe mit Aenderungen", "Pruefbedarf", "Abgelehnt" - keine telefonische Halbfreigabe.
6. **Aenderungen umsetzen.** Jede juristische Aenderung mit dem Autor abstimmen, sonst wird der Beitrag verfaelscht.
7. **Dokumentation.** Pruefauftrag, Antwort und finale Fassung gemeinsam ablegen (Beweisvorsorge bei Klage).

## Trade-off-Matrix

| Aspekt | Justiziariat eng einbinden | Redaktion entscheidet allein |
|---|---|---|
| Risiko | Niedriger | Hoeher |
| Tempo | Langsamer | Schneller |
| Autorenbindung | Sicherheit, aber Eingriffe | Vertrauen, aber Risiko |
| Folgekosten | Vorab teurer, hinten billiger | Vorab billig, ggf. teurer Rechtsstreit |

## Praxistipps der alten Redaktion

- "Lieber einmal abgelehnt als dreimal abgemahnt." Schon ein Unterlassungsverfahren kostet mehr als zehn Pruefdurchgaenge.
- Bei kritischen Personen: Anonymisierung pruefen (Initialen, Funktionsbeschreibung). Wenn Identifizierbarkeit zwingend fuer Aussage ist, soll Justiziariat das absegnen.
- Bei laufenden Verfahren stets pruefen, ob § 353d StGB (verbotene Mitteilung) tangiert ist.
- KI-Anteile am Beitrag separat kennzeichnen; Justiziariat braucht das fuer die Pruefung der Verantwortlichkeitskette.
- Bei Druckaufsatz: Pruefung in Setzung-Fahnenform, nicht im Word-Manuskript; im Setzungsstand sieht man Layoutfolgen.

## Mustertexte / Vorlagen

**Pruefauftrag an Justiziariat**

```
Betreff: Rechtspruefung [Werktitel] vor Imprimatur am [Datum]

Sehr geehrte/r [Name Justiziariat],

bitte pruefen Sie den anliegenden Beitrag mit Blick auf folgende Punkte:

1. Persoenlichkeitsrecht - Passage S. [n] Abs. [n] enthaelt namentliche
 Bewertung von [Name/Funktion]. Ist die Bewertung als Werturteil
 zulaessig?
2. Aeusserungsrecht / Tatsachenbehauptung - Passage S. [n] Abs. [n]
 behauptet "[konkretes Zitat]". Ist der Beleg in Fn. [n] ausreichend?
3. Bildrechte - Abbildung [n] stammt aus [Quelle], Lizenz: [Quelle/Stand].
 Bitte Rechte/Personen pruefen.
4. Wettbewerbsrecht - Tabelle S. [n] vergleicht Produkte von [Anbietern].
5. KI-Anteil - Abschnitt [Bezug] enthaelt mit [Tool] generierte Passage,
 redaktionell ueberarbeitet.

Imprimaturziel: [Datum, Uhrzeit].
Bei Rueckfragen erreichen Sie mich unter [Kontakt].

Mit freundlichen Gruessen
[Name]
```

**Freigabevermerk Justiziariat (Vorlage)**

```
Beitrag: [Werktitel]
Pruefdatum: [Datum]
Pruefer/in: [Name]
Ergebnis: [ ] Freigabe / [ ] Freigabe mit Auflagen / [ ] Aenderungsbedarf / [ ] Ablehnung
Auflagen / Aenderungen:
1. [...]
2. [...]
Gueltigkeitsdauer der Freigabe: [Datum]
Hinweis fuer Onlineversion: [...]
Unterschrift: [Name]
```

## Typische Fehler / Pitfalls

- "Bitte freigeben" ohne konkrete Pruefpunkte - Pruefung wird oberflaechlich.
- Freigabe mit Aenderung wird nicht in die Endfassung uebernommen - Haftungsfalle.
- Pruefauftrag erst zur Drucknacht - Druck der Bewertung lastet auf Justiziariat.
- Nachtraegliche Aenderungen am Beitrag nach Freigabe ohne erneute Vorlage - Freigabe entfaellt.
- Bei Onlineversion abweichende Fassung ohne separate Freigabe.

## Querverweise

- `workflow-kaltstart-und-routing` - Einordnung der Pruefdringlichkeit.
- `workflow-dokumentenintake` - Aufbereitung der Pruefunterlagen.
- `rechtecheck-urhg-verlg` - Pruefung der urheber- und verlagsrechtlichen Fragen.
- `qualitaetsgate-verlag` - Endkontrolle vor Imprimatur.
- `ai-einsatz-transparenz-datenschutz` - bei KI-Anteilen besonders relevant.
- `verl-haftungsfreistellung-autor-verlag` - vertragliche Risikoverteilung.

## Quellen Stand 06/2026

- KUG §§ 22, 23 - Recht am eigenen Bild.
- BGB §§ 823, 824, 1004 (analog) - Persoenlichkeitsrecht, Kreditgefaehrdung.
- StGB §§ 185-187, 353d - Aeusserungsdelikte, verbotene Mitteilung aus Verfahren.
- UrhG §§ 51, 51a - Zitat, Pastiche.
- UWG §§ 6, 7 - vergleichende Werbung.
- DSGVO Art. 6, 17, 85 - Datenverarbeitung, Loeschung, Medienprivileg.
- DDG § 5 - Impressumspflicht; MStV § 18 - journalistische Sorgfalt.
- BVerfG, st. Rspr. zur Abwaegung Meinungsfreiheit / Persoenlichkeitsrecht (Volltexte zur amtlichen Pruefung unter bundesverfassungsgericht.de).

## 4. `verl-abstimmung-mit-vertrieb-marketing`

**Fokus:** Briefing fuer Vertrieb und Marketing zu einem Verlagsprodukt: Zielgruppe Kernnutzen Vergleichstitel Preisarchitektur und Material fuer Katalog Webseite Veranstaltungen.

# Abstimmung mit Vertrieb / Marketing

## Worum geht es konkret

Vertrieb und Marketing brauchen vor dem Erscheinen eines Buches, eines Loseblattwerks oder einer neuen Zeitschriftenreihe ein praezises Briefing: Was traegt das Produkt? Wer kauft es? Was ist anders als Konkurrenz? Welcher Preis ist plausibel? Welche Materialien werden gebraucht (Katalog, Web, Veranstaltungs-Pitches)? Dieser Skill liefert die Schnittstelle.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn 6-9 Monate vor Erscheinen eines neuen Produkts, periodisch fuer Backlist-Pflege. Klaeren Sie:

1. Welches Produkt (Buch, Loseblattwerk, Zeitschrift, Online-Kommentar)?
2. Veroeffentlichungstermin?
3. Zielgruppe (Anwalt, Richter, Berater, Lehre, Studium)?
4. Welche Konkurrenzprodukte gibt es?

## Material- bzw. Sachrahmen

- Produkt-Konzept / Manuskriptentwurf / Inhaltsverzeichnis.
- Autoren-/Herausgeberprofil.
- Verlagshistorie zu vergleichbaren Produkten.
- Preisliste / Kostenschaetzung.
- Marketing-Briefingvorlage des Hauses.

## Praxisleitfaden / Schritt fuer Schritt

1. **Kernnutzen in einem Satz.** "Was kann der Leser nach Kauf, was er vorher nicht konnte?"
2. **Zielgruppen-Segmentierung.** Primaer (Hauptkaeufer), sekundaer (gelegentliche Kaeufer), tertiar (Empfehlungstreiber).
3. **Vergleichstitel-Analyse.** 2-4 Konkurrenzprodukte. Was machen die besser, schlechter, anders?
4. **Alleinstellungsmerkmale.** Was hat NUR dieses Produkt?
5. **Preisarchitektur.** Standardausgabe / Online-Lizenz / Kombiabo. Stichprobe Konkurrenzpreise.
6. **Marketing-Material aufbereiten:**
 - Klappentext (200-400 Z).
 - Kapitelteaser fuer Web.
 - Autoren-Kurzbiografie.
 - Probekapitel oder Leseprobe.
 - Pressetext (300-600 Z).
7. **Veranstaltungspitch.** Wenn auf Tagung / Messe: 60-Sek-Pitch.
8. **Erscheinungs-Vorschau.** Was passiert zu welchem Zeitpunkt (Vorschau, Vorab-Mailings, Erstauslieferung)?

## Trade-off-Matrix

| Pfad | A: Marketing fuehrt | B: Inhalt fuehrt | Empfehlung |
|------|--------------------|------------------|------------|
| Markterfolg | hoch | mittel | A bei breit aufgestelltem Verlag |
| Inhaltsqualitaet | gefaehrdet | hoch | B bei Fachverlag |
| Optimum | Marketing folgt Inhalt - liefert nicht den Inhalt | beide brauchen einander |

## Praxistipps der alten Redaktion

- "Ein Verlagsprodukt, das in einem Satz beschrieben werden kann, verkauft sich. Eines, das drei braucht, ist beratungsbeduerftig."
- Vergleichstitel ehrlich nennen - Marketing erkennt sonst Schwachstellen erst nach Erscheinen.
- Preisarchitektur fruh klaeren, sonst Schock beim Vertrieb.
- Pressetext / Klappentext im Verlag mit Autorin abstimmen, nicht erst vor Druck zeigen.
- Bei Online-Lizenz: Verlaengerungsmodell von Anfang an mitdenken.

## Mustertexte / Vorlagen

**Marketing-Briefing-Vorlage:**

```
Marketing-Briefing
Produkt: Mueller, "Praxiskommentar Plattformhaftung", 1. Aufl. 2027
Erscheinen: 03/2027
Zielgruppe primaer: IT-/Plattform-Rechtler, Anwaltschaft
Zielgruppe sekundaer: Compliance-Verantwortliche
Kernnutzen: Erster Praxiskommentar zur Plattformhaftung nach BGH-Linie 2026
Konkurrenz:
- [Konkurrenztitel A] - aelter, kein BGH 2026
- [Konkurrenztitel B] - akademischer, weniger praxisorientiert
Alleinstellung:
- Aktuellste BGH-Rspr.
- Praxistabellen / Schemata
- Vertragsmuster im Anhang
Preisarchitektur: Print 119 EUR / Online-Lizenz 99 EUR p.a. / Kombi 159 EUR
Erscheinungsphasen:
- Vorschau: 11/2026 Vertriebskatalog
- Vorab-Mailing Q1/2027
- Erstauslieferung 03/2027
- Buchmesse-Praesentation 10/2027
```

**Klappentext (Beispiel):**

> Die BGH-Rechtsprechung 2025/2026 hat die Plattformhaftung grundlegend neu geordnet. Mueller liefert den ersten Praxiskommentar nach dieser Wende: alle relevanten Vorschriften, mit Streitstandsdarstellung, BGH- und EuGH-Linien, Vertragsmustern und Compliance-Hilfen. Fuer Anwaltschaft, Compliance und Rechtsabteilungen.

**Anschreiben an Marketing-Verantwortliche:**

> Sehr geehrte Frau Marketing, anbei das aktualisierte Briefing zu Mueller "Praxiskommentar Plattformhaftung". Wir bitten um Aufnahme in den Vertriebskatalog 11/2026 und um Abstimmungstermin zu Klappentext, Pressetext und Vorab-Mailing-Plan. Vorgeschlagener Termin: 19.06.2026, 10:00. Bei Rueckfragen ...

## Typische Fehler / Pitfalls

- Kernnutzen unklar - Vertrieb verwendet eigene Formulierung, Autorin kommt erst nach Druck dazu.
- Vergleichstitel beschoenigt - Marktreaktion enttaeuscht.
- Preis erst nach Druck festgelegt - Kalkulation passt nicht.
- Pressetext / Klappentext ohne Autorenabstimmung.
- Erscheinungsphasen nicht synchron mit Marketing-Kalender.

## Querverweise

- `metadaten-seo-klappentext` - Klappentext, SEO.
- `marketing-presse-social` - Presse, Social Media.
- `sales-katalog-vlb-buchhandel` - Vertriebskatalog, VLB.
- `verl-buchprojekt-bauleiter` - Buchprojekt allgemein.
- `verl-abstimmung-mit-produktion-satz-druck` - Produktionsschnittstelle.

## Quellen Stand 06/2026

- Verlagsgesetz, [https://www.gesetze-im-internet.de/verlg/](https://www.gesetze-im-internet.de/verlg/).
- VLB Verzeichnis lieferbarer Buecher, [https://www.vlb.de](https://www.vlb.de).
- BoersenblattOnline, [https://www.boersenblatt.net](https://www.boersenblatt.net) (Branchenmonitor).
- UrhG fuer Marketing-Rechte (Bilder, Klappentexte).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024.
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016 (fuer Markeintegritaet).

## 5. `verl-audio-transkript-zu-fachbeitrag`

**Fokus:** Destilliert einen Audio-Vortrag oder ein freies Diktat zu einem zitierfaehigen Fachbeitrag fuer juristische Fachzeitschriften und Sammelbaende.

# Audio-Transkript zu Fachbeitrag

## Worum geht es konkret

Eine Autorin liefert nicht ein Manuskript, sondern eine Audiodatei: Mitschnitt einer Tagung, ein freies Diktat, ein Telefon-Brainstorming mit einem Co-Autor. Sie muessen daraus einen abgabefaehigen Fachbeitrag machen - ohne dass die muendliche Rohfassung im Druck als Geschwaetz wirkt.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, wenn Audio + Verschriftlichungsauftrag vorliegen. Klaeren Sie zu Beginn nur:

1. Welche Zielzeitschrift / welcher Sammelband, welche Hoechstlaenge?
2. Liegt das Transkript schon vor oder muessen Sie transkribieren?
3. Ist die Autorin mit Bearbeitung einverstanden ("Aut. Ueberarbeitung erforderlich" - Schriftform)?
4. Datenschutz: enthaelt die Aufnahme Drittstimmen, Mandantendaten, Zwischenrufe?

## Material- bzw. Sachrahmen

- Audiofile (mp3, m4a, wav).
- Vortragstitel und Termin der Aufzeichnung.
- Folien / Handout (oft die einzige strukturierende Quelle).
- Hinweise der Autorin zu Quellen, die sie muendlich nur halb genannt hat.

## Praxisleitfaden / Schritt fuer Schritt

1. **Einverstaendnis sichern.** Ohne schriftliche Freigabe keine Bearbeitung; bei Drittstimmen (Diskussion!) Anonymisierung pruefen.
2. **Transkription.** Wortgetreu in einem ersten Durchgang, Zeitstempel alle 30 Sekunden. Bei lizenziertem Whisper / Audiotrans-Tool: AVV pruefen.
3. **Sinnabschnitte bilden.** Audio ist linear, Text braucht Hierarchie. Drei bis fuenf Sinnabschnitte als Gliederungsgeruest.
4. **Mundartliches kuerzen.** "Aehs", Wiederholungen, "wie ich vorhin schon sagte" raus. Sie-Ansprache des Publikums in indirekte Rede.
5. **Quellen rekonstruieren.** Muendliche Halb-Zitate ("der Bundesgerichtshof hat ja vor ein paar Jahren entschieden") als Recherche-Auftrag an die Autorin zurueck.
6. **Schriftbild herstellen.** Gutachten- oder Urteilsstil je nach Format der Zeitschrift; Fussnotenapparat aufbauen.
7. **Autoren-Freigabe.** Erste Schriftfassung an Autorin mit kommentierten Stellen ("Originalzitat hier nicht eindeutig - bitte praezisieren") zurueckspielen.

## Trade-off-Matrix

| Pfad | A: Wortgetreues Transkript erhalten | B: Stark redigieren | Empfehlung |
|------|------------------------------------|---------------------|------------|
| Authentizitaet | hoch | mittel | A bei Interview-Format |
| Lesbarkeit | gering | hoch | B bei Fachaufsatz |
| Autoren-Stress | gering | Freigaberunde | B bei begrenzter Autorenzeit |

## Praxistipps der alten Redaktion

- "Vortraege wirken im Druck immer 30 % laenger als beim Zuhoeren. Kuerzen Sie hart."
- Schreiben Sie sich beim ersten Hoeren die Hauptthesen auf eine Seite - das ist Ihre Gliederung.
- Quellen, die im Vortrag nur halb genannt wurden, niemals selber ergaenzen, immer ruecksprechen - die Autorin haftet, nicht der Verlag.
- Wenn das Audio Zwischenrufe oder Fragen enthaelt, klaeren Sie, ob diese in den Druck sollen (dann anonymisieren) oder herausfallen.

## Mustertexte / Vorlagen

**Anschreiben an Autorin nach Transkription:**

> Sehr geehrter Herr Professor Schmitt, anbei die redaktionelle Bearbeitung Ihres Vortrags vom 14.05.2026 in Heidelberg. Wir haben das Wortprotokoll auf rund 28.000 Zeichen verdichtet (Zielmarke NJW: 25.000 bis 30.000). An vier Stellen (S. 3, 7, 9, 12) haben wir Quellen markiert, die im Vortrag nur halb genannt wurden - wir bitten um Vervollstaendigung. Bitte senden Sie uns die Freigabe bis 26.06.2026.

**Transkriptions-Logfile:**

```
Audio: Vortrag-Schmitt-Heidelberg-2026-05-14.m4a
Laenge: 47:12 min
Transkriptions-Tool: [Tool] (AVV Stand 04/2026)
Drittstimmen anonymisiert: ja (Fragen aus dem Publikum als "Frage aus dem Plenum")
Quellen-Lueckenliste:
- 04:21 "der Bundesgerichtshof hat das mal entschieden" - Az. fehlt
- 12:33 "Canaris hat dazu in der JZ geschrieben" - Jahr/Seite fehlt
- 19:08 "die ganz herrschende Meinung" - Beleg fehlt
```

## Typische Fehler / Pitfalls

- Audio ohne Einverstaendnis bearbeitet - Persoenlichkeitsrecht der Autorin und Dritter.
- Halbzitate eigenmaechtig ergaenzt - juristisch falsch oder erfunden.
- Mundartliche Wendungen woertlich uebernommen - peinlich im Druck.
- Drittstimmen aus dem Publikum unter Klarnamen veroeffentlicht.
- Audio nicht archiviert - Streitfall um den Originalton nicht mehr aufklaerbar.

## Querverweise

- `workflow-dokumentenintake` - fuer den allgemeinen Intake.
- `verl-zeitschriftenartikel-leitfaden` - fuer den Zielformat-Aufbau.
- `verl-podcast-zu-zeitschriftenbeitrag` - eng verwandt.
- `verl-konferenzmitschnitt-zu-tagungsbericht` - wenn aus dem Vortrag ein Tagungsbericht wird.
- `verl-redaktionelle-rueckmeldung-formulieren` - fuer das Rueckspielen an die Autorin.

## Quellen Stand 06/2026

- UrhG §§ 31 ff., § 51, § 63, [https://www.gesetze-im-internet.de/urhg/](https://www.gesetze-im-internet.de/urhg/).
- KUG § 22 fuer Persoenlichkeitsrecht (sinngemaess auch fuer Stimme zu beachten), [https://www.gesetze-im-internet.de/kunsturhg/](https://www.gesetze-im-internet.de/kunsturhg/).
- DSGVO Art. 6 bei personenbezogenen Daten in der Aufnahme.
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016, fuer Pinpoint-Disziplin.
- Moellers, Juristische Arbeitstechnik, 11. Aufl. 2023, zum Aufbau von Fachaufsaetzen.
