# Regulatorischer Quellenkatalog

Ein Startkatalog für den Reg-Feed-Watcher. Das Kaltstart-Interview konfiguriert,
welche Quellen überwacht werden sollen; dieser Katalog stellt die Optionen bereit. URLs verifiziert stand
**Mai 2026** — Feed-URLs ändern sich; bei ausbleibenden Ergebnissen einer Quelle verifizieren.

**Lesehinweis:**
- **Format** — was der Feed zurückgibt: JSON-API (strukturiert, am besten), RSS/Atom (halbstrukturiert, gut), HTML-Seite (benötigt Änderungserkennung), E-Mail (erfordert Gmail/Outlook-MCP-Integration).
- **Ebene** — *Primär* bedeutet der Regulator selbst; *Sekundär* bedeutet ein Kommentator, Aggregator oder eine Kanzlei, die Primärquellen zusammenfasst. Sekundärquellen immer auf die Primärquelle zurückverfolgen, bevor sie als maßgeblich behandelt werden.
- **Auth** — Keine = offen; Schlüssel = kostenloser, aber registrierungspflichtiger API-Schlüssel; Kostenpflichtig = Abonnement erforderlich.
- **Hinweise** — etwaige Besonderheiten (Rate-Limits, eingestellte Feeds, Auffindungsschritte).

Mit ⚠️ markierte Quellen wurden von Nutzern oder Behörden als unzuverlässig oder
eingestellt gemeldet — vor der Konfiguration verifizieren.

---

## Bundesrecht — Primär (Deutschland)

