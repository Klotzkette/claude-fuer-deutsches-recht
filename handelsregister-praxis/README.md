# Handelsregister Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`handelsregister-praxis`) | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B** (`handelsregister-registergericht-rabenhof-gmbh-2026`) | [Gesamt-PDF lesen](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf) | [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Registergerichts-Cockpit für Gesellschaftsrechtler, Notariate, Kanzleien und Rechtsabteilungen. Es ordnet, was eingetragen werden soll, welche Urkunden nötig sind, wer beim Registergericht entscheidet, wie man Beanstandungen beantwortet und wann Beschwerde oder Eilrechtsschutz Sinn ergeben.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `handelsregister-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [HGB §§ 8 ff., § 15](https://www.gesetze-im-internet.de/hgb/)
- [FamFG Registersachen und Beschwerde](https://www.gesetze-im-internet.de/famfg/)
- [GmbHG Anmeldung, Gesellschafterliste, Kapitalmaßnahmen](https://www.gesetze-im-internet.de/gmbhg/)
- [Registerportal der Länder](https://www.handelsregister.de/)
- [Unternehmensregister](https://www.unternehmensregister.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 76 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtsloeschung-familienloeschung-registerblatt` | Prüft Löschungsandrohung, Anhörung, Unrichtigkeit, Vermögenslosigkeit, Gegenwehr und Dokumentationsstrategie im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `auslandsurkunden-apostille-legalisation-uebersetzung` | Prüft Apostille, Legalisation, beglaubigte Übersetzung, Existenznachweis und Vertretungsnachweis im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `beanstandung-zwischenverfuegung` | Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Fristverlängerung oder Beschwerdevorbereitung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkma... |
| `bekanntmachungen-monitoring` | Erstellt Monitoringplan für Bekanntmachungen, Friststart, Einspruchsfenster und Mandantenalerts im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Out... |
| `chronologischer-registerauszug` | Rekonstruiert Registergeschichte, kritische Umschlagpunkte und mögliche Inkonsistenzen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit N... |
| `closing-handelregister-einstweiliger` | Prüft CP/CS, Eintragungsabhängigkeiten, Vollzugsreihenfolge, Escrow, Notarbestätigung und Bring-down im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierte... |
| `einstweiliger-rechtsschutz-registerstreit` | Plant Schutz gegen drohende Eintragung, Verzögerung, Registersperre, Gesellschafterlistenstreit und Vollzugsschäden im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `eintragung-prozessvergleich-registerfolge` | Übersetzt gerichtliche Vergleiche in Beschluss, Anmeldung, Liste, Löschung oder Berichtigung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `erlaubnispflichtige-taetigkeit-famfg` | Prüft KWG, ZAG, GewO, Handwerk, Arbeitnehmerüberlassung und ob das Registergericht Nachweise verlangen kann im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `famfg-beschwerde-registersache` | Prüft Statthaftigkeit, Beschwer, Frist, Form, Abhilfe, Nichtabhilfe und Beschwerdebegründung gegen Registerentscheidungen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `fehlerhafte-eintragung-berichtigung` | Prüft Schreibfehler, materiell falsche Eintragung, Amtskorrektur, Löschung, neue Anmeldung und Haftungsnotiz im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `firma-firmenbildung-formwechsel-registercheck` | Prüft Firmenkern, Unterscheidbarkeit, Irreführung, Rechtsformzusatz, IHK-Stellungnahme und Abgrenzung zu Marke/Domain im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `formwechsel-registercheck` | Prüft Formwechselbericht, Beschlüsse, Satzung, neue Firma, Registerwechsel und Identitätskontinuität im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierte... |
| `frist-und-vollzugslog-register` | Baut ein Log für Beanstandungsfristen, Eintragungsdatum, Bekanntmachung, Closing-Abhängigkeit und Mandantenbericht im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefer... |
| `genossenschaft-registerschnittstelle` | Prüft Vorstand, Aufsichtsrat, Prüfung, Satzung und Eintragungslogik bei eG im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoint... |
| `gesellschafterlistenstreit-eilstrategie-gmbh` | Ordnet Anspruch, einstweilige Verfügung, Registersperre, materiellen Streit und Kommunikation mit Registergericht/Notar im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `gmbh-co-kg-registerdoppelvollzug` | Koordiniert KG-Register, Komplementär-GmbH, Vertretung, Gesellschafterlisten und Firmenidentität im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `gmbh-geschaeftsfuehrerbestellung-abberufung` | Prüft Beschluss, Anmeldung, Versicherung, Vertretungsregel, Amtsannahme, Abberufung und Handelsregistervollzug im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `gmbh-gesellschafterliste-paragraph-gruendung` | Prüft Liste, Prozentangaben, Veränderungsspalte, Notarzuständigkeit, Legitimationswirkung und Streit über Unrichtigkeit im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `gmbh-gruendung-erstanmeldung` | Checkt Stammkapital, Einzahlung, Geschäftsführer, Versicherung, Musterprotokoll, Gesellschaftsvertrag und Registereintragung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechu... |
| `gmbh-kapitalerhoehung-bareinlage` | Prüft Satzungsänderung, Übernahme, Einzahlung, Anmeldung, Versicherung, Liste und Registervollzug im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `gmbh-kapitalerhoehung-sacheinlage` | Prüft Sacheinlagebericht, Werthaltigkeit, verdeckte Sacheinlage, Anmeldung und Beanstandungsrisiko im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `gmbh-kapitalherabsetzung-und-schutzjahr` | Prüft Gläubigerschutz, Sperrjahr, Bekanntmachungen, Versicherung und registerfeste Unterlagen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outpu... |
| `gmbh-liquidation-und-loeschung` | Führt durch Auflösung, Liquidatoren, Sperrjahr, Schlussbilanz, Löschung, Nachtragsliquidation und Registerkommunikation im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `gmbh-satzungsaenderung-handelsvollmacht-nicht` | Prüft Beschlussmehrheit, notarielle Beurkundung, vollständige Neufassung, Gegenstand, Firma, Sitz, Kapital und Anmeldung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `handelsvollmacht-nicht-eintragungsfaehig` | Erklärt, was nicht ins Register gehört und wie interne Vollmachten dennoch sicher dokumentiert werden im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisiert... |
| `insolvenzvermerk-registereintrag` | Prüft Eintragung von Eröffnung, Eigenverwaltung, Aufhebung, Insolvenzplan, Freigabe und Wirkungen für Vertretung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `internationaler-registervergleich` | Vergleicht Companies House, irische/österreichische/schweizer Register und deutsche Nachweisanforderungen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `kaltstart-routing` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `kg-kommanditist-eintritt-austritt-haftsumme` | Prüft Einlage/Haftsumme, Sonderrechtsnachfolge, Austritt, Nachhaftung und Registerpublizität im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `ki-registerakte-nachlass` | Zwingt zu Belegpfad, Registerauszug, Aktenzeichen, Normenanker und klarer Kennzeichnung nicht verifizierter Annahmen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `nachlass-und-testamentsvollstrecker-register` | Prüft Erbschein, Europäisches Nachlasszeugnis, Testamentsvollstreckerzeugnis und Vertretungsmacht im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `notar-registergericht-kommunikation` | Erstellt klare Nachreichungslisten, Telefonnotizen, E-Mail-Entwürfe und Mandantenupdates ohne Schuldzuweisungschaos im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `ohg-kg-online-abruf-partg-partgmbb` | Prüft kaufmännischen Betrieb, Statuswechsel, Anmeldung, Gesellschafter, Vertretung und MoPeG-Schnittstellen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `online-abruf-registerportal-unternehmensregister` | Führt durch Handelsregister, Unternehmensregister, Bekanntmachungen, Chronologie, Ausdrucke, Screenshots und Beleglog im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `partg-partgmbb-register` | Prüft Partnerschaftsregister, Berufszulassung, Namensführung, Haftungsbeschränkung und Berufshaftpflichtnachweis im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `prokura-eintragung-rechtsabteilung` | Prüft Einzel-/Gesamtprokura, Filialprokura, Gesamtvertretung, Widerruf, Publizität und Unterschriftenmuster im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug` | Rechtsabteilungs-Fachmodul für Geschäftsführerbestellung mit Auslandsbezug: Identität, Versicherung, Unterschrift und Übersetzung werden sauber vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im H... |
| `rechtsabteilung-gesellschafterliste-nach-streit-und-ev` | Rechtsabteilungs-Fachmodul für Gesellschafterliste nach Streit und EV: Rechtsabteilungen bauen registertaugliche Listenpakete und Widerspruchsstrategien. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Hand... |
| `rechtsabteilung-insolvenzvermerk` | Rechtsabteilungs-Fachmodul für Insolvenzvermerk und ausländischer Trustee: Vertretungsmacht ausländischer Insolvenzorgane wird registertauglich nachgewiesen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im... |
| `rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung` | Rechtsabteilungs-Fachmodul für Kapitalerhöhung und Zwischenverfügung: Zwischenverfügungen werden in heilbare Punkte, Streitpunkte und Beschwerde sortiert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Han... |
| `rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung` | Rechtsabteilungs-Fachmodul für MoPeG-Gesellschaftsregister und OHG-Sprung: GbR, eGbR, OHG und Grundstücksfähigkeit werden registerlogisch abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsr... |
| `rechtsprechung-register-frist-vollzugslog` | Legt fest, wie Entscheidungen in Registersachen nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink ausgegeben werden im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung... |
| `rechtsschein-innenstreit-register` | Trennt materielles Gesellschaftsrecht, Registerlage, Vertretungsmacht und Gutglaubensschutz im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `register-mandantenbrief` | Erstellt klare Mandantenupdates: Stand, Risiko, To-dos, Fristen, nächste Entscheidung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit No... |
| `register-qualitaetsgate-vor-einreichung` | Checkliste vor dem Absenden: Urkunden, Beschlüsse, Listen, Unterschriften, Kapital, Namen, Daten, Registerblatt im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `registerakte-schnellscan-registerauszug-lesen` | Erstellt eine Vollzugskarte aus Satzung, Beschluss, Anmeldung, Liste, Notarvermerk, Gerichtsschreiben und Fristenlog im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `registerauszug-lesen` | Erklärt Abteilungen/Spalten, Historie, Vertretung, Kapital, Firma, Prokura, Insolvenz und Bekanntmachungen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priori... |
| `registerbeweis-im-prozess` | Bereitet Registerauszüge, Bekanntmachungen und Nachweise prozesstauglich auf im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoi... |
| `registergericht-rollen-datenschutz` | Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rein vollzugstechnisch hängt im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Be... |
| `registergericht-und-datenschutz` | Klärt öffentliche Registerdaten, sensible Anlagen, Schwärzungen, Anschriften und Löschungswünsche im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `registerkosten-und-notarkosten` | Ordnet Register- und Notarkosten grob, vermeidet Doppelvollzug und erklärt Mandanten die Kostenlogik im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierte... |
| `registerrecht-aktiengesellschaft-vorstand` | Prüft Bestellung, Vertretung, Satzungsänderungen, Kapitalmaßnahmen und Eintragung bei der AG im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `registerrecht-beschlussmaengel-und-registervollzug` | Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beachten muss, wie weit die formelle Prüfung reicht und wann der materielle Streit auf Zivilprozess/Eilrechtsschutz verlag... |
| `registerrecht-digitalgruendung` | Prüft Online-Beurkundung/Beglaubigung, Identifizierung, digitale Einreichung und Medienbruch im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `registerrecht-fehlende-einzahlung-fehlerhafte` | Prüft Geschäftsführerversicherung, Kontoauszug, Hin- und Herzahlen, verdeckte Sacheinlage und Haftungsnotiz im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prior... |
| `registerrecht-fehlerhafte-geschaeftsfuehreradresse` | Prüft Anschriften, Geburtsdaten, Schutzinteressen, Schwärzungsmöglichkeiten und Auszugstypen im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `registerrecht-kapitalgesellschaft-co-kg-komplementaerwechsel` | Koordiniert Ausscheiden/Eintritt der Komplementär-GmbH, Haftung, Vertretung und Registerreihenfolge im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `registerrecht-mandatsannahme-notarferne` | Klärt Rolle der anwaltlichen Beratung neben Notar, Verantwortungsgrenzen und Mandantensteuerung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Out... |
| `registerrecht-niederlassung-registergericht` | Prüft eintragungsfähige Zweigniederlassung, unselbständige Betriebsstätte und Adress-/Vertretungsangaben im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisi... |
| `registerrecht-registergericht-telefonat-protokoll` | Erstellt kurze Telefonnotiz mit Name, Aktenzeichen, Beanstandung, Frist, Zusage und Folgeschritt im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Ou... |
| `registerrecht-registerzeichen-und-aktenzeichen` | Erklärt HRB, HRA, PR, GnR, VR, Registernummer, Gericht und Aktenzeichenlogik im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoi... |
| `registerrecht-scheinloeschung` | Prüft Restvermögen, Prozessfähigkeit, Bestellung Nachtragsliquidator und Registereintragung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output... |
| `registerrecht-se-und-europaeische-gesellschaft` | Prüft SE-Firma, Sitz, monistisches/dualistisches System, Leitung, Verwaltungsrat und grenzüberschreitende Bezüge im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `registerrecht-umbenennung-rebranding` | Prüft Firmenänderung, Satzung, IHK, Marken-/Domainkonflikte, Bekanntmachung und Mandantenkommunikation im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisier... |
| `registersperre-closing-sitz-inlandsanschrift` | Bewertet Sperrwirkung, einstweilige Verfügung, Gesellschafterlistenkonflikt und Alternativvollzug im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `sitz-inlandsanschrift-und-geschaeftsanschrift` | Prüft Satzungssitz, inländische Geschäftsanschrift, Empfangsbevollmächtigte, Briefkastenrisiken und Registereintragung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `todesfall-gesellschafter-register` | Prüft Erbnachweis, Sonderrechtsnachfolge, Testamentsvollstrecker, Liste und Registerkommunikation im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `transparenzregister-schnittstelle-umwandlung` | Verbindet Handelsregisterdaten mit wirtschaftlich Berechtigten, GwG-Risiken und Meldepflichten im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Outp... |
| `umwandlung-registervollzug` | Prüft Verschmelzung, Spaltung, Formwechsel, Registerreihenfolge, Schlussbilanz und Bekanntmachung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten O... |
| `umzug-registerbezirk-amtsloeschung` | Prüft innerörtlich/anderer Bezirk, Satzungsänderung, Registerabgabe, Bekanntmachung und Adresslogik im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `unternehmensgegenstand-beanstandung` | Formuliert eintragungsfähige Gegenstände ohne Erlaubnis-/Aufsichtsrechtsfalle und ohne zu enge Zukunftsfessel im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pri... |
| `verein-registerschnittstelle-verschmelzung` | Klärt, wann Vereinsregisterlogik statt Handelsregisterlogik greift und welche Beschlüsse/Protokolle gebraucht werden im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `verschmelzung-gmbh-registercheck` | Checkt Verschmelzungsvertrag, Zustimmungsbeschlüsse, Registeranmeldungen, Gläubigerschutz und Wirksamkeitszeitpunkt im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `vollmacht-und-anmeldung-oeffentliche-beglaubigung` | Prüft notarielle Beglaubigung, Vertreteranmeldung, Untervollmacht, Signatur und elektronische Einreichung im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `zweigniederlassung-auslaendische` | Zweigniederlassung Auslaendische im Handelsregister-Praxis im Handelsregister Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
