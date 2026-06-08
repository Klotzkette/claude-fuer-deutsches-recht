# Meinungsprüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`meinungspruefer`) | [`meinungspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Meinungsprüfer - Grenzfälle im Alltag** (`meinungspruefer-grenzfaelle-alltag`) | [Gesamt-PDF lesen](../testakten/meinungspruefer-grenzfaelle-alltag/gesamt-pdf/meinungspruefer-grenzfaelle-alltag_gesamt.pdf) | [`testakte-meinungspruefer-grenzfaelle-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-meinungspruefer-grenzfaelle-alltag.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Prüfung von Äußerungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung oder Tatsachenbehauptung, Beleidigung, üble Nachrede, Verleumdung, Personen des politischen Lebens, Wahrnehmung berechtigter Interessen, zivilrechtliche Unterlassung, Widerruf, Geldentschädigung, Plattform- und Social-Media-Kontext, EGMR/EuGH/GRCh, OLG-/KG-Praxis und US-Supreme-Court-Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt eine strukturierte Vorprüfung und dokumentierbare Arbeitsprodukte zur anwaltlichen Kontrolle. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet.

## Start

```
/meinungspruefer:allgemein
```

Der Einstieg fragt schnell ab: exakter Wortlaut, Medium, Publikum, Anlass, Vorgeschichte, Betroffene, Tatsachenkern, Belege, Wiederholungsgefahr, gewünschter Output und Risikotoleranz. Danach routet er zu den passenden Spezialskills.

## Skills (36)

| Skill | Zweck |
|---|---|
| `meinungspruefer-allgemein` | Schöner Einstieg, Schnelltriage, Quellenhygiene und Routing |
| `schnelltriage-aeusserung` | Erste Ampel für Strafrecht, Zivilrecht, Plattform und arbeits-/schulbezogene Risiken |
| `zitat-und-kontextaufnahme` | Wortlaut, Kontext, Adressatenkreis, Medium und Vorgeschichte sauber erfassen |
| `meinung-tatsache-abgrenzung` | Meinung, Tatsache, gemischte Äußerung und Tatsachenkern trennen |
| `mehrdeutigkeit-sinnermittlung` | Sinnermittlung, Durchschnittspublikum und nicht ehrverletzende Deutungen |
| `beleglage-tatsachenbehauptung` | Belegmatrix für Tatsachen, Verdachtsäußerung und erwiesen unwahre Behauptung |
| `strafrecht-185-beleidigung` | § 185 StGB mit Art.-5-GG-Abwägung |
| `ueble-nachrede-186` | § 186 StGB, Nichterweislichkeit und Tatsachenkern |
| `verleumdung-187` | § 187 StGB, Wissen um Unwahrheit und Belegprüfung |
| `personen-politisches-leben-188` | § 188 StGB, Person des politischen Lebens, Öffentlichkeit und Erschwerung des Wirkens |
| `wahrnehmung-berechtigter-interessen-193` | § 193 StGB, Beschwerde, Bewertung, Mandats-/Arbeits-/Bürgerkontext |
| `strafantrag-194-und-verfahren` | Strafantrag, Antragsberechtigte, Fristen, Privatklage, Einstellungsoptionen |
| `schmaehkritik-formalbeleidigung-menschenwuerde` | Enge Ausnahmen ohne Normalabwägung |
| `abwaegung-art-5-gg` | Verfassungsrechtlicher Abwägungskern nach Art. 5 GG |
| `machtkritik-amtstraeger` | Amtsträger, Behörden, Bürgermeister, Schule, Justiz und Machtkritik |
| `arbeitgeber-betrieb-kantine` | Arbeitsplatz, Kantine, Kollegium, Betriebsrat, arbeitsrechtliche Nebenfolgen |
| `schule-elternchat` | Schule, Elternchat, Lehrkräfte, Schulleitung und pädagogischer Konflikt |
| `soziale-medien-x-linkedin` | X, LinkedIn, Kommentarspalten, Sichtbarkeit, Prangerwirkung, Screenshots |
| `kommunalrecht-buergermeister` | Kommunale Debatte, Bauprojekt, Ratssitzung, Amts- und Privatrolle |
| `satire-ironisierung-pinocchio` | Satire, Überzeichnung, Pinocchio-Vergleich, Lügenvorwurf als Wertung oder Tatsache |
| `schimpfwort-lackaffe-und-spott` | Spottbegriffe wie Lackaffe im Kontext prüfen |
| `zivilrecht-unterlassung-widerruf-schadensersatz` | APR, §§ 823, 1004 BGB analog, § 824 BGB und Beseitigungsansprüche |
| `presserecht-plattformen-loeschung-dsa` | Medien, Plattformmeldungen, Löschung, Sperrung und DSA-Schnittstellen |
| `europarecht-emrk-grch` | Art. 10 EMRK, Art. 11 GRCh, unions- und konventionsfreundliche Lesart |
| `egmr-art-10-rechtsprechung` | EGMR-Leitlinien zu öffentlicher Debatte, Werturteil, Tatsachengrundlage, Art.-8-/Art.-10-Abwägung, Hyperlinks und Drittkommentaren |
| `eugh-grch-art-11-rechtsprechung` | EuGH/GRCh bei Plattformen, Suchmaschinen, Datenschutz, Uploadfiltern, De-Referenzierung und journalistischen Zwecken |
| `olg-kg-praxis-rechtsprechung` | Obergerichtliche Praxis zu Unterlassung, Sinnermittlung, Social Media, Verdachtsäußerung, Plattformlabel und Tenorrisiko |
| `rechtsvergleich-usa-supreme-court` | US-Supreme-Court-Vergleich zu First Amendment, actual malice, public concern, opinion, parody, threats und incitement |
| `beweissicherung-screenshots` | Screenshots, Metadaten, Zeugen, URLs, Löschungen, Chatverläufe |
| `risikomatrix-ampel` | Ergebnis als Grün/Gelb/Rot mit Unsicherheiten und nächstem Schritt |
| `gegendarstellung-entschuldigung-deeskalation` | Reaktionsoptionen ohne unnötige Eskalation |
| `abmahnung-strafanzeige-reaktion` | Eingang von Abmahnung, Strafanzeige, Anhörung oder Plattformmeldung bearbeiten |
| `schriftsatz-stellungnahme-verteidigung` | Verteidigungs- und Erwiderungsbausteine |
| `output-memo-pruefvermerk` | Dokumentierter Prüfvermerk mit Zitat, Kontext, Normen und Ergebnis |
| `testakte-auswertung` | Die Testakte strukturiert auswerten |
| `rechtsprechungsbank-verifiziert` | Verifizierte Rechtsprechung mit Datum, Aktenzeichen und freier Quelle |