| Quelle | Feed-URL | Format | Abdeckung | Auth | Hinweise |
|---|---|---|---|---|---|
| Bundesgesetzblatt (BGBl.) | `https://www.recht.bund.de/api/v1/norm?format=json` | JSON-API | Gesetze und Verordnungen des Bundes, amtliche Verkündungen | Keine | Bundesnormendatenbank recht.bund.de; Filter nach Datum und Rechtsgebiet möglich. Verbindliche Verkündung aller Bundesgesetze und Rechtsverordnungen. **Erste Anlaufstelle** für neue Bundesgesetze. |
| Bundesanzeiger (BAnz) | `https://www.bundesanzeiger.de/` | HTML + E-Mail-Alert | Bekanntmachungen, Handelsregister, Insolvenzbekanntmachungen, sonstige amtliche Veröffentlichungen | Keine (E-Mail-Alert) | Keine offizielle RSS-API bekannt; E-Mail-Benachrichtigung über die Seite konfigurierbar. Für regulatorische Verlautbarungen nachrangig gegenüber BGBl. |
| Gesetze im Internet (BMJV) | `https://www.gesetze-im-internet.de/` | HTML | Konsolidierte Fassungen aller deutschen Bundesgesetze und -verordnungen | Keine | ⚠️ Kein strukturierter Feed; manuelle Prüfung oder Änderungserkennung erforderlich. Maßgeblich für Gesetzestexte in aktueller Fassung. |
| BaFin — Pressemitteilungen | `https://www.bafin.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed_Presse.xml` | RSS | Aufsichtsrechtliche Allgemeinverfügungen, Rundschreiben, Verwaltungsakte, Bußgeldentscheidungen | Keine | Weiterer BaFin-Feed: Verbraucherwarnungen. BaFin-Journal erscheint monatlich (PDF, kein Direktfeed — manuelle Prüfung). BaFin zuständig für Banken-, Versicherungs- und Wertpapieraufsicht (§ 6 WpHG, KWG, VAG). |
| BaFin — Konsultationen | `https://www.bafin.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed_Konsultationen.xml` | RSS | Konsultationsentwürfe, Merkblätter, Hinweisschreiben | Keine | Wichtig für frühzeitige Beteiligung an Regulierungsvorhaben. |
| BSI — Publikationen und Pressemitteilungen | `https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsreader.xml` | RSS | IT-Sicherheitswarnungen, technische Richtlinien (BSI-Richtlinien), Verlautbarungen nach BSIG, NIS2-Umsetzung | Keine | BSI-Grundschutz-Kompendium: eigenes Dokument, kein Feed. Für KRITIS-Betreiber besonders relevant (§ 8a BSIG). |
| BNetzA — Pressemitteilungen | `https://www.bundesnetzagentur.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed_Presse.xml` | RSS | Regulierung Energie, Telekommunikation, Post; Rundfunk; Eisenbahn; Konsultationen | Keine | Separate Feeds für einzelne Sektoren auf der BNetzA-Webseite. Zuständig nach TKG, EnWG, PostG, ERegG. |
| Bundeskartellamt | `https://www.bundeskartellamt.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed_Pressemitteilungen.xml` | RSS | Fusionskontrolle, Kartellverfahren, Missbrauchsverfahren, Sektoruntersuchungen | Keine | Entscheidungsdatenbank unter bundeskartellamt.de/entscheidungen. |
| Bundesrat — Drucksachen | `https://www.bundesrat.de/SharedDocs/rss/DE/tagesordnung-feed.xml?__blob=publicationFile` | RSS | Tagesordnungen, Drucksachen, Beschlüsse | Keine | Für Gesetzgebungsvorhaben im zweiten Durchgang. Drucksachen-Volltextsuche unter bundesrat.de/bv.html. |
| BMJ — Referentenentwürfe | `https://www.bmj.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed_Pressemitteilungen.xml` | RSS | Referentenentwürfe, Regierungsentwürfe, Pressemitteilungen des Bundesministeriums der Justiz | Keine | Entwürfe häufig früher über bundesrat.de oder bmj.de als über BGBl. zugänglich. |
| BMWK (Bundesministerium für Wirtschaft) | `https://www.bmwk.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed_Presse.xml` | RSS | Wirtschaftsrecht, Energierecht, Außenwirtschaft, KI-Strategie | Keine | |
| Bundesarbeitsgericht (BAG) — Pressemitteilungen | `https://www.bundesarbeitsgericht.de/presse/rss-feed/` | RSS | Aktuelle BAG-Entscheidungen (Kurzfassungen) | Keine | Volltexte auf bundesarbeitsgericht.de/entscheidungen; Leitsätze zeitversetzt. |
| Bundesgerichtshof (BGH) — Pressemitteilungen | `https://www.bundesgerichtshof.de/cgi-bin/rechtsprechung/rss.cgi?Gericht=bgh&Art=pm` | RSS | BGH-Entscheidungen (Zivilsenate und Strafsenate, Kurzfassungen) | Keine | Volltexte auf bundesgerichtshof.de; ECLI-Suche über juris oder openjur möglich. |
| Bundesdatenschutzbeauftragter (BfDI) | `https://www.bfdi.bund.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed.xml` | RSS | Tätigkeitsberichte, Stellungnahmen, Pressemitteilungen; DSGVO-Aufsicht für Bundesbehörden | Keine | Für DSGVO-Aufsicht bei Bundesbehörden und Telekommunikationsunternehmen (TDDDG). |

---

## Landesrecht — Primär (Auswahl)

Abdeckung ist uneinheitlich. Bundesländer mit aktiver Datenschutz- und Verbraucherschutzdurchsetzung bevorzugt. Viele Landesbehörden veröffentlichen ausschließlich HTML-Seiten — falls kein RSS, als „manuell" konfigurieren oder Webseitenänderungserkennung einrichten.

| Quelle | Feed-URL | Format | Abdeckung | Auth | Hinweise |
|---|---|---|---|---|---|
| LfDI Bayern | `https://www.lda.bayern.de/de/news.html` | HTML | Datenschutzaufsicht Bayern (privater Sektor) | Keine | ⚠️ Kein direkter RSS-Feed bekannt; Pressemitteilungen auf der Seite. E-Mail-Benachrichtigung prüfen. |
| LfDI Baden-Württemberg | `https://www.baden-wuerttemberg.datenschutz.de/service/` | HTML | Datenschutzaufsicht BW | Keine | ⚠️ Kein öffentlicher RSS-Feed bekannt. |
| BlnBDI (Berlin) | `https://www.datenschutz-berlin.de/pressemitteilungen/` | HTML + RSS | Datenschutzaufsicht Berlin; im Fokus: Techunternehmen, AI-Act-Anwendungen | Keine | RSS-Option auf der Seite vorhanden; prüfen. |
| Hamburgischer Beauftragter für Datenschutz (HmbBfDI) | `https://datenschutz.hamburg.de/infothek/` | HTML | Datenschutzaufsicht Hamburg; zuständig für viele internationale Konzernzentralen in HH | Keine | ⚠️ Kein konsolidierter RSS-Feed bekannt. |
| Landesamt für Verbraucherschutz NRW | `https://www.verbraucherschutz.nrw.de/` | HTML | Verbraucherschutzdurchsetzung NRW | Keine | ⚠️ Kein öffentlicher RSS-Feed bekannt. |

