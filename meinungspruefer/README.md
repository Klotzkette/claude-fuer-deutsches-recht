# Meinungsprüfer

Freistehendes Plugin für die Prüfung von Äußerungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung oder Tatsachenbehauptung, Beleidigung, üble Nachrede, Verleumdung, Personen des politischen Lebens, Wahrnehmung berechtigter Interessen, zivilrechtliche Unterlassung, Widerruf, Geldentschädigung, Plattform- und Social-Media-Kontext, EGMR/EuGH/GRCh, OLG-/KG-Praxis und US-Supreme-Court-Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt eine strukturierte Vorprüfung und dokumentierbare Arbeitsprodukte zur anwaltlichen Kontrolle. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet.

## Direkt-Download

| Plugin | Direkt-Download |
|---|---|
| Meinungsprüfer (`meinungspruefer`) | [meinungspruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |

## Start

```
/meinungspruefer:allgemein
```

Der Einstieg fragt schnell ab: exakter Wortlaut, Medium, Publikum, Anlass, Vorgeschichte, Betroffene, Tatsachenkern, Belege, Wiederholungsgefahr, gewünschter Output und Risikotoleranz. Danach routet er zu den passenden Spezialskills.

## Skills (36)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Schnelltriage, Quellenhygiene und Routing |
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

## Testakte

Die Testakte [`meinungspruefer-grenzfaelle-alltag`](../testakten/meinungspruefer-grenzfaelle-alltag/) enthält mehrere lebensnahe Grenzfälle ohne parteipolitische Zuspitzung: ein X-Post über ein Bauprojekt, ein LinkedIn-Kommentar über Projektleitung, ein Kantinengespräch im Betrieb, ein Elternchat zur Schulleitung, eine kommunale Bürgerversammlung mit dem Begriff "Lackaffe", ein Pinocchio-Vergleich, eine unsaubere Tatsachenbehauptung mit lückenhafter Beleglage und eine interne Notiz zum USA-Vergleich.

Direkt-Download der Akte: [testakte-meinungspruefer-grenzfaelle-alltag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-meinungspruefer-grenzfaelle-alltag.zip)

## Quellenstand

Stand: 05/2026. Kernnormen: Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, §§ 185-188, 192-194 StGB, §§ 823, 824, 1004 BGB analog, § 22 KUG bei Bildern und DSA-Schnittstellen bei Plattformen. Leitentscheidungen sind im Skill `rechtsprechungsbank-verifiziert` dokumentiert; der USA-Vergleich ist ausdrücklich nur Vergleich, kein Import amerikanischer Standards in die deutsche Prüfung.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 36 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-strafanzeige-reaktion` | Hilft bei Reaktion auf Abmahnung, Strafanzeige, polizeiliche Anhörung, Plattformmeldung oder Löschungsverlangen wegen einer Äußerung. Erstellt Fristencheck, Beweisplan und Verteidigungsstrategie. |
| `abwaegung-art-5-gg` | Erstellt die verfassungsrechtliche Normalabwägung zwischen Meinungsfreiheit und Persönlichkeitsrecht. Berücksichtigt Sachbezug, Machtkritik, Anlass, Form, Reichweite, Wiederholung, Prangerwirkung und Beleglage. |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Meinungsprüfer. Fragt Wortlaut, Kontext, Medium, Publikum, Tatsachenkern, Belege, betroffene Person, Anlass, Vorgeschichte, gewünschtes Ziel und Risiko ab; schlägt passende Spezial-Skills z... |
| `arbeitgeber-betrieb-kantine` | Prüft Äußerungen im Betrieb, in der Kantine, im Kollegenkreis, gegenüber Arbeitgeber, Betriebsrat oder auf LinkedIn. Verbindet Ehrschutz, Meinungsfreiheit, arbeitsrechtliche Nebenpflichten und Eskalationsrisiko. |
| `beleglage-tatsachenbehauptung` | Erstellt eine Belegmatrix für Tatsachenbehauptungen, Verdachtsäußerungen und gemischte Äußerungen. Prüft Wahrheit, Beweisbarkeit, Nichterweislichkeit, bewusste Unwahrheit, Quellenqualität und Dokumentationsbedarf. |
| `beweissicherung-screenshots` | Erstellt einen Beweissicherungsplan für Screenshots, URLs, Zeitstempel, Chatverläufe, Zeugen, Metadaten, Löschungen und Exportdateien. Geeignet für Social Media, Messenger, E-Mail und Bewertungsportale. |
| `egmr-art-10-rechtsprechung` | Prüft Äußerungsfälle mit der EGMR-Linie zu Art 10 EMRK: öffentlicher Diskurs, Werturteil, Tatsachengrundlage, Reputation, Amtsträger, Anwälte, Hyperlinks und Plattformkommentare. |
| `eugh-grch-art-11-rechtsprechung` | Prüft EuGH- und Art 11 GRCh-Bezüge bei Äußerungen: Plattformen, Suchmaschinen, Datenschutz, Uploadfilter, De-Referenzierung, journalistische Zwecke und Informationsfreiheit. |
| `europarecht-emrk-grch` | Ordnet Art 10 EMRK und Art 11 GRCh in die Äußerungsprüfung ein. Prüft scharfe Äußerungen, Reputationsschutz, Plattformen, Suchmaschinen, Datenschutz, Verhältnismäßigkeit und unionsrechtliche Bezüge. |
| `gegendarstellung-entschuldigung-deeskalation` | Entwickelt Reaktionsoptionen bei eskalierten Äußerungen: Klarstellung, Entschuldigung, Löschung, Gegendarstellung, Antwort, Gesprächsangebot und Vergleich ohne unnötiges Schuldanerkenntnis. |
| `kommunalrecht-buergermeister` | Prüft kommunale Meinungsfälle um Bürgermeister, Rat, Verwaltung und Bauprojekte. Fokussiert öffentliche Sachdebatte, Amtsrolle, § 188 StGB, scharfe Bürgerkritik, Versammlung und lokale Öffentlichkeit. |
| `machtkritik-amtstraeger` | Prüft Kritik an Amtsträgern, Behörden, Schulleitung, Bürgermeister, Justiz und Verwaltung. Gewichtet Machtkritik, Sachbezug, Amtsrolle, private Sphäre, Öffentlichkeit, § 188 StGB und Art 5 GG. |
| `mehrdeutigkeit-sinnermittlung` | Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung nach Wortlaut, Kontext, Begleitumständen und Durchschnittspublikum. Prüft, ob nicht ehrverletzende Deutungen tragfähig ausgeschlossen werden können. |
| `meinung-tatsache-abgrenzung` | Prüft, ob eine Äußerung Meinung, Tatsachenbehauptung, gemischte Äußerung, Verdachtsäußerung, Frage oder Satire ist. Schützt die Meinungsfreiheit vor falscher Tatsachenschublade und verlangt Belege nur dort, wo Tatsachen behauptet werden. |
| `olg-kg-praxis-rechtsprechung` | Nutzt obergerichtliche Praxis zu Äußerungen: OLG Frankfurt, OLG München, OLG Köln, OLG Düsseldorf, KG Berlin, Social Media, Unterlassung und Sinnermittlung. |
| `output-memo-pruefvermerk` | Erzeugt den finalen Prüfvermerk zum Meinungsfall mit Sachverhalt, Wortlaut, Kontext, Normen, Rechtsprechung, Subsumtion, Risikoampel, Belegliste, Alternativformulierungen und Handlungsempfehlung. |
| `personen-politisches-leben-188` | Prüft § 188 StGB bei Äußerungen gegen Personen des politischen Lebens. Klärt Öffentlichkeit, Zusammenhang mit Stellung, Eignung zur Erschwerung öffentlichen Wirkens und die verfassungsrechtliche Machtkritik. |
| `presserecht-plattformen-loeschung-dsa` | Prüft Medien- und Plattformfälle mit Löschung, Sperrung, Meldung, Bewertungsportal, DSA-Schnittstelle, Notice-and-Action, Gegendarstellung, Antwort und Beweissicherung. |
| `rechtsprechungsbank-verifiziert` | Enthält eine verifizierte Rechtsprechungsbank zur Meinungsfreiheit und Ehrschutzprüfung mit Gericht, Datum, Aktenzeichen und freier Quelle. Keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. |
| `rechtsvergleich-usa-supreme-court` | Vergleicht deutsche Meinungsfreiheit mit der US-First-Amendment-Linie des Supreme Court: defamation, actual malice, opinion, parody, threats und incitement. |
| `risikomatrix-ampel` | Erzeugt eine verständliche Risikoampel für Äußerungen mit Strafrecht, Zivilrecht, Plattformrisiko, arbeits- oder schulbezogenem Risiko, Beleglage, Verteidigungslinie und empfohlenem nächsten Schritt. |
| `satire-ironisierung-pinocchio` | Prüft satirische, ironische und bildhafte Äußerungen wie Pinocchio-Vergleiche. Trennt Lügenvorwurf, gebrochene Zusage, Werturteil, Tatsachenkern, Bildsprache, Publikum und Kontext. |
| `schimpfwort-lackaffe-und-spott` | Prüft Spott- und Schimpfwörter wie Lackaffe im Kontext. Bewertet Sachbezug, Amtsrolle, Spontanität, Reichweite, Herabsetzungsgrad, Formalbeleidigung, Schmähkritik und Art 5 GG. |
| `schmaehkritik-formalbeleidigung-menschenwuerde` | Prüft die engen Ausnahmefälle Schmähkritik, Formalbeleidigung und Menschenwürdeangriff. Verhindert, dass Fachgerichte oder Nutzer die Art 5 GG Normalabwägung vorschnell abschneiden. |
| `schnelltriage-aeusserung` | Schnelle Erstbewertung einer Äußerung mit Ampel für Strafrecht, Zivilrecht, Plattform, Arbeitsplatz, Schule und Öffentlichkeitsrisiko. Nutzt Wortlaut, Kontext, Medium, Reichweite, betroffene Person, Belege und Ziel der Nutzerin. |
| `schriftsatz-stellungnahme-verteidigung` | Erstellt strukturierte Stellungnahmen und Verteidigungsbausteine zu Äußerungsvorwürfen. Nutzt Sinnermittlung, Meinung-Tatsache-Abgrenzung, Art 5 GG, § 193 StGB, Belegmatrix und Rechtsprechungsbank. |
| `schule-elternchat` | Prüft Äußerungen über Lehrkräfte, Schulleitung und Eltern in Elternchat, Schulmail, Klassenpflegschaft und Beschwerde. Achtet auf Sachbezug, Kindesschutz, Amtsträgerrolle, Belege und Deeskalation. |
| `soziale-medien-x-linkedin` | Prüft Äußerungen auf X, LinkedIn, Bewertungsportalen und Kommentarspalten. Bewertet Reichweite, Dauerhaftigkeit, Tags, Bilder, Wiederholung, Prangerwirkung, Plattformregeln und Beweissicherung. |
| `strafantrag-194-und-verfahren` | Prüft Strafantrag, Fristen, Antragsberechtigung, öffentliches Interesse, Privatklage, Einstellungsmöglichkeiten, Anhörung als Beschuldigter und taktische Reaktion bei Ehrdelikten. |
| `strafrecht-185-beleidigung` | Prüft § 185 StGB bei ehrverletzenden Werturteilen und Schimpfworten mit Art 5 GG. Zwingt Sinnermittlung, Kontext, Sachbezug, Formalbeleidigung, Schmähkritik, Menschenwürde und Normalabwägung. |
| `testakte-auswertung` | Wertet die Testakte meinungspruefer-grenzfaelle-alltag aus. Sortiert X, LinkedIn, Kantine, Schule, Arbeitgeber, Bürgermeister, Lackaffe, Pinocchio und Tatsachenbelege in getrennte Prüfstränge. |
| `ueble-nachrede-186` | Prüft § 186 StGB bei ehrenrührigen Tatsachenbehauptungen, die nicht erweislich wahr sind. Trennt Tatsachenkern, Beweislast, Verdachtsäußerung, Öffentlichkeit, § 188 StGB und Art 5 GG. |
| `verleumdung-187` | Prüft § 187 StGB bei bewusst unwahren ehrverletzenden Tatsachenbehauptungen. Fokussiert Wissen um Unwahrheit, Beweisstand, Rufschädigung, Öffentlichkeitswirkung und zivilrechtliche Anschlussrisiken. |
| `wahrnehmung-berechtigter-interessen-193` | Prüft § 193 StGB bei Beschwerde, Bewertung, Anzeige, arbeitsbezogener Kritik, Mandatskonflikt, Schulstreit und sonstiger Interessenwahrnehmung. Verbindet Sachbezug, Erforderlichkeit, Form und Art 5 GG. |
| `zitat-und-kontextaufnahme` | Erfasst den exakten Wortlaut, Screenshot-Kontext, Medium, Adressatenkreis, Anlass, Vorgeschichte, zeitliche Abfolge, Wiederholung, Sichtbarkeit und Ziel der Äußerung. Grundlage für jede Äußerungsprüfung. |
| `zivilrecht-unterlassung-widerruf-schadensersatz` | Prüft zivilrechtliche Ansprüche bei Äußerungen: Unterlassung, Beseitigung, Widerruf, Richtigstellung, Geldentschädigung, § 823 BGB, § 824 BGB und § 1004 BGB analog. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