## Quellenstand

Stand: 05/2026. Kernnormen: Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, §§ 185-188, 192-194 StGB, §§ 823, 824, 1004 BGB analog, § 22 KUG bei Bildern und DSA-Schnittstellen bei Plattformen. Leitentscheidungen sind im Skill `rechtsprechungsbank-verifiziert` dokumentiert; der USA-Vergleich ist ausdrücklich nur Vergleich, kein Import amerikanischer Standards in die deutsche Prüfung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-strafanzeige-reaktion` | Hilft bei Reaktion auf Abmahnung, Strafanzeige, polizeiliche Anhörung, Plattformmeldung oder Löschungsverlangen wegen einer Äußerung. Erstellt Fristencheck, Beweisplan und Verteidigungsstrategie im Meinungspruefer: prüft konkret die eins... |
| `abwaegung-art-arbeitgeber-betrieb` | Erstellt die verfassungsrechtliche Normalabwägung zwischen Meinungsfreiheit und Persönlichkeitsrecht. Berücksichtigt Sachbezug, Machtkritik, Anlass, Form, Reichweite, Wiederholung, Prangerwirkung und Beleglage im Meinungspruefer: prüft k... |
| `aeusserungsrecht-tatbestand-beweis-und-belege` | Aeusserungsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die e... |
| `arbeitgeber-betrieb-kantine` | Prüft Äußerungen im Betrieb, in der Kantine, im Kollegenkreis, gegenüber Arbeitgeber, Betriebsrat oder auf LinkedIn. Verbindet Ehrschutz, Meinungsfreiheit, arbeitsrechtliche Nebenpflichten und Eskalationsrisiko im Meinungspruefer: prüft... |
| `beleglage-tatsachenbehauptung-beweissicherung` | Erstellt eine Belegmatrix für Tatsachenbehauptungen, Verdachtsäußerungen und gemischte Äußerungen. Prüft Wahrheit, Beweisbarkeit, Nichterweislichkeit, bewusste Unwahrheit, Quellenqualität und Dokumentationsbedarf im Meinungspruefer: prüf... |
| `beleidigung-meinungspruefer` | Beleidigung: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die ei... |
| `beweissicherung-screenshots` | Erstellt einen Beweissicherungsplan für Screenshots, URLs, Zeitstempel, Chatverläufe, Zeugen, Metadaten, Löschungen und Exportdateien. Geeignet für Social Media, Messenger, E-Mail und Bewertungsportale im Meinungspruefer: prüft konkret d... |
| `chronologie-fristen` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `egmr-art-eugh-grch` | Prüft Äußerungsfälle mit der EGMR-Linie zu Art 10 EMRK: öffentlicher Diskurs, Werturteil, Tatsachengrundlage, Reputation, Amtsträger, Anwälte, Hyperlinks und Plattformkommentare im Meinungspruefer: prüft konkret die einschlägigen Tatbest... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `eugh-grch-art-11-rechtsprechung` | Prüft EuGH- und Art 11 GRCh-Bezüge bei Äußerungen: Plattformen, Suchmaschinen, Datenschutz, Uploadfilter, De-Referenzierung, journalistische Zwecke und Informationsfreiheit im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsm... |
| `europarecht-emrk-gegendarstellung` | Ordnet Art 10 EMRK und Art 11 GRCh in die Äußerungsprüfung ein. Prüft scharfe Äußerungen, Reputationsschutz, Plattformen, Suchmaschinen, Datenschutz, Verhältnismäßigkeit und unionsrechtliche Bezüge im Meinungspruefer: prüft konkret die e... |
| `gegendarstellung-entschuldigung-deeskalation` | Entwickelt Reaktionsoptionen bei eskalierten Äußerungen: Klarstellung, Entschuldigung, Löschung, Gegendarstellung, Antwort, Gesprächsangebot und Vergleich ohne unnötiges Schuldanerkenntnis im Meinungspruefer: prüft konkret die einschlägi... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Meinungsprüfer. Fragt Wortlaut, Kontext, Medium, Publikum, Tatsachenkern, Belege, betroffene Person, Anlass, Vorgeschichte, gewünschtes Ziel und Risiko ab; schlägt passende Fachmodule zu Beleidi... |
| `kommunalrecht-buergermeister-machtkritik` | Prüft kommunale Meinungsfälle um Bürgermeister, Rat, Verwaltung und Bauprojekte. Fokussiert öffentliche Sachdebatte, Amtsrolle, § 188 StGB, scharfe Bürgerkritik, Versammlung und lokale Öffentlichkeit im Meinungspruefer: prüft konkret die... |
| `machtkritik-amtstraeger` | Prüft Kritik an Amtsträgern, Behörden, Schulleitung, Bürgermeister, Justiz und Verwaltung. Gewichtet Machtkritik, Sachbezug, Amtsrolle, private Sphäre, Öffentlichkeit, § 188 StGB und Art 5 GG im Meinungspruefer: prüft konkret die einschl... |
| `mehrdeutigkeit-sinnermittlung-meinung` | Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung nach Wortlaut, Kontext, Begleitumständen und Durchschnittspublikum. Prüft, ob nicht ehrverletzende Deutungen tragfähig ausgeschlossen werden können im Meinungspruefer: prüft konkr... |
| `meinung-strafantrag-verfahren` | Meinung: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschlägigen T... |
| `meinung-tatsache-abgrenzung` | Prüft, ob eine Äußerung Meinung, Tatsachenbehauptung, gemischte Äußerung, Verdachtsäußerung, Frage oder Satire ist. Schützt die Meinungsfreiheit vor falscher Tatsachenschublade und verlangt Belege nur dort, wo Tatsachen behauptet werden... |
| `meinungspruefer-erstpruefung-und-mandatsziel` | Meinungspruefer: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschl... |
| `nachrede-tatsache` | Nachrede: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschlägigen Tat... |
| `olg-kg-rechtsprechungsbank-verifiziert` | Nutzt obergerichtliche Praxis zu Äußerungen: OLG Frankfurt, OLG München, OLG Köln, OLG Düsseldorf, KG Berlin, Social Media, Unterlassung und Sinnermittlung im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `output-memo-pruefvermerk` | Erzeugt den finalen Prüfvermerk zum Meinungsfall mit Sachverhalt, Wortlaut, Kontext, Normen, Rechtsprechung, Subsumtion, Risikoampel, Belegliste, Alternativformulierungen und Handlungsempfehlung. |
| `personen-politisches-presserecht-plattformen` | Prüft § 188 StGB bei Äußerungen gegen Personen des politischen Lebens. Klärt Öffentlichkeit, Zusammenhang mit Stellung, Eignung zur Erschwerung öffentlichen Wirkens und die verfassungsrechtliche Machtkritik im Meinungspruefer: prüft konk... |
| `presserecht-plattformen-loeschung-dsa` | Prüft Medien- und Plattformfälle mit Löschung, Sperrung, Meldung, Bewertungsportal, DSA-Schnittstelle, Notice-and-Action, Gegendarstellung, Antwort und Beweissicherung im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkma... |
| `rechtsprechungsbank-verifiziert` | Enthält eine verifizierte Rechtsprechungsbank zur Meinungsfreiheit und Ehrschutzprüfung mit Gericht, Datum, Aktenzeichen und freier Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate im Meinungspruefer: prüft konkret die einschlä... |
| `rechtsvergleich-usa-risikomatrix-ampel` | Vergleicht deutsche Meinungsfreiheit mit der US-First-Amendment-Linie des Supreme Court: defamation, actual malice, opinion, parody, threats und incitement im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `risikomatrix-ampel` | Erzeugt eine verständliche Risikoampel für Äußerungen mit Strafrecht, Zivilrecht, Plattformrisiko, arbeits- oder schulbezogenem Risiko, Beleglage, Verteidigungslinie und empfohlenem nächsten Schritt im Meinungspruefer: prüft konkret die... |
| `satire-ironisierung-schimpfwort-lackaffe` | Prüft satirische, ironische und bildhafte Äußerungen wie Pinocchio-Vergleiche. Trennt Lügenvorwurf, gebrochene Zusage, Werturteil, Tatsachenkern, Bildsprache, Publikum und Kontext im Meinungspruefer: prüft konkret die einschlägigen Tatbe... |
| `schimpfwort-lackaffe-und-spott` | Prüft Spott- und Schimpfwörter wie Lackaffe im Kontext. Bewertet Sachbezug, Amtsrolle, Spontanität, Reichweite, Herabsetzungsgrad, Formalbeleidigung, Schmähkritik und Art 5 GG im Meinungspruefer: prüft konkret die einschlägigen Tatbestan... |
| `schmaehkritik-formalbeleidigung-schnelltriage` | Prüft die engen Ausnahmefälle Schmähkritik, Formalbeleidigung und Menschenwürdeangriff. Verhindert, dass Fachgerichte oder Nutzer die Art 5 GG Normalabwägung vorschnell abschneiden im Meinungspruefer: prüft konkret die einschlägigen Tatb... |
| `schnelltriage-aeusserung` | Schnelle Erstbewertung einer Äußerung mit Ampel für Strafrecht, Zivilrecht, Plattform, Arbeitsplatz, Schule und Öffentlichkeitsrisiko. Nutzt Wortlaut, Kontext, Medium, Reichweite, betroffene Person, Belege und Ziel der Nutzerin im Meinun... |
| `schule-elternchat` | Prüft Äußerungen über Lehrkräfte, Schulleitung und Eltern in Elternchat, Schulmail, Klassenpflegschaft und Beschwerde. Achtet auf Sachbezug, Kindesschutz, Amtsträgerrolle, Belege und Deeskalation im Meinungspruefer: prüft konkret die ein... |
| `soziale-medien-aeusserungsrecht` | Prüft Äußerungen auf X, LinkedIn, Bewertungsportalen und Kommentarspalten. Bewertet Reichweite, Dauerhaftigkeit, Tags, Bilder, Wiederholung, Prangerwirkung, Plattformregeln und Beweissicherung im Meinungspruefer: prüft konkret die einsch... |
| `stellungnahme-verteidigung-schule-elternchat` | Erstellt strukturierte Stellungnahmen und Verteidigungsbausteine zu Äußerungsvorwürfen. Nutzt Sinnermittlung, Meinung-Tatsache-Abgrenzung, Art 5 GG, § 193 StGB, Belegmatrix und Rechtsprechungsbank im Meinungspruefer: prüft konkret die ei... |
| `stgb-quellenkarte` | Stgb Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `strafantrag-194-und-verfahren` | Prüft Strafantrag, Fristen, Antragsberechtigung, öffentliches Interesse, Privatklage, Einstellungsmöglichkeiten, Anhörung als Beschuldigter und taktische Reaktion bei Ehrdelikten im Meinungspruefer: prüft konkret die einschlägigen Tatbes... |
| `strafrecht-beleidigung-testakte-auswertung` | Prüft § 185 StGB bei ehrverletzenden Werturteilen und Schimpfworten mit Art 5 GG. Zwingt Sinnermittlung, Kontext, Sachbezug, Formalbeleidigung, Schmähkritik, Menschenwürde und Normalabwägung im Meinungspruefer: prüft konkret die einschlä... |
| `tatsache-dokumentenmatrix-und-lueckenliste` | Tatsache: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschläg... |
| `testakte-auswertung` | Wertet die Testakte meinungspruefer-grenzfaelle-alltag aus. Sortiert X, LinkedIn, Kantine, Schule, Arbeitgeber, Bürgermeister, Lackaffe, Pinocchio und Tatsachenbelege in getrennte Prüfstränge im Meinungspruefer: prüft konkret die einschl... |
| `ueble-nachrede-verleumdung` | Prüft § 186 StGB bei ehrenrührigen Tatsachenbehauptungen, die nicht erweislich wahr sind. Trennt Tatsachenkern, Beweislast, Verdachtsäußerung, Öffentlichkeit, § 188 StGB und Art 5 GG im Meinungspruefer: prüft konkret die einschlägigen Ta... |
| `ueble-verleumdung` | Ueble: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschlägigen Tatbesta... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verleumdung-187` | Prüft § 187 StGB bei bewusst unwahren ehrverletzenden Tatsachenbehauptungen. Fokussiert Wissen um Unwahrheit, Beweisstand, Rufschädigung, Öffentlichkeitswirkung und zivilrechtliche Anschlussrisiken im Meinungspruefer: prüft konkret die e... |
| `verleumdung-verhandlung-vergleich-und-eskalation` | Verleumdung: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Meinungspruefer: prüft konkret die einschlägigen Ta... |
| `wahrnehmung-berechtigter-zitat` | Prüft § 193 StGB bei Beschwerde, Bewertung, Anzeige, arbeitsbezogener Kritik, Mandatskonflikt, Schulstreit und sonstiger Interessenwahrnehmung. Verbindet Sachbezug, Erforderlichkeit, Form und Art 5 GG im Meinungspruefer: prüft konkret di... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pr... |
| `zitat-und-kontextaufnahme` | Erfasst den exakten Wortlaut, Screenshot-Kontext, Medium, Adressatenkreis, Anlass, Vorgeschichte, zeitliche Abfolge, Wiederholung, Sichtbarkeit und Ziel der Äußerung. Grundlage für jede Äußerungsprüfung im Meinungspruefer: prüft konkret... |
| `zivilrecht-unterlassung-abmahnung` | Prüft zivilrechtliche Ansprüche bei Äußerungen: Unterlassung, Beseitigung, Widerruf, Richtigstellung, Geldentschädigung, § 823 BGB, § 824 BGB und § 1004 BGB analog im Meinungspruefer: prüft konkret die einschlägigen Tatbestandsmerkmale,... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