---

## EU — Primär

| Quelle | Feed-URL | Format | Abdeckung | Auth | Hinweise |
|---|---|---|---|---|---|
| EUR-Lex (Amtsblatt der EU, ABl. EU) | `https://eur-lex.europa.eu/` | Webservice + RSS nach Suche | Verbindliche Veröffentlichungen im Amtsblatt der EU (L und C-Reihe); Verordnungen, Richtlinien, Entscheidungen | Schlüssel (kostenlos, Webservice) | Für verbindliche EU-Rechtsakte maßgeblich. RSS-Abonnement nach Suchfilter möglich. CELEX-Nummern als stabile Referenz. |
| Europäische Kommission — Press Corner | `https://ec.europa.eu/commission/presscorner/` | RSS + E-Mail | Pressemitteilungen, Reden, Q&As — DSGVO-Durchführungsakte, DSA, DMA, AI Act, NIS2 | Keine | Abonnement unter ec.europa.eu/commission/presscorner/login/de. Gefilterte Teilfeeds nach Thema. |
| Europäisches Parlament — Pressemitteilungen | `https://www.europarl.europa.eu/rss/doc/press/en.xml` | RSS | Plenarbeschlüsse, Ausschussergebnisse, Pressemitteilungen | Keine | Für Legislativverfahren auf EU-Ebene relevant. |
| Europäischer Datenschutzausschuss (EDSA/EDPB) | `https://www.edpb.europa.eu/news/news_en` | RSS (2 Feeds angeboten) | Leitlinien, Stellungnahmen, Durchsetzungszusammenfassungen, verbindliche Beschlüsse | Keine | Feeds auf edpb.europa.eu beschrieben. Für DSGVO-Aufsicht grenzüberschreitender Verarbeitungen federführend. |
| ENISA | — | E-Mail | Cybersicherheit, NIS2-Leitlinien | Keine | ⚠️ **RSS-Feeds eingestellt** mit neuer Website. Bis zur Einführung eines neuen Abonnementmechanismus nur E-Mail-Alerts (`enisa.europa.eu/rss-feeds-discontinued-new-subscription-mechanism-coming-soon`). |
| Europäischer Datenschutzbeauftragter (EDSB/EDPS) | `https://www.edps.europa.eu/press-publications/press-news_en` | HTML + RSS-Option | Datenschutzaufsicht EU-Institutionen | Keine | |
| EU-Finanzmarktaufsicht (ESMA) | `https://www.esma.europa.eu/press-news/rss` | RSS | MiFIR, MAR, EMIR, Prospektrecht, Leitlinien | Keine | Wichtig für Wertpapierrecht und Kapitalmarktrecht. |
| Europäische Bankenaufsichtsbehörde (EBA) | `https://www.eba.europa.eu/rss` | RSS | CRR/CRD-Durchführungsstandards, Q&A, Leitlinien, Stresstest-Ergebnisse | Keine | |
| Europäische Zentralbank (EZB) — Pressemitteilungen | `https://www.ecb.europa.eu/rss/press.html` | RSS | Bankenaufsicht (SSM), Leitzinsen, EZB-Leitlinien | Keine | Für beaufsichtigte Kreditinstitute im SSM unmittelbar relevant. |
| Europäischer Gerichtshof (EuGH) — Pressemitteilungen | `https://curia.europa.eu/jcms/jcms/Jo2_7052/de/` | HTML | EuGH- und EuG-Urteile, Vorabentscheidungen, Generalanwaltsschlussanträge | Keine | ⚠️ Kein direkter RSS-Feed auf der Startseite; Urteilssuche über curia.europa.eu. ECLI-Nummern als stabile Referenz. |

