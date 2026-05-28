---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Steuerrecht Anwalt Und Berater-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Steuerrecht Anwalt Und Berater — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Steuerrecht Anwalt Und Berater**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Steuerrecht für Anwalt (anw- FAO § 9) und Steuerberater (stb-): Einspruch Klage FG Aussenprüfung Selbstanzeige. StB-Tools BWA SuSa Lohnbuchhaltung Jahresabschluss Mandantenkommunikation Software-Bedienung. DBA Europa Tuerkei Israel USA Kanada.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anw-akteneinsicht-steuerakte` | Akteneinsicht in die Steuerakte beantragen und auswerten — Einspruchsverfahren nach § 364 AO Klageverfahren nach § 78 FGO sowie ergaenzend Art. 15 DSGVO bei personenbezogenen Daten. Anwendungsfall Mandant will… |
| `anw-aussenpruefung-strategien` | Anwaltliche Begleitung einer Betriebsprüfung Aussenprüfung nach §§ 193 ff. AO. Anwendungsfall Mandant erhaelt Prüfungsanordnung § 196 AO oder Prüfung laeuft bereits. Prüfraster Umfang § 194 AO Mitwirkungspflichten §… |
| `anw-aussetzung-vollziehung` | Antrag auf Aussetzung der Vollziehung AdV stellen um Steuerzahlung bis zur Streitentscheidung auszusetzen. Anwendungsfall Mandant hat Einspruch eingelegt will aber Nachforderung nicht sofort zahlen. Zweistufig zuerst… |
| `anw-betriebsausgaben-werbungskosten-pruefraster` | Prüfraster Betriebsausgaben § 4 Abs. 4 EStG und Werbungskosten § 9 EStG abgrenzen von Kosten der privaten Lebensführung § 12 EStG. Anwendungsfall Mandant fragt ob Ausgabe steuerlich absetzbar ist Finanzamt streicht… |
| `anw-dac7-dac8-plattformen-krypto` | Beratung zu DAC7-Meldepflichten für digitale Plattformen ab 2023 PStTG und DAC8-Meldepflichten für Krypto-Dienstleister ab 2026 KryptoStG. Anwendungsfall Plattformbetreiber oder Krypto-Dienstleister fragt nach… |
| `anw-defi-lending-yield-farming-bmf-22-11-2024` | Steuerliche Behandlung von DeFi-Lending Yield Farming Liquidity Mining Staking nach BMF-Schreiben vom 22.11.2024. Anwendungsfall Mandant nutzt DeFi-Protokolle Aave Compound Curve Yearn Uniswap Lido EigenLayer und fragt… |
| `anw-einspruch-finanzamt` | Begründeten Einspruch gegen Steuerbescheid nach §§ 347 ff. AO formulieren. Anwendungsfall Mandant erhaelt Steuerbescheid und will Einspruch einlegen. Frist ein Monat ab Bekanntgabe § 355 Abs. 1 AO bzw. ein Jahr bei… |
| `anw-fristenbuch-steuerrecht` | Fristenbuch für steuerrechtliche Verfahren pflegen und Fristen berechnen. Anwendungsfall neue Bescheide oder Entscheidungen eingegangen Fristen muessen sofort eingetragen und ueberwacht werden. Standardfristen… |
| `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern` | Verteidigung gegen Haftungsbescheid nach § 69 AO wegen nicht abgeführter Lohnsteuer oder Umsatzsteuer der GmbH oder UG. Anwendungsfall Geschäftsführer erhaelt persoenlichen Haftungsbescheid des Finanzamts für… |
| `anw-grunderwerbsteuer-share-deal-90-prozent` | Grunderwerbsteuer GrEStG bei Share-Deal-Transaktionen mit grundbesitzhaltenden Gesellschaften berechnen und gestalten. Anwendungsfall M-und-A-Transaktion mit Immobilien-Hintergrund Anteilsuebertragung droht… |
| `anw-haftungswarn-15a-inso-mandant` | Anwaltliche Beratung und Warnschreiben an GmbH-Geschäftsführung bei festgestellter Insolvenzreife nach §§ 17 19 InsO. Anwendungsfall GmbH-GF spricht beim Anwalt vor weil Steuerberater Krisensignale gemeldet hat.… |
| `anw-insolvenzreife-pruefung-17-19-inso` | Anwaltliches Prüfgutachten zur Insolvenzreife einer GmbH oder UG aus Steueranwalts-Sicht. Anwendungsfall GF einer Krisengesellschaft mit Steuerrückstaenden kommt zum Anwalt und Insolvenzreife muss rechtssicher geprüft… |
| `anw-kaltstart-interview` | Kaltstart-Interview für die steuerrechtsanwaltliche Kanzlei um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation Plugin oder Konfiguration enthaelt noch Platzhalter-Marker. Erfragt Schwerpunktbereiche ESt USt… |
| `anw-klage-finanzgericht` | Klageschrift zum Finanzgericht nach §§ 40 ff. FGO entwerfen. Anwendungsfall Einspruch wurde zurückgewiesen Mandant will Klage einreichen oder Untätigkeitsklage nach sechs Monaten ohne Entscheidung. Klagefrist ein Monat… |
| `anw-mandat-triage-steuerrecht` | Strukturierte Erstabfrage und Triage bei Eingang eines steuerrechtlichen Mandats. Anwendungsfall Mandant meldet sich mit Steuerproblem Art und Dringlichkeit noch unklar. Klaert Mandantenrolle Steuerart ESt KSt GewSt… |
| `anw-minbestg-pillar2-konzernbesteuerung` | Beratung zur globalen Mindestbesteuerung Pillar Two MinBestG für Konzerne ab 750 Mio EUR Umsatz. Anwendungsfall Konzern fragt nach GloBE-Pflichten Compliance-Aufbau oder Country-by-Country Reporting ab 01.01.2024.… |
| `anw-organschaft-konzern-grundlagen` | Beratung zur ertragsteuerlichen gewerbesteuerlichen und umsatzsteuerlichen Organschaft bei Holding- oder Konzernstrukturen. Anwendungsfall Mandant plant Organschaft Holding oder prüft ob bestehende Organschaft wirksam… |
| `anw-orientierung` | Orientierungs-Skill für Anwaeltinnen und Anwaelte im Steuerrecht. Anwendungsfall Einstieg in das Plugin oder Überblick über verfuegbare Skills gewuenscht. Zentrale Gesetze AO EStG KStG UStG GewStG ErbStG GrEStG.… |
| `anw-selbstanzeige-371` | Selbstanzeige nach § 371 AO als strafbefreiende Berichtigung bei Steuerhinterziehung vorbereiten und einreichen. Anwendungsfall Mandant hat Steuern hinterzogen und will Straffreiheit erlangen bevor Entdeckung droht.… |
| `anw-steuerbescheid-analyse` | Steuerbescheid strukturiert auswerten und Angriffspunkte für Einspruch identifizieren. Anwendungsfall Mandant hat Steuerbescheid bekommen und fragt ob und wie er sich wehren kann. Bescheidarten Festsetzungsbescheid… |
| `anw-steuerstrafverteidigung-verstaendigung` | Strafverteidigung in Steuerstrafsachen nach §§ 369 ff. AO mit Ziel Einstellung oder Verständigung. Anwendungsfall Mandant ist Beschuldigter wegen Steuerhinterziehung § 370 AO oder leichtfertiger Verkuerzung § 378 AO.… |
| `anw-stundung-erlass-vollstreckungsaufschub` | Anträge auf Stundung Erlass und Vollstreckungsaufschub bei Zahlungsproblemen stellen. Anwendungsfall Mandant kann fällige Steuerschulden vorueber-gehend oder dauerhaft nicht zahlen Vollstreckung droht. Stundung… |
| `anw-tatsaechliche-verstaendigung-schlussbesprechung` | Tatsaechliche Verständigung mit dem Finanzamt und Schlussbesprechung nach § 201 AO vorbereiten und durchführen. Anwendungsfall Betriebsprüfung geht zu Ende oder Steuerstreit soll durch Einigung beigelegt werden. BFH IV… |
| `anw-umsatzsteuer-vorsteuerabzug-pruefen` | Vorsteuerabzug nach § 15 UStG prüfen und Risiken bei Umsatzsteuer-Prüfung bewerten. Anwendungsfall Finanzamt streicht Vorsteuer Mandant fragt ob Rechnung ausreicht oder Vorsteuer-Karussell-Vorwurf droht.… |
| `anw-verbindliche-auskunft` | Antrag auf verbindliche Auskunft nach § 89 Abs. 2 AO vor Verwirklichung eines steuerlich unsicheren Sachverhalts stellen. Anwendungsfall Mandant plant Umstrukturierung Holding Wegzug Schenkung Erbschaft oder… |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Steuerrechtsmandate — Mandatsannahme von der ersten Kontaktaufnahme bis zur Vollmachtserteilung. Anwendungsfall Mandant ruft erstmals an oder kommt zum Erstgespraech… |
| `schriftsatzkern-substantiierung` | Substantiierten Schriftsatzkern für steuerrechtliche Verfahren aufbauen. Anwendungsfall Einspruch Klage FG Revision BFH Stundungs- und Erlassantrag muessen begründet und mit Beweisen unterfuettert werden.… |
| `stb-addison-bwa-konfiguration-tipps` | Addison BWA-Konfiguration. Anwendungsfall Kanzleien mit Wolters Kluwer Addison statt DATEV. Methodik Unterschiede zu DATEV Konten-Konfiguration Branchenanpassung. Output BWA in Addison. |
| `stb-belegtransfer-datev-unternehmen-online` | Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard. |
| `stb-buchhaltungsbutler-mandantencloud` | BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetsprüfung AVV.… |
| `stb-bwa-aufbau-grundlagen` | Aufbau der Standard-BWA für Steuerberater erlaeutern und konfigurieren. Anwendungsfall monatliche oder quartalsweise BWA-Erstellung für GmbH oder Personenunternehmen mit SKR 03 oder SKR 04. Struktur Umsatzerlöse… |
| `stb-bwa-betriebsergebnis-deckungsbeitrag` | Ausweis Betriebsergebnis vor und nach Zinsen Deckungsbeitragsstruktur in der BWA. Anwendungsfall analytische BWA mit Stufendeckungsbeitrag EBITDA EBIT EBT Mandant aus Industrie Handel Dienstleistung. Methodik fixe und… |
| `stb-bwa-betriebsuebersicht-erstellen` | Betriebsuebersicht als ergaenzende Auswertung zur BWA. Anwendungsfall ausführliche Monats- oder Quartalsauswertung mit allen Sachkonten-Salden ergaenzend zur kompakten BWA. Methodik Konfiguration in DATEV oder Addison… |
| `stb-bwa-bewegungsbilanz-erstellen` | Bewegungsbilanz aus BWA und SuSa erstellen. Anwendungsfall Veranschaulichung Geld- und Mittelfluss zwischen zwei Stichtagen Vermögens- und Kapitalbewegung. Methodik Aktiva und Passiva Vergleich Mittelherkunft… |
| `stb-bwa-branchenvergleich-bbe-datev` | Branchenvergleich BWA auf Basis BBE-Datenbank über DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen… |
| `stb-bwa-cashflow-laienverstaendlich` | Cashflow-Darstellung für Mandant in laienverstaendlicher Form. Anwendungsfall Quartals-BWA mit vereinfachter Cashflow-Aufstellung für GF ohne Finanz-Hintergrund. Methodik einfache Mittelfluss-Tabelle… |
| `stb-bwa-erlaeuterungstext-mandant` | Erlaeuterungstext unter der BWA für den Mandanten. Anwendungsfall Monats- oder Quartals-BWA mit kurzem fachlichem Begleittext der die wesentlichen Abweichungen und Risiken benennt. Aufbau Sachverhalt Erlaeuterung… |
| `stb-bwa-fehlerquellen-haeufig` | Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetsprüfung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste… |
| `stb-bwa-jahres-bwa-erstellen` | Jahres-BWA als Ergaenzung zum Jahresabschluss. Anwendungsfall Jahresabschluss-Begleitung mit BWA für das Gesamtjahr inkl Vorjahresvergleich Mehrjahrestrend und Mandantenpraesentation. Methodik kumulierte BWA mit… |
| `stb-bwa-kapitalflussrechnung-iduk` | Kapitalflussrechnung nach indirekter Methode aus BWA und Bilanz. Anwendungsfall Jahresabschluss Bankreporting Sanierungskonzept Konzernabschluss. Methodik DRS 21 indirekte Ableitung aus Jahresueberschuss Mittelfluss… |
| `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` | Rentabilitaetskennzahlen Eigenkapitalrendite Gesamtkapitalrendite ROI Umsatzrentabilitaet. Anwendungsfall Quartals- oder Jahresauswertung Beratungsgespraech Investor-Update. Methodik Berechnung Bewertung… |
| `stb-bwa-kontenrahmen-skr03-skr04` | Vergleich Kontenrahmen SKR 03 versus SKR 04 für BWA-Erstellung. Anwendungsfall Mandantenneuaufnahme oder Wechsel des Kontenrahmens Entscheidungsgrundlage Industrie Handel Dienstleistung. Aufbau Bilanz vs Prozess… |
| `stb-bwa-mandantengespraech-uebergabe` | BWA-Übergabegespraech mit dem Mandanten. Anwendungsfall persoenliche oder telefonische Besprechung der monatlichen oder quartalsweisen BWA mit dem GF Klaerung der Abweichungen Steuerungsempfehlungen Risikoeskalation.… |
| `stb-bwa-mandantenreport-monatlich` | Monatlicher Mandantenreport zusammenführend aus BWA SuSa OPOS Lohn Liquiditaet. Anwendungsfall standardisierter Monatsreport an Mandant per Mail oder Portal. Methodik 4-Seiten-Vorlage Cover BWA Kennzahlen Empfehlung.… |
| `stb-bwa-monatsabschluss-routine` | Routine für den Monatsabschluss in der Steuerberater-Kanzlei. Anwendungsfall monatliche BWA-Erstellung in einem standardisierten 30-Tage-Zyklus mit Belegabgabe Buchung Abstimmung BWA-Versand. Schritte Belegannahme… |
| `stb-bwa-soll-ist-vergleich` | Soll-Ist-Vergleich in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Plan-Werten aus Wirtschaftsplan Unternehmensplanung Forecast. Methodik Planeingabe Abweichungsanalyse Steuerungsempfehlung. Output BWA mit… |
| `stb-bwa-statische-liquiditaet-kennzahlen` | Statische Liquiditaetskennzahlen Liquiditaet 1 2 3 Grades aus BWA und Bilanz. Anwendungsfall Quartalsauswertung Bankreporting Krisenfrueherkennung. Methodik Working Capital Aufstellung Anlagendeckung Kennzahlen. Output… |
| `stb-bwa-sus-bilanz-pruefung` | BWA SuSa Summen- und Saldenliste und Bilanzentwurf einer GmbH oder UG auf insolvenzrechtliche Krisensignale prüfen. Anwendungsfall Steuerberater erstellt Jahresabschluss BWA-Review oder Krisenfrueherkennung und muss… |
| `stb-bwa-vorlaeufiges-ergebnis-darstellung` | Darstellung vorlaeufiges Ergebnis in Quartals- und Halbjahres-BWA. Anwendungsfall unterjaehrige BWA mit Vorlaeufigkeitsvermerk Bestand-Schaetzung noch nicht abgeschlossene Periodenabgrenzung. Methodik klare Trennung… |
| `stb-bwa-zeitlicher-vergleich-jahresvergleich` | Zeitvergleich Vorjahr und Vormonat in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Gegenüberstellung Vorjahres-Periode kumulierter Jahresvergleich Abweichungs-Analyse Trendaussage. Methodik gleicher Zeitraum… |
| `stb-bwa-zeitvergleich-vorjahr-darstellung` | Zeitvergleich Vorjahr in der BWA grafisch und tabellarisch. Anwendungsfall optische Aufbereitung der Vorjahresvergleichsdaten für Mandantengespraech mit Liniendiagrammen Balkengrafik. Methodik Standard-Tabelle plus… |
| `stb-datentransfer-mandant-cloud-dsgvo` | Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Prüfung der DSGVO-Konformität beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Massnahmen Drittlandtransfer. Methodik… |
| `stb-datev-bwa-modul-bedienen-tipps` | DATEV Kanzlei-Rechnungswesen BWA-Modul Bedienung. Anwendungsfall Erstellung BWA in DATEV Auswahl Form Konfiguration Periodenvergleich Branchenvergleich. Methodik Workflow-Tipps. Output BWA-konfiguriert. |
| `stb-datev-lohn-modul-lodas-luh` | DATEV LODAS und Lohn und Gehalt LUG. Anwendungsfall Lohnabrechnung in DATEV-Welt Konfiguration ELSTER ELStAM sv.net Schnittstellen. Methodik Unterschiede LODAS vs Lohn und Gehalt Praxis-Tipps. Output Lohnprogramm… |
| `stb-dba-ansaessigkeit-tie-breaker-rules` | Ansaessigkeit nach Art. 4 OECD-Musterabkommen und Tie-Breaker-Regelungen bei mehrfacher Ansaessigkeit. Anwendungsfall natuerliche Person mit Wohnsitz in mehreren Staaten oder Kapitalgesellschaft mit Sitz und… |
| `stb-dba-belgien` | DBA Deutschland Belgien aktuelle Fassung. Anwendungsfall Eupen Malmedy Grenzgaenger Pendler Beteiligungen Lizenzen. Anwendungsbereich Sprachgrenze. Loehne mit 183-Tage-Regelung. Pensionen mit Spezialregelung. Output… |
| `stb-dba-betriebsstaette-art-5-musterabkommen` | Betriebsstaette nach Art. 5 OECD-Musterabkommen einschließlich BEPS- und MLI-Anpassungen. Anwendungsfall Steuerberater prüfen ob auslaendische Aktivitaet eines deutschen Unternehmens oder umgekehrt eine Betriebsstaette… |
| `stb-dba-bulgarien` | DBA Deutschland Bulgarien 2010. Anwendungsfall Outsourcing IT Pflege Holding Beteiligungen. EU-MTRL ergaenzend. Niedrige KSt 10 Prozent. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel… |
| `stb-dba-daenemark` | DBA Deutschland Daenemark aktuelle Fassung. Anwendungsfall Pendler Schleswig-Holstein Daenemark Beteiligungen Pensionen Sozialversicherung Lizenzen. Methodenartikel Freistellung mit Anrechnungswahl. Sonderregelungen… |
| `stb-dba-dividenden-quellensteuer-art-10` | Dividenden nach Art. 10 OECD-MA und EU-Mutter-Tochter-Richtlinie. Anwendungsfall Ausschuettungen über Grenze Quellensteuer im Quellenstaat Hoechstsatz Schachtelhoehe. § 43b EStG MTRL § 8b KStG Schachtelprivileg.… |
| `stb-dba-estland` | DBA Deutschland Estland 1996. Anwendungsfall IT-Branche E-Residency Holding Beteiligungen. EU-MTRL ergaenzend. Besonderheit estnisches Steuersystem mit Besteuerung nur bei Ausschuettung. Output Mandanten-Memo… |
| `stb-dba-finnland` | DBA Deutschland Finnland 2016. Anwendungsfall Maschinenbau IT Telekommunikation Pensionen Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-frankreich-1959` | DBA Deutschland Frankreich aus 1959 mit Aenderungsprotokollen. Anwendungsfall Pendler im Elsass und Lothringen Grenzgaengerregelung 20-km-Zone. Beteiligungen Pensionen Lizenzen. Aelteres DBA mit Sonderkonstruktionen… |
| `stb-dba-grenzgaenger-frankreich-vor-allem-elsass` | Grenzgaengerregelung DBA Frankreich mit Schwerpunkt Elsass-Lothringen und 20-km-Zone. Anwendungsfall Arbeitnehmer Wohnsitz und Tätigkeit in Grenzgemeinde. Arbeitstaegliche Rückkehr 45-Tage-Schaedlichkeit. Beweismittel… |
| `stb-dba-grenzgaenger-oesterreich-rueckkehr` | Grenzgaengerregelung DBA Oesterreich mit Wohnsitz in der Grenznaehe und arbeitstaeglicher Rückkehr. Anwendungsfall Arbeitnehmer Wohnsitz Bayern oder Salzburg/Tirol Tätigkeit auf der anderen Seite.… |
| `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` | Grenzgaengerregelung DBA Schweiz Art. 15a mit 60-Tage-Schaedlichkeit. Anwendungsfall Arbeitnehmer Wohnsitz Suedbaden Baden-Wuerttemberg Bayern Tätigkeit Schweiz. Arbeitstaegliche Rückkehr maximal 60 Nicht-Rückkehrtage… |
| `stb-dba-griechenland` | DBA Deutschland Griechenland 1966. Anwendungsfall Schifffahrt Tourismus Pensionen Beteiligungen. EU-MTRL ergaenzend. Aelteres DBA. Methodenartikel Anrechnung Sonderregelungen. Output Mandanten-Memo Berechnungsbeispiel… |
| `stb-dba-grossbritannien-2010` | DBA Deutschland Vereinigtes Koenigreich 2010 mit Protokollen 2014 und 2021. Anwendungsfall Brexit-Folgen Holding-Strukturen City-Branchen Pensionen Finanzdienstleistungen. Keine EU-Richtlinien nach Brexit.… |
| `stb-dba-grundprinzip-oecd-musterabkommen` | Grundprinzipien des OECD-Musterabkommens 2017 inkl. BEPS-Anpassungen und MLI für die Prüfung deutscher Doppelbesteuerungsabkommen. Anwendungsfall Steuerberater oder Steueranwalt arbeitet einen DBA-Sachverhalt vom… |
| `stb-dba-home-office-pandemie-folgeregelung` | Konsultations-Vereinbarungen zu Home-Office wahrend und nach Pandemie. Anwendungsfall Grenzüberschreitender Arbeitnehmer mit Home-Office-Tagen. Konkrete Vereinbarungen DE-Schweiz DE-Oesterreich DE-Luxemburg… |
| `stb-dba-irland` | DBA Deutschland Irland 2011. Anwendungsfall IT- und Pharma-Holdings (Apple Google Pfizer), Holding-Strukturen, Lizenzeinkuenfte. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung. Output… |
| `stb-dba-island` | DBA Deutschland Island. Anwendungsfall Fischerei Geothermie Tourismus Pensionen Beteiligungen. EWR-Status keine MTRL. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-israel-2014` | DBA Deutschland Israel Neufassung 2014 in Kraft 21.5.2016. Anwendungsfall Hightech IT Software-Lizenzen Holdings Pensionen Aliyah-Konstellation. Methodenartikel Anrechnung. MLI relevant. Output Mandanten-Memo… |
| `stb-dba-italien` | DBA Deutschland Italien aus 1989. Anwendungsfall Mittelstand Maschinenbau Mode Pharma Holding Pensionen Wegzug Suedtirol. EU-MTRL Subject-to-Tax-Klauseln. Methodenartikel Freistellung mit Aktivitaetsklausel. Output… |
| `stb-dba-kanada-2001` | DBA Deutschland Kanada 2001. Anwendungsfall RRSP RRIF Pensionen Beteiligungen Branch Profits Tax. Auswanderung Quebec. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-kroatien` | DBA Deutschland Kroatien 2006. Anwendungsfall Tourismus Mittelstand Beteiligungen. EU-MTRL seit 2013. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-kuenstler-sportler-art-17-ma` | Kuenstler und Sportler nach Art. 17 OECD-MA mit Auftrittsstaat-Besteuerung. Anwendungsfall Musiker Schauspieler Sportler mit Auftritten in mehreren Staaten. Quellensteuer und BZSt-Anträge Anti-Treaty-Shopping nach §… |
| `stb-dba-lettland` | DBA Deutschland Lettland 1997. Anwendungsfall Mittelstand IT Holding Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-litauen` | DBA Deutschland Litauen 1997. Anwendungsfall Mittelstand Logistik Holding Beteiligungen Fintech. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-lizenzgebuehren-art-12-bzst` | Lizenzgebühren nach Art. 12 OECD-MA und EU-Zins-Lizenzgebühren-Richtlinie. Anwendungsfall Software-Lizenz Patent Marken IP-Box-Konstruktionen. § 50g EStG ZinsLizenzRL § 50a EStG Steuerabzug § 50c EStG BZSt-Entlastung.… |
| `stb-dba-luxemburg-2012` | DBA Deutschland Luxemburg aktuelle Fassung 2012 mit Aenderungsprotokollen. Anwendungsfall Holding-Konstruktionen Soparfi Fondsstrukturen grenzüberschreitende Arbeitsverhältnisse mit hoher Pendlerzahl. Substanz… |
| `stb-dba-malta-2001` | DBA Deutschland Malta 2001 mit Protokollen. Anwendungsfall Holding REIT-Strukturen Schifffahrt Online-Glueckspiel. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung Aktivitaetsklausel.… |
| `stb-dba-methodenartikel-anrechnung-vs-freistellung` | Methodenartikel Art. 23A und Art. 23B OECD-Musterabkommen und Wahl zwischen Anrechnung und Freistellung mit Progressionsvorbehalt. Anwendungsfall Steuerberater entscheidet zwischen Anrechnungsmethode mit § 34c EStG und… |
| `stb-dba-niederlande-2012` | DBA Deutschland Niederlande aktuelle Fassung 2012 in Kraft seit 2016. Anwendungsfall grenzüberschreitende Arbeitsverhältnisse Pensionen Beteiligungen Logistikbetriebsstaetten. Aktive Einkuenfte Freistellung mit… |
| `stb-dba-norwegen` | DBA Deutschland Norwegen. Anwendungsfall Oel und Gas Offshore Schifffahrt Mittelstand Pensionen Beteiligungen. EWR-Status keine MTRL. Methodenartikel Freistellung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-oesterreich` | DBA Deutschland Oesterreich aktuelle Fassung mit Protokollen. Anwendungsfall grenzüberschreitende Beschaeftigung Grenzgaenger Pensionen Beteiligungen Lizenzen Bauausführung. Grenzgaengerregelung… |
| `stb-dba-polen` | DBA Deutschland Polen aktuelle Fassung 2003. Anwendungsfall Arbeitnehmer Entsendung Pendler Beteiligungen Lizenzen Bauausführung. EU-MTRL EU-ZinsLizenzRL ergaenzend. Methodenartikel Anrechnungsmethode mit… |
| `stb-dba-portugal` | DBA Deutschland Portugal. Anwendungsfall Pensionen Algarve NHR-Status Beteiligungen Lizenzen Immobilien. EU-MTRL Madeira-Sondersteuergebiet. Methodenartikel Anrechnung mit Sonderregelungen. Output Mandanten-Memo… |
| `stb-dba-quellensteuer-erstattung-bzst-50c-estg` | Quellensteuerentlastung nach § 50c EStG beim Bundeszentralamt für Steuern BZSt. Anwendungsfall auslaendischer Empfaenger deutscher Kapitalertraege Lizenzen oder Verguetungen will deutsche Quellensteuer ermäßigen oder… |
| `stb-dba-rentner-pensionen-art-18` | Rentenbesteuerung nach Art. 18 OECD-MA und Sonderregelungen einzelner DBA. Anwendungsfall Rentner mit Wohnsitz im Ausland (Spanien Portugal Italien Tuerkei Schweiz Oesterreich) oder auslaendische Rente bei Wohnsitz… |
| `stb-dba-rumaenien` | DBA Deutschland Rumaenien 2001. Anwendungsfall Automotive-Produktion IT Pflege Holding Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-russland-suspendierung-2024` | DBA Deutschland Russland Suspendierung wesentlicher Verguenstigungen. Russische Verbalnote vom 08.08.2023 suspendiert von russischer Seite Art. 5 bis 22 und 24. Deutsche Gegenmassnahme nach § 1 Abs. 3 Satz 2 StAbwG mit… |
| `stb-dba-schweden` | DBA Deutschland Schweden 1992. Anwendungsfall Mittelstand Maschinenbau Pendler Pensionen Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Freistellung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-schweiz` | DBA Deutschland Schweiz mit Schwerpunkt 60-Tage-Grenzgaengerregelung Art. 15a. Anwendungsfall Pendler Suedbaden Bodensee Zuerich Pauschalbesteuerung Wegzug Wegzugsbesteuerung Beteiligungen Lizenzen. Anrechnungsmethode… |
| `stb-dba-serbien-montenegro` | Nachfolge-DBA Jugoslawien für Serbien und Montenegro. Anwendungsfall Mittelstand Diaspora Pensionen Bauausführung Beteiligungen. Aelteres DBA mit roemischen Artikelnummern. Methodenartikel Anrechnung. Output… |
| `stb-dba-slowakei` | DBA Deutschland Slowakei aus 1980 fortgeltend gegenüber Nachfolgestaat. Anwendungsfall Automotive Zulieferung Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo… |
| `stb-dba-slowenien` | DBA Deutschland Slowenien 2006. Anwendungsfall Mittelstand Automotive Tourismus Beteiligungen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-spanien-2011` | DBA Deutschland Spanien Neufassung 2011 in Kraft seit 2012. Anwendungsfall Mittelstand Immobilien Mallorca-Konstellation Pensionen Beteiligungen. EU-MTRL Subject-to-Tax-Klausel. Methodenartikel Anrechnung. Output… |
| `stb-dba-tschechien` | DBA Deutschland Tschechien aus 1980 fortgeltend gegenüber Nachfolgestaat. Anwendungsfall grenzüberschreitende Arbeitsverhältnisse Bauausführung Beteiligungen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung.… |
| `stb-dba-tuerkei-2011` | DBA Deutschland Tuerkei Neufassung 2011 in Kraft seit 1.8.2012 anwendbar ab 2012. Anwendungsfall Familienbande Deutschland-Tuerkei Arbeitseinkuenfte Pensionen Beteiligungen Bauausführung in der Tuerkei Holding.… |
| `stb-dba-ukraine` | DBA Deutschland Ukraine. Anwendungsfall Mittelstand IT Pflege Holding Beteiligungen mit Konfliktrelevanz seit 2022. Sanktionen Devisenkontrollen Überweisungssperren. Methodenartikel Anrechnung. Output Mandanten-Memo… |
| `stb-dba-ungarn` | DBA Deutschland Ungarn 2011. Anwendungsfall Automotive-Zulieferer Holding Beteiligungen Pensionen Lizenzen. EU-MTRL ergaenzend. Methodenartikel Anrechnung. Output Mandanten-Memo Berechnungsbeispiel BZSt-Hinweise. |
| `stb-dba-usa-1989-protokoll-2006` | DBA Deutschland USA 1989 mit Protokollen 1998 2006 2021. LOB-Klausel Limitation on Benefits Substanztest. Pension Protection im Protokoll 2006. Branch Profits Tax. Anwendungsfall US-Holdings IRA 401(k) Roth… |
| `stb-dba-zypern-2011` | DBA Deutschland Zypern 2011. Anwendungsfall Holding-Konstruktionen Schifffahrt Beteiligungen Investmentfonds. EU-MTRL ergaenzend. Substanz Anti-Treaty-Shopping. Methodenartikel Anrechnung. Output Mandanten-Memo… |
| `stb-drv-sozialversicherungspruefung` | Steuerberater-Begleitung der DRV-Sozialversicherungsprüfung nach § 28p SGB IV. Anwendungsfall Mandant-GmbH erhaelt DRV-Prüfankündigung oder Prüfung laeuft bereits. Prüfungsschwerpunkte Statusfeststellung GF… |
| `stb-eau-elektronische-arbeitsunfaehigkeit-2023` | eAU elektronische Arbeitsunfähigkeitsbescheinigung seit 2023. Anwendungsfall AN-Krankmeldung AG-Abruf bei Krankenkasse Entgeltfortzahlung. Methodik Schnittstelle Konfiguration Workflow. Output eAU-Konfiguration. |
| `stb-erechnung-pflicht-b2b-2025-2026` | eRechnung-Pflicht B2B seit 01.01.2025 § 14 UStG ViDA. Anwendungsfall Prüfung Mandantenbetrieb eRechnungs-Empfang Versand Übergangsfristen PDF reicht nicht mehr. Methodik Format XRechnung ZUGFeRD. Output… |
| `stb-jahresabschluss-abgrenzungen-rap-rai` | Rechnungsabgrenzungsposten RAP aktiv und passiv. Anwendungsfall Jahresabschluss-Buchung Versicherung Miete Kfz-Steuer Vorauszahlungen periodengerechte Zuordnung. Methodik Identifikation Berechnung Buchung. Output… |
| `stb-jahresabschluss-anlagenverzeichnis-afa` | Anlagenverzeichnis und AfA-Buchung Jahresabschluss. Anwendungsfall vollständige Aktualisierung Anlagen Zugaenge Abgaenge AfA-Methoden Sonderabschreibung 7g 7b 6b EStG. Methodik AfA-Tabellen. Output Anlagenspiegel. |
| `stb-jahresabschluss-bestandskonten-abstimmung` | Bestandskonten-Abstimmung zum Jahresabschluss. Anwendungsfall Endbestaende Bank Kasse Forderungen Verbindlichkeiten Anlagen Eigenkapital abstimmen Inventur-Werte einarbeiten. Methodik Saldenabstimmung Vergleich. Output… |
| `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` | E-Bilanz § 5b EStG elektronische Übermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Übermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt. |
| `stb-jahresabschluss-handels-vs-steuerbilanz` | Handelsbilanz vs Steuerbilanz Massgeblichkeit § 5 EStG. Anwendungsfall Prüfung Abweichungen Handels- und Steuerbilanz Massgeblichkeitsprinzip umgekehrte Massgeblichkeit Wahlrechte. Methodik Differenz-Tabelle… |
| `stb-jahresabschluss-kassenfuehrung-gobd-pflichten` | Kassenführung GoBD-Pflichten. Anwendungsfall Mandanten mit Bargeschäft Kasse Aufzeichnungspflichten Kassenbuch elektronische Aufzeichnungssysteme TSE technische Sicherheitseinrichtung. Methodik Prüfung Sorgfalt. Output… |
| `stb-jahresabschluss-rueckstellungen-bewertung` | Rückstellungen Bewertung § 249 HGB. Anwendungsfall Jahresabschluss Bildung Rückstellungen Garantie drohende Verluste Tantieme Urlaub Steuern Prozesskosten. Methodik Prüfung Anlass Quantifizierung Auflösung. Output… |
| `stb-jahresabschluss-veroeffentlichung-bundesanzeiger` | Jahresabschluss-Veröffentlichung Bundesanzeiger § 325 HGB. Anwendungsfall Pflichtveröffentlichung Kapitalgesellschaft Frist 12 Monate Groessenklassen Erleichterungen. Methodik elektronische Übermittlung. Output… |
| `stb-jahresabschluss-vorbereitung-stichtag` | Jahresabschluss-Vorbereitung Stichtag. Anwendungsfall systematische JA-Vorbereitung Inventur Periodenabgrenzung Rückstellungen Anlagenspiegel. Methodik 8-Wochen-Vorlauf. Output JA-Vorbereitungs-Routine. |
| `stb-jahresabschluss-warenbestand-inventur` | Warenbestand und Inventur für Jahresabschluss. Anwendungsfall jaehrliche Inventur Aufnahme Warenbestand permanente Inventur Stichprobeninventur Bewertung. Methodik § 240 HGB GoBD. Output Inventur-Protokoll… |
| `stb-jahresgespraech-mandant-bwa-basis` | Jahresgespraech Mandant auf BWA-Basis. Anwendungsfall jaehrliches Bilanzgespraech nach Jahresabschluss-Erstellung Gesamtjahresblick Mehrjahres-Trend Strategie Folgejahr. Methodik intensive Vorbereitung 2-3 Stunden… |
| `stb-kaltstart-interview` | Kaltstart-Interview für das Steuerberater-Plugin um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation oder Konfiguration enthaelt noch Platzhalter-Marker oder Re-Interview mit --redo oder Konnektoren-Prüfung… |
| `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht` | KI-Tools im StB-Betrieb Berufsrechtliche Grenzen § 57 StBerG. Anwendungsfall ChatGPT Claude Microsoft Copilot Datev-KI Nutzung Mandantenkommunikation Berufsverschwiegenheit. Methodik Prüfung Compliance KI-VO… |
| `stb-liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau 3-6-12 Monate für GmbH oder UG erstellen mit insolvenzrechtlicher Fortbestehensprognose. Anwendungsfall Steuerberater begleitet Krisenmandat und benoetigt strukturierte Zahlungsplanung… |
| `stb-liquiditaetsvorschau-3wochen` | Kurzfristige Drei-Wochen-Liquiditaetsvorschau für GmbH oder UG zur wochentlichen Krisenfrueherkennung. Anwendungsfall Steuerberater will schnell prüfen ob Zahlungsunfähigkeit nach § 17 InsO droht oder schon vorliegt.… |
| `stb-lohn-abfindungen-besteuerung-funftel-regel` | Abfindungen Besteuerung Fuenftel-Regelung § 34 EStG. Anwendungsfall Aufhebungsvertrag Kündigung mit Abfindung Prüfung Voraussetzungen Fuenftel-Regel Berechnung Vorteilsvergleich. Methodik Berechnung mit DATEV LODAS.… |
| `stb-lohn-arbeitgeber-arbeitnehmer-anteile` | Arbeitgeber- und Arbeitnehmer-Anteile in der SV. Anwendungsfall Verteilung der SV-Beitraege zwischen AG und AN PV-Zuschlag Kinderlose KV-Zusatzbeitrag Sonderbeitraege Lohnabrechnung. Methodik AG-AN-Aufteilung in DATEV… |
| `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` | Arbeitsvertrag aus lohnrelevanter Sicht prüfen. Anwendungsfall Onboarding neuer AN Vertragsaenderungen Stundenlohn Festgehalt Sonderverguetungen Sachbezuege Dienstwagen JobRad bAV Vermögenswirksame Leistungen. Methodik… |
| `stb-lohn-aufzeichnungspflichten-milog` | Aufzeichnungspflichten nach MiLoG § 17 für Mindestlohn-relevante Branchen Geringfuegige Beschaeftigung. Anwendungsfall Prüfung Aufzeichnungspflicht 2 Jahre Aufbewahrung Schwarzarbeitsbekaempfung. Methodik Form der… |
| `stb-lohn-ausgleichszahlungen-altersteilzeit` | Altersteilzeit Block-Modell Gleichverteilungsmodell Aufstockungsbetrag. Anwendungsfall AN-Antrag Altersteilzeit ab 55 Block-/Gleichverteilungs-Variante AG-Aufstockung 20 Prozent steuerfrei. Methodik Prüfung AltTZG… |
| `stb-lohn-bav-doppelversorgung-foerderung` | bAV bei mehreren Durchführungswegen Doppelversorgung Foerderung. Anwendungsfall AN hat Direktversicherung und Pensionskasse Beitragsobergrenzen gemeinsame Prüfung Hoechstforderung. Methodik kumulierte… |
| `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` | Berufsgenossenschaft Lohnnachweis Jahresende. Anwendungsfall jaehrlicher Lohnnachweis an die zuständige BG Vorauszahlung BG-Beitrag Schluesseldaten Gefahrtarif. Methodik elektronischer Lohnnachweis über sv.net oder… |
| `stb-lohn-betriebliche-altersversorgung-grundlagen` | Betriebliche Altersversorgung bAV Grundlagen Durchführungswege. Anwendungsfall Beratung Mandant zu bAV Direktversicherung Pensionskasse Pensionsfonds Direktzusage Unterstuetzungskasse steuerliche und SV-rechtliche… |
| `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro` | Aufmerksamkeiten 60 EUR-Freigrenze pro persoenlichem Anlass. Anwendungsfall Sachgeschenk zu Geburtstag Hochzeit Jubilaeum 60 EUR Hoechstwert LSt-frei. Methodik Abgrenzung zur 50 EUR-Sachbezugs-Freigrenze. Output… |
| `stb-lohn-betriebsveranstaltung-110-euro-freibetrag` | Betriebsveranstaltung 110 EUR-Freibetrag § 19 Abs 1 Nr 1a EStG. Anwendungsfall Firmenfeier Sommerfest Weihnachtsfeier Kostenkalkulation 110 EUR pro AN Pauschalierung. Methodik Berechnung Prüfung Belege. Output… |
| `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` | Dienstwagen 1-Prozent-Methode oder Fahrtenbuch. Anwendungsfall geldwerter Vorteil Privatnutzung Dienstwagen E-Auto Hybrid Listenpreis Brutto-Methode. Methodik Prüfung Methode Vergleich Steuerklasse. Output… |
| `stb-lohn-direktversicherung-3-nr-63-estg` | Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik… |
| `stb-lohn-elternzeit-mutterschutz` | Elternzeit Mutterschutz Mutterschaftsgeld Elterngeld lohnrelevant. Anwendungsfall AN-Schwangerschaft Geburt Antrag Mutterschutz Elternzeit Auswirkung auf Lohn SV-Status Steuerprogression. Methodik Prüfung MuschG… |
| `stb-lohn-firmenrad-leasing-jobrad` | JobRad Dienstrad Leasingmodell steuerliche Behandlung. Anwendungsfall AG-Leasing eines Fahrrads oder E-Bikes Überlassung an AN durch Gehaltsumwandlung Sachbezug von einem Viertel Prozent. Methodik Prüfung Konfiguration… |
| `stb-lohn-gesellschafter-geschaeftsfuehrer-sv` | Gesellschafter-Geschäftsführer GGF SV-Pflicht oder SV-Befreiung. Anwendungsfall Prüfung GGF einer GmbH ob abhaengig beschaeftigt oder selbständig tätig Statusfeststellung. Methodik Kriterienkatalog Beteiligung… |
| `stb-lohn-jahresmeldungen-ahn-asn-besondere` | Jahresmeldungen DEUEV Jahreslohnsumme Abmelde- und Sondermeldungen. Anwendungsfall Jahresende-Meldungen 15. Februar Folgejahr AN-Jahresarbeitsentgelt-Meldung Sondermeldungen Lohnsteuerbescheinigung. Methodik… |
| `stb-lohn-jobticket-mobilitaet-deutschlandticket` | Jobticket Deutschlandticket steuerliche Behandlung. Anwendungsfall AG erstattet AN Mobilitaetsticket OePNV oder bietet Jobticket steuerfrei nach § 3 Nr 15 EStG Auswirkung auf Entfernungspauschale. Methodik Prüfung… |
| `stb-lohn-krankheit-entgeltfortzahlung-efzg` | Krankheit Entgeltfortzahlung 6 Wochen § 3 EFZG eAU. Anwendungsfall Lohnabrechnung bei Krankheit Entgeltfortzahlung 6 Wochen U1-Umlage Krankengeld Krankenkasse-Erstattung elektronische Arbeitsunfähigkeit. Methodik… |
| `stb-lohn-kurzarbeit-kug-progression` | Kurzarbeitergeld KUG Anmeldung Berechnung Progressionsvorbehalt. Anwendungsfall Kurzarbeit-Antrag bei der Bundesagentur Lohnabrechnung mit anteiligem Lohn und KUG Steuerprogressionsvorbehalt für AN. Methodik Prüfung… |
| `stb-lohn-lohnsteuer-anmeldung-elster` | Elektronische Lohnsteuer-Anmeldung über ELSTER. Anwendungsfall monatliche oder vierteljaehrliche LSt-Anmeldung KiSt SolZ Pauschalierung Anmeldungs-Schema technische Übermittlung. Methodik Daten aus Lohnabrechnung… |
| `stb-lohn-lohnsteuer-monatsabschluss` | Monatlicher Lohnsteuer-Monatsabschluss. Anwendungsfall regulaere Lohnabrechnung Bruttolohn LSt KiSt SolZ pauschalierte Loehne SV-Abrechnung Auszahlung Anmeldung. Methodik Standard-Workflow Abrechnungsschritte 39e… |
| `stb-lohn-mandantenaufnahme-onboarding` | Onboarding eines neuen Lohn-Mandanten. Anwendungsfall Erstaufnahme Stammdaten Arbeitnehmer-Liste Sozialversicherungs-Anmeldung Mandantenstamm DATEV LODAS oder Lohn und Gehalt. Methodik Checkliste Datenerfassung… |
| `stb-lohn-mehrarbeit-zuschlaege-39b-estg` | Sonn- Feiertag- und Nachtarbeitszuschlaege § 3b EStG. Anwendungsfall Lohnabrechnung mit Schichtzuschlaegen Gastronomie Pflege Sicherheitsdienst LSt-Freiheit SV-Freiheit in Grenzen. Methodik Prüfung Begrenzung Grundlohn… |
| `stb-lohn-meldungen-sv-elstam-zugang` | SV-Meldungen und ELStAM-Verfahren beim AN-Onboarding. Anwendungsfall Beschaeftigungsbeginn und Beendigung Anmeldung Abmeldung Aenderungsmeldung Sofortmeldung Sonderbranchen Elektronische LSt-Merkmale Abruf. Methodik… |
| `stb-lohn-midi-job-uebergangsbereich-2000-euro` | Midi-Job-Übergangsbereich 538 EUR/01 bis 2000 EUR Stand 2023. Anwendungsfall geminderte AN-SV-Beitraege in der Gleitzone Berechnung Faktor F Anpassung 2026. Methodik Berechnungsmodul SV-Beitrag AN Gleitzone. Output… |
| `stb-lohn-mindestlohn-aktuell-2026-anpassung` | Aktueller Mindestlohn 2026 Anpassung. Anwendungsfall Prüfung des aktuellen MiLo-Wertes Auswirkung auf Mini- Midi-Job-Grenzen Vertragsklauseln Mandanten-Information. Methodik Verifikation amtliche Quellen… |
| `stb-lohn-mini-midi-grenzen-2026-stand` | Aktuelle Mini- und Midi-Job-Grenzen 2026. Anwendungsfall Prüfung aktueller Schwellenwerte für Geringfuegigkeit und Übergangsbereich Verifikation gegen Mindestlohn-Anpassungen. Methodik Werteprüfung Quellen amtliche… |
| `stb-lohn-minijob-538-euro-2024-anpassung` | Minijob 538 EUR-Grenze dynamisch an Mindestlohn gekoppelt seit 1.10.2022. Anwendungsfall geringfuegige Beschaeftigung pauschale Abgaben Beitragsbefreiung Steuerklassen-Frage Mehrfachbeschaeftigung. Methodik Prüfung 538… |
| `stb-lohn-monatsende-meldepflichten-checkliste` | Lohn-Meldepflichten zum Monatsende Checkliste LSt-Anmeldung SV-Beitragsnachweis DEUEV BG-Lohnnachweis. Anwendungsfall standardisierter Prüfablauf vor Monatsende und Fristen Auswertung. Methodik Prüfliste… |
| `stb-lohn-praktikanten-azubis-loehne` | Praktikanten und Azubis lohnrelevante Sonderregeln. Anwendungsfall Pflichtpraktikum freiwilliges Praktikum Berufsausbildung BBiG Berufsausbildungsbeihilfe SV-Behandlung Vergueteung. Methodik Unterscheidung Pflicht- vs… |
| `stb-lohn-pruefungen-drv-bp-haftung-stb` | Prüfungen DRV-Prüfung Lohnsteuer-Aussenprüfung Steuerberater-Haftung. Anwendungsfall DRV-Prüfer kommt Prüfkriterien Nachforderung Haftungsrisiken Mandant. Methodik Vorbereitung Begleitung Reaktion. Output Prüfbericht… |
| `stb-lohn-sachbezuege-50-euro-freigrenze` | Sachbezuege 50 EUR Freigrenze § 8 Abs 2 EStG. Anwendungsfall geldwerte Vorteile Gutscheine Sachgeschenke Aufmerksamkeiten Begründung steuerfrei wenn unter 50 EUR/Monat. Methodik Prüfung Sachbezugs-Typ… |
| `stb-lohn-statistik-meldungen-destatis` | Statistik-Meldungen Verdienststatistik Destatis. Anwendungsfall jaehrliche oder unterjaehrige Statistik-Meldungen an das Statistische Bundesamt Verdienste Arbeitszeit. Methodik Pflicht-Prüfung Erfassung Übermittlung.… |
| `stb-lohn-streitfaelle-bag-bsg-haftungsrisiko` | Lohn-Streitfaelle BAG-Linie BSG-Linie StB-Haftungsrisiko. Anwendungsfall typische Streitfaelle Werkvertrag versus AN Status arbeitsrechtlich vs sozialversicherungsrechtlich Klagerisiko. Methodik Rechtsprechungsanalyse… |
| `stb-lohn-sv-beitraege-grundlagen` | Sozialversicherungs-Beitraege Grundlagen RV KV PV AV Umlagen. Anwendungsfall monatliche Lohnabrechnung mit SV-Berechnung Beitragsbemessungsgrenzen AG-AN-Aufteilung Sonderfaelle. Methodik Beitragsberechnung mit JAEG BBG… |
| `stb-lohn-sv-meldungen-dakota-svnet` | SV-Meldungen über sv.net oder DAKOTA. Anwendungsfall Beitragsnachweis Meldung an Krankenkassen elektronische Übermittlung Prüfung Quittungen. Methodik System-Wahl Konfiguration. Output Meldebescheinigungen Quittungen. |
| `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` | Überstunden Arbeitszeitkonto Stundenkonto Auszahlung. Anwendungsfall AN haeuft Überstunden an Bilanzierung im Arbeitszeitkonto Abbau in Freizeit oder Auszahlung lohn- und sv-rechtliche Behandlung. Methodik Aufzeichnung… |
| `stb-lohn-umlage-u1-u2-insogeld-umlage` | Umlagen U1 U2 Insolvenzgeld-Umlage. Anwendungsfall AG-Umlagen monatlich Erstattung Krankheit Mutterschaft Insolvenz Berechnung Saetze Variabilitaet KK. Methodik Prüfung Pflicht Kleinunternehmer 30 AN. Output… |
| `stb-lohn-vermoegenswirksame-leistungen` | Vermögenswirksame Leistungen VL AG-Anteil AN-Sparzulage. Anwendungsfall AG-Zuschuss bis 480 EUR jaehrlich AN-Sparzulage einkommensabhaengig Bausparen Aktien-Fonds. Methodik Prüfung Antrag AN-Sparzulage Beratung. Output… |
| `stb-lohn-werkstudent-pauschalen` | Werkstudent SV-Status 20-Stunden-Grenze pauschale Beitraege. Anwendungsfall Beschaeftigung Student Werkstudentenprivileg KV-Befreiung RV-Pflicht JAEG nicht relevant Klassifizierung. Methodik Prüfung 20-Stunden-Woche… |
| `stb-mandanten-onboarding-checkliste-vollservice` | Onboarding-Checkliste Neumandant Vollservice. Anwendungsfall Mandatsannahme Standardablauf Mandantenvereinbarung Vollmachten DSGVO-Information Buchführung Lohn Steuererklärung. Methodik strukturierter Checkliste.… |
| `stb-mandantenanfrage-reaktion-frist-laufend` | Mandantenanfragen Reaktionsfristen Servicelevel. Anwendungsfall Standardisierte Reaktion auf Mandantenanfragen klare Service-Versprechen Eskalation. Methodik SLA-Festlegung. Output Service-Standard-Dokument. |
| `stb-mandantenfragebogen-jahresabschluss` | Mandantenfragebogen zum Jahresabschluss. Anwendungsfall JA-Vorbereitung systematische Datenerhebung vom Mandanten Bestaende Forderungen Verbindlichkeiten Rückstellungen Sondervorgaenge. Methodik strukturierter… |
| `stb-mandantenkommunikation-bwa-uebergabe-quartal` | Quartalsgespraech BWA-Übergabe. Anwendungsfall systematische Quartalskommunikation mit Mandant Ergebnisbesprechung Steuerthemen Investitionsplanung. Methodik Termin-Vorbereitung Agenda Dokumentation. Output… |
| `stb-mandantenrechnung-honorar-stbvv` | Mandantenrechnung Honorar StBVV. Anwendungsfall Honorarabrechnung Pauschal- Zeit- und Gegenstandswert-Honorar Steuerberatergebührenverordnung. Methodik Rechnungsschreibung Gebührensaetze § 33 35 35a. Output… |
| `stb-online-portal-datev-mandantenshop` | DATEV Unternehmen Online Mandantenshop. Anwendungsfall Belegtransfer Bank-Abruf Auswertungs-Download Mandantenakte digital für Mandant. Methodik Konfiguration Benutzer Schulung Mandant. Output eingerichtetes Portal. |
| `stb-pruefliste-belegabgabe-monatlich` | Prüfliste monatliche Belegabgabe. Anwendungsfall standardisierte Belegabgabe-Kontrolle Mandant Vollständigkeit Bankauszuege Kasse Eingangsrechnungen Ausgangsrechnungen Lohnauswertung. Methodik Prüfliste… |
| `stb-routine-monatsabschluss-30-tage-zyklus` | Routine Monatsabschluss im 30-Tage-Zyklus. Anwendungsfall systematische Steuerung der Monatsabschluss-Routine in der Kanzlei mit klaren Deadlines Belegabgabe Buchung BWA-Versand USt-VA. Methodik Termin-Controlling.… |
| `stb-routine-quartalsabschluss-prozess` | Routine Quartalsabschluss-Prozess. Anwendungsfall vierteljaehrlicher Quartalsabschluss mit Periodenabgrenzung Quartals-BWA Mandantengespraech und Steuerthemen. Methodik strukturierter Quartals-Plan. Output Quartals-BWA… |
| `stb-sage-buchhalter-bwa-konfiguration` | Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage. |
| `stb-susa-anlagenkonten-ueberblick` | Anlagenbuchhaltung in der SuSa Anlagenkonten Klasse 0 SKR 03 immaterielle WG Sachanlagen Finanzanlagen Buchwerte. Anwendungsfall Monats- oder Jahres-SuSa mit Anlagenbestand AfA-Aktualisierung Zu- und Abgaenge. Methodik… |
| `stb-susa-debitorenliste-osa-offene-posten` | Debitoren-Saldenliste und Offene-Posten-Auswertung OPOS. Anwendungsfall Monats- oder Quartalsauswertung Mahnwesen Forderungsanalyse Bilanzvorbereitung. Methodik OPOS-Liste Fälligkeitsstrukur Top-Schuldner… |
| `stb-susa-erstellen-grundlagen` | Summen- und Saldenliste SuSa erstellen Grundlagen. Anwendungsfall monatliche Erstellung aus Finanzbuchhaltung Hauptbuchkonten Personenkonten Erfolgskonten Bestandsbuchungen. Methodik Aufbau Prüfung Verwendung. Output… |
| `stb-susa-formfehler-pruefen` | SuSa-Prüfung auf Formfehler Plausibilitaet und Differenzen. Anwendungsfall Qualitaetsprüfung der SuSa vor Versand oder Prüfung Buchungsdifferenzen typische Anomalien. Methodik Checkliste Plausibilitaet… |
| `stb-susa-haupt-und-personenkonten` | SuSa-Auswertung Hauptbuchkonten und Personenkonten separat auswerten. Anwendungsfall Prüfung Hauptbuch Sammelkonten 1400 1500 vs Personenkonten Debitoren Kreditoren OPOS. Methodik Konsistenz Hauptbuch zu Personenkonten… |
| `stb-susa-kreditorenliste-ova` | Kreditoren-Saldenliste OVA Offene-Verbindlichkeiten-Auswertung. Anwendungsfall Monats- oder Quartalsauswertung Zahlungsdisposition Lieferanten-Analyse Bilanzvorbereitung. Methodik Fälligkeitsstaffel Top-Lieferanten… |
| `stb-susa-monatlich-quartalsweise` | Periodische SuSa-Erstellung monatlich oder quartalsweise. Anwendungsfall standardisierter Erstellungsprozess Wahl der Periodizitaet Belegvolumen Mandantengroesse. Methodik Wahl der Frequenz Kommunikations-Routine.… |
| `stb-susa-saldenabstimmung-bestaetigung` | Saldenabstimmung und Saldenbestätigung im Jahresabschluss-Anlass. Anwendungsfall Bilanzvorbereitung Stichtag Forderungen und Verbindlichkeiten Lieferanten Kunden Banken. Methodik Abstimmungsschreiben Antwortauswertung… |
| `stb-susa-saldennullstellung-jahresende` | Erfolgskonten-Saldennullstellung zum Jahresende. Anwendungsfall Jahresabschluss-Vorbereitung Schluss-SuSa GuV-Überleitung Bilanzgewinn auf Konto 800 oder 2000. Methodik Abschlussbuchungen über GuV-Konto. Output… |
| `stb-susa-vorperiode-vergleich` | SuSa-Periodenvergleich Vormonat und Vorjahr. Anwendungsfall Prüfung Salden-Konsistenz Saldenentwicklung Vergleich der einzelnen Konten über Perioden. Methodik Differenz-Tabelle Auffälligkeit Hinweis-Liste. Output SuSa… |
| `stb-ueberschuldungspruefung-19-inso` | Stichtagsbezogene Überschuldungsprüfung einer GmbH nach § 19 Abs. 2 InsO durch den Steuerberater. Anwendungsfall Jahresabschluss oder BWA zeigt Krisensignale Steuerberater muss Überschuldung rechtssicher prüfen.… |
| `stb-warnschreiben-krisensignale` | Schreibvorlage Steuerberater-Warnschreiben an Mandanten-Geschäftsführung bei Krisensignalen aus Bilanz BWA SuSa Liquiditaet. Anwendungsfall Steuerberater erkennt Krisensignale und muss Hinweispflicht nach § 102 StaRUG… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Steuerstreit und Steuerprozess entwickeln. Anwendungsfall Mandant will Steuerstreit durch Einigung beenden ohne Urteil oder Verfahren steht vor Schlussbesprechung oder… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Spezial-Skills aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Keine Rechtsberatung. Dieser Skill strukturiert Workflow, Intake und Routing; fachliche Ergebnisse brauchen je nach Thema die passenden Spezial-Skills und menschliche Endprüfung.