---

## International

| Quelle | Feed-URL | Format | Abdeckung | Auth | Hinweise |
|---|---|---|---|---|---|
| OECD AI Policy Observatory | `https://oecd.ai/en/` | HTML + Newsletter | Nationale KI-Strategien, OECD-Leitlinien | Keine | Geeignet für die Verfolgung von KI-Regulierung außerhalb der EU. |
| Europarat | `https://www.coe.int/de/web/portal/news` | RSS + HTML | Europaratsübereinkommen einschließlich KI-Rahmenübereinkommen (CETS Nr. 225) | Keine | |
| UK ICO | `https://ico.org.uk/global/rss-feeds/` | RSS (mehrere Feeds) | Durchsetzung, Leitlinien, Nachrichten, Konsultationen (UK GDPR, DPA 2018) | Keine | Separate Feeds für Nachrichten, Durchsetzungsmaßnahmen und Blog. |
| CNIL (Frankreich) | `https://www.cnil.fr/en/rss.xml` (verifizieren) | RSS | Französische DSGVO-Entscheidungen, Leitlinien, Sanktionen | Keine | Englischsprachige Neuigkeiten unter cnil.fr/en/news. Drittanbieter-Indizes deuten auf Feed hin; vor Einbindung verifizieren. |

---

## Sekundär / Aggregatoren

**Inhalte aus diesen Quellen als Hinweise, nicht als Autorität behandeln.** Wenn eine Sekundärquelle meldet „BaFin hat X veröffentlicht" bedeutet das: X auf bafin.de suchen und dann darauf stützen. Aus diesen Feeds gezogene Einträge im Digest als `[Sekundärquelle]` kennzeichnen.

| Quelle | Feed-URL | Format | Abdeckung | Auth | Hinweise |
|---|---|---|---|---|---|
| IAPP Daily Dashboard | `https://iapp.org/rss/daily-dashboard/` | RSS | Globale Datenschutz- und KI-Governance-Neuigkeiten, kuratiert | Keine (einzelne Artikel ggf. hinter Paywall) | Höchstes Signal-Rausch-Verhältnis für Datenschutzteams. |
| Future of Privacy Forum (FPF) | `https://fpf.org/feed/` | RSS (WordPress) | Datenschutzkommentare, Länder-Rechts-Tracker, Berichte | Keine | |
| Freshfields | `https://www.freshfields.com/en-gb/our-thinking/` | RSS/HTML | Mandanteninformationen zu deutschem und EU-Recht (Gesellschaftsrecht, Kartellrecht, Finanzrecht) | Keine | Fachbereichsbezogene Sub-Feeds prüfen. |
| Linklaters — Insights | `https://www.linklaters.com/en/insights` | HTML + E-Mail | EU-Regulierung, Finanzrecht, Datenschutz | Keine | ⚠️ Kein konsolidierter öffentlicher RSS bekannt; E-Mail-Newsletter als Hauptkanal. |
| Hogan Lovells | `https://www.hoganlovells.com/en/rss` | RSS (mehrere nach Rechtsgebiet) | Mandanteninformationen, Regulierungsrecht | Keine | Fachbereichsbezogene Teilfeeds vorhanden. |
| Noerr — Blog | `https://www.noerr.com/de/insights` | HTML | Deutsches und europäisches Wirtschaftsrecht | Keine | ⚠️ Kein öffentlicher RSS-Feed bekannt. |
| Beck-Blog (beck-community) | `https://community.beck.de/feed` | RSS | Rechtliche Fachkommentare zu aktuellen BGH/BVerwG/BAG-Urteilen und Gesetzgebung | Keine | Hohe Aktualität; breites Themenspektrum. |
| Lexology | `https://www.lexology.com/account/rss` | RSS (konfigurierbar nach Thema/Rechtsordnung) | Aggregierte Kanzlei-Alerts | Konto (kostenlos) | Mächtig: Themen- und Rechtsordnungsfeeds aufbauen. Gehört zu LBR. |
| JD Supra | `https://www.jdsupra.com/legal-news/rss-law-feeds.aspx` | RSS (mehrere nach Thema) | Aggregierte Kanzlei-Alerts | Keine | Breiter und rauschiger als Lexology. |
| Artificial Lawyer | `https://www.artificiallawyer.com/feed/` | RSS | Legal-Tech-/KI-Regulierungsnachrichten | Keine | |

---

## Quellen ohne Feeds (Webseitenmonitoring oder E-Mail erforderlich)

Einige wichtige Quellen veröffentlichen keine Feeds oder deren RSS wurde eingestellt.
Die Überwachung erfordert:
- Webseitenänderungserkennung (derzeit nicht eingebaut)
- E-Mail-Newsletter-Weiterleitung (erfordert Gmail/Outlook-MCP-Integration)
- Manuelle Prüfung über den Reg-Feed-Watcher-Pfad „manuelle Eingabe"

| Quelle | URL | Hinweise |
|---|---|---|
| ENISA | `https://www.enisa.europa.eu/news` | RSS eingestellt; neuer Abonnementmechanismus in Vorbereitung |
| Datenschutzbehörde Irland (DPC) | `https://www.dataprotection.ie/en/news-media/latest-news` | Kein RSS; bedeutsam für DSGVO-Durchsetzung bei US-Technologieunternehmen |
| BaFin-Journal | `https://www.bafin.de/DE/PublikationenDaten/BaFinJournal/bafin_journal_node.html` | Monatliches PDF, kein Feed; manuelle Prüfung |
| LfDI Bayern | `https://www.lda.bayern.de/de/news.html` | Kein RSS bekannt |
| Hamburgischer Beauftragter (HmbBfDI) | `https://datenschutz.hamburg.de/` | Kein konsolidierter RSS bekannt |
| Noerr | `https://www.noerr.com/de/insights` | E-Mail-Abonnement als primärer Kanal |
| BMJ — Referentenentwürfe (Volltext) | `https://www.bmj.de/SharedDocs/Gesetzgebungsvorhaben/` | Volltexte als PDFs auf der BMJ-Seite; kein strukturierter Feed |
| Bundesrat — Volltext-Drucksachen | `https://www.bundesrat.de/SharedDocs/drucksachen/` | Inhaltsverzeichnis mit RSS, Volltexte als PDFs |

---

## Empfohlene Starterpakete

**Datenschutz-fokussiertes Inhouse-Team (Deutschland + EU):**
BGBl., BaFin-Pressemitteilungen, BfDI-Feed, EUR-Lex (DSGVO, AI-Act-Filter), EDSA/EDPB, EDPS, BlnBDI (RSS prüfen), LfDI Bayern (Änderungserkennung), IAPP, FPF.

**Allgemeines regulatorisches Inhouse-Team (breit):**
BGBl., BAnz (E-Mail-Alert), BaFin (Pressemitteilungen + Konsultationen), BSI, BNetzA, Bundeskartellamt, BMJ-RSS, Bundesrat-RSS, EUR-Lex (nach Rechtsgebieten filtern), Europäische Kommission Press Corner, ESMA, EBA. IAPP + Lexology für Aggregatorabdeckung ergänzen.

**KI-Governance-Team:**
BGBl. (Filter: BMWK, BMJ, BMDV), BSI-RSS, Europäische Kommission Press Corner (AI Act, AIA-Durchführungsakte), EDSA/EDPB, OECD AI Observatory, Europarat (CETS Nr. 225), BfDI, IAPP, Artificial Lawyer.

---

## Quelle hinzufügen

Um eine Quelle hinzuzufügen, die nicht in diesem Katalog enthalten ist:
1. Feed-URL ermitteln (versuchen Sie `/rss`, `/feed`, `/news.rss` oder Seitenquelltext nach `<link rel="alternate" type="application/rss+xml">` durchsuchen).
2. Mit `curl` oder im Browser prüfen, ob die URL XML/JSON zurückgibt.
3. In der regulatorischen-recht-CLAUDE.md des Benutzers unter **Feed-Konfiguration → Direkte Behördenfeeds** eintragen, mit: Quellenname, URL, Format, Abdeckung.
4. Falls kein Feed vorhanden, unter **Quellen ohne Feeds** eintragen und entscheiden: manuell, E-Mail oder Änderungserkennung.
