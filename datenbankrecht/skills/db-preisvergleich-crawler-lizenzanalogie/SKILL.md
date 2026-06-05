---
name: db-preisvergleich-crawler-lizenzanalogie
description: "DB Preisvergleich Crawler Lizenzanalogie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Preisvergleich Crawler Lizenzanalogie

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Preisvergleich Crawler Lizenzanalogie** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-016-preisvergleich-crawler-und-plattformvertrag` | Datenbankrecht für Preisvergleichsportale und deren Crawler: Prüft §§ 87a-87e UrhG gegen automatisierte Preisabfragen, Wirksamkeit von AGB-Scraping-Verboten (§ 307 BGB), EuGH C-202/12 (Innoweb/Wegener) und P2B-VO 2019/1150. Bewertet Plattformverträge mit Händlern und Datenlieferanten sowie Unterlassungsansprüche gegen Preisvergleichs-Crawler. |
| `db-030-lizenzanalogie-und-unterlassungsvertrag` | Lizenzanalogie und Unterlassungsvertragsgestaltung im Datenbankrecht: Berechnung der Lizenzanalogie nach § 97 Abs. 2 UrhG für Datenbankherstellerrechts-Verletzungen, Unterlassungsvertrags-Klauseln (Vertragsstrafe nach § 339 BGB) als Alternative zur Klage und Abgrenzung von Abschlusserklärung zu titulierter Unterlassung. Erstellt Vertragsstrafe-Klausel und Berechnungsmodell. |
| `db-032-datenbankrecht-und-urhebervertragsrecht` | Datenbankrecht im Urhebervertragsrecht: §§ 31-44 UrhG für Datenbankwerke (§ 4 Abs. 2 UrhG) — Einräumung und Rückruf von Nutzungsrechten, angemessene Vergütung (§ 32 UrhG), Bestseller-Klausel (§ 32a UrhG) und Verlagsrecht. Abgrenzung zur Übertragung des Datenbankherstellerrechts (§ 87a Abs. 2 UrhG). Erstellt Nutzungsrechtsklauseln für Datenbankverträge. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Preisvergleich Crawler Lizenzanalogie**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-016-preisvergleich-crawler-und-plattformvertrag`

**Fokus:** Datenbankrecht für Preisvergleichsportale und deren Crawler: Prüft §§ 87a-87e UrhG gegen automatisierte Preisabfragen, Wirksamkeit von AGB-Scraping-Verboten (§ 307 BGB), EuGH C-202/12 (Innoweb/Wegener) und P2B-VO 2019/1150. Bewertet Plattformverträge mit Händlern und Datenlieferanten sowie Unterlassungsansprüche gegen Preisvergleichs-Crawler.

# Preisvergleich-Crawler und Plattformverträge — Datenbankrecht und P2B

## Mandantenfall

- Online-Händler findet seine Preise auf einem Preisvergleichsportal, das keinen Vertrag mit ihm hat, und fragt, ob er dagegen vorgehen kann.
- Plattformbetreiber will Crawler-Verbote in seinen AGB verankern und Preisvergleichsportalen den Zugang sperren.
- Preisvergleichsportal-Betreiber fragt, ob er rechtlich verpflichtet ist, Händlerdaten auf Anfrage bereitzustellen (P2B-VO) und wie er die eigene Datenbank schützen kann.

## Erste Schritte

1. Datenbankschutz der Zielplattform prüfen: Hat der Online-Marktplatz oder Händler eine Datenbank mit wesentlicher Investition in Beschaffung und Darstellung von Preisen?
2. AGB-Crawler-Verbot analysieren: Ist das Verbot klar formuliert, wirksam einbezogen und nach § 307 BGB nicht unangemessen benachteiligend?
3. EuGH Innoweb/Wegener anwenden: Systematische Echtzeitabfrage der Zieldatenbank als verbotene Weiterverwendung nach Art. 7 RL 96/9/EG?
4. P2B-VO prüfen: Gilt die Plattform-zu-Business-Verordnung 2019/1150 — welche Transparenz- und Nicht-Diskriminierungspflichten bestehen?
5. Wettbewerbsrecht klären: Gezielte Behinderung nach § 4 Nr. 4 UWG oder Marktmissbrauch bei marktbeherrschender Stellung?
6. Gegenseitige Schutzstrategie entwickeln: Wie schützt das Preisvergleichsportal seine eigene aggregierte Datenbank?

## Rechtsrahmen

- § 87a UrhG: Datenbankherstellerrecht für Preisdatenbanken auf Online-Marktplätzen.
- § 87b UrhG: Wesentliche Entnahme von Preisdaten aus Händlerdatenbanken.
- EuGH C-202/12 (Innoweb/Wegener): Meta-Suchmaschine, die Fremddatenbanken in Echtzeit durchsucht, verwendet wesentliche Teile weiter.
- P2B-VO 2019/1150: Pflichten von Online-Vermittlungsdiensten gegenüber gewerblichen Nutzern — Transparenz, Ranking-Erklärung.
- § 307 BGB: AGB-Kontrolle für Crawler-Verbote — transparente Formulierung und verhältnismäßige Rechtsfolgen erforderlich.
- § 4 Nr. 4 UWG: Gezielte Behinderung — Daten-Scraping als unfaire Wettbewerbshandlung.

## Prüfraster

- Hat der angegriffene Plattformbetreiber wesentliche Investitionen in seine Preisdatenbank getätigt?
- Führt der Preisvergleichs-Crawler eine Echtzeitabfrage durch, die funktional einer Suche in der Fremddatenbank entspricht (Innoweb-Test)?
- Ist das AGB-Crawler-Verbot wirksam einbezogen, hinreichend bestimmt und kein Verstoß gegen § 307 BGB?
- Kumuliert der Crawler durch viele Einzelabfragen eine wesentliche Gesamtentnahme (§ 87b Abs. 1 S. 2 UrhG)?
- Ist der Plattformbetreiber nach P2B-VO verpflichtet, den Preisvergleichsdienst nicht zu diskriminieren?
- Schützt die eigene Datenbank des Preisvergleichsportals (aggregierte Preishistorien) eigenes Herstellerrecht?
- Besteht kartellrechtliches Risiko, wenn Plattform mit marktbeherrschender Stellung den Zugang verweigert?

## Typische Fallstricke

- AGB-Crawler-Verbote ohne explizite Einbeziehung im Onboarding-Prozess sind gegenüber gewerblichen Nutzern oft unwirksam.
- P2B-VO kann bei marktbeherrschenden Plattformen den Datenzugang für Preisvergleichsdienste erzwingen — kartellrechtliche Dimension.
- Händler, die Produktdaten an die Plattform übermitteln, behalten eigene Rechte an ihren Preisangaben — keine vollständige Übertragung.
- Innoweb-Entscheidung gilt für Echtzeitsuche; reine Archivabfragen könnten anders bewertet werden.
- Schadensberechnung bei unerlaubtem Crawling schwierig — Lizenzanalogie (§ 97 Abs. 2 UrhG) als Methode.

## Output

- Rechtsgutachten Crawler-Verbot (§ 87b UrhG + AGB + UWG)
- AGB-Crawler-Klausel-Vorlage (§ 307 BGB-konform)
- P2B-VO-Compliance-Check für Plattformbetreiber
- Unterlassungsschreiben gegen Preisvergleichsportal
- Eigener Datenbankschutz-Aufbauplan für Preisvergleichsdienst

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [P2B-VO 2019/1150 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R1150)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 4 UWG — dejure.org](https://dejure.org/gesetze/UWG/4.html)
- [Art. 7 RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## 2. `db-030-lizenzanalogie-und-unterlassungsvertrag`

**Fokus:** Lizenzanalogie und Unterlassungsvertragsgestaltung im Datenbankrecht: Berechnung der Lizenzanalogie nach § 97 Abs. 2 UrhG für Datenbankherstellerrechts-Verletzungen, Unterlassungsvertrags-Klauseln (Vertragsstrafe nach § 339 BGB) als Alternative zur Klage und Abgrenzung von Abschlusserklärung zu titulierter Unterlassung. Erstellt Vertragsstrafe-Klausel und Berechnungsmodell.

# Lizenzanalogie und Unterlassungsvertrag im Datenbankrecht

## Mandantenfall

- Verletzer hat nach Abmahnung eine Unterlassungserklärung abgegeben — Datenbankbetreiber fragt, ob die Vertragsstrafe angemessen und vollstreckbar ist.
- Datenbankbetreiber möchte außergerichtlich einigen und verhandelt über einen Vergleich — wie wird die Lizenzanalogie berechnet und im Vergleich abgebildet?
- Anwalt muss entscheiden, ob Unterlassungsklage oder modifizierte Unterlassungserklärung die bessere Absicherung für seinen Mandanten bietet.

## Erste Schritte

1. Lizenzanalogie berechnen: Übliche Lizenzgebühr für die Nutzung des verletzten Datenbankherstellerrechts ermitteln — eigene Lizenzpraxis, Marktpreise, Vergleichslizenzverträge.
2. Unterlassungserklärung prüfen: Ist sie hinreichend bestimmt, zeitlich unbegrenzt und enthält eine angemessene Vertragsstrafe (§ 339 BGB)?
3. Vertragsstrafe-Höhe festlegen: Hamburger Brauch (nach billigem Ermessen des Gläubigers) oder konkrete Summe? Verhältnismäßigkeit nach § 340 BGB prüfen.
4. Wiederholungsgefahr-Beseitigung bewerten: Beseitigt die Unterlassungserklärung die Wiederholungsgefahr vollständig — ist ein Unterlassungsurteil noch nötig?
5. Vergleich gestalten: Lizenzgebühr für Vergangenheit, Unterlassungsverpflichtung für Zukunft, ggf. Lizenzvertrag für zukünftige Nutzung.
6. Modifizierte Unterlassungserklärung: Welche Einschränkungen des Verletzers sind akzeptabel — muss der Gläubiger widersprechen?

## Rechtsrahmen

- § 97 Abs. 2 S. 3 UrhG: Lizenzanalogie — als Schaden gilt auch die fiktive Lizenzgebühr, die bei erlaubter Nutzung angefallen wäre.
- § 339 BGB: Vertragsstrafenklausel — Vertragsstrafe bei Verstoß gegen Unterlassungserklärung; Hamburger Brauch oder Festsumme.
- § 340 BGB: Herabsetzung unverhältnismäßig hoher Vertragsstrafen durch Gericht.
- § 97a UrhG: Abmahnung als Voraussetzung für Erstattung von Rechtsanwaltsgebühren; Unterlassungserklärung beendet Wiederholungsgefahr.
- § 87b UrhG: Verletzungstatbestand als Grundlage der Unterlassungs- und Lizenzanalogie-Ansprüche.
- § 890 ZPO: Vollstreckung von Unterlassungsurteilen — Ordnungsgeld bis 250.000 EUR oder Ordnungshaft.

## Prüfraster

- Liegt eine genau bezifferte oder zumindest bestimmbare übliche Lizenzgebühr für die verletzten Datenbankteile vor?
- Ist die Unterlassungserklärung hinreichend bestimmt — erfasst sie alle Verletzungshandlungen und Varianten?
- Ist die Vertragsstrafe-Höhe angemessen und nicht so hoch, dass das Gericht sie nach § 340 BGB herabsetzen würde?
- Beseitigt die Erklärung die Wiederholungsgefahr vollständig, sodass eine Unterlassungsklage entbehrlich wird?
- Nimmt der Gläubiger die modifizierte Unterlassungserklärung an — oder muss er widersprechen und klagen?
- Sind Vergleichsverhandlungen über Lizenzgebühren für Vergangenheit und Zukunft sinnvoll?
- Besteht Strafklausel für den Fall weiterer Verletzungen nach der Unterlassungserklärung?

## Typische Fallstricke

- Zu eng gefasste Unterlassungserklärung lässt Umgehungsmöglichkeiten — Gläubiger kann auf vollständigem Rechtsschutz bestehen.
- Hamburger Brauch bei der Vertragsstrafe gibt dem Verletzer Rechtsunsicherheit — zu niedrige Strafe entfaltet keine abschreckende Wirkung.
- Lizenzanalogie ohne Nachweis der üblichen Lizenzgebühr führt zu unsicherer Vergleichsverhandlung.
- Modifizierte Unterlassungserklärung muss innerhalb kurzer Frist angenommen oder abgelehnt werden — prozessuale Fristen beachten.
- Vergleich über Vergangenheit schließt Schadensersatzansprüche für den vereinbarten Zeitraum ab — Restansprüche sichern.

## Output

- Lizenzanalogie-Berechnungsmodell (Marktpreisanalyse, eigene Lizenzpraxis)
- Unterlassungserklärung-Muster mit Vertragsstrafe (Hamburger Brauch und Festsumme-Variante)
- Vertragsstrafe-Verhältnismäßigkeitsprüfung nach § 340 BGB
- Vergleichsvertrag-Muster (Lizenzgebühr + Unterlassung + Lizenz)
- Modifizierte Unterlassungserklärung — Annahme/Ablehnung-Entscheidungsmatrix

## Quellen

- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 339 BGB — dejure.org](https://dejure.org/gesetze/BGB/339.html)
- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 890 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/890.html)
- [§ 340 BGB — dejure.org](https://dejure.org/gesetze/BGB/340.html)

## 3. `db-032-datenbankrecht-und-urhebervertragsrecht`

**Fokus:** Datenbankrecht im Urhebervertragsrecht: §§ 31-44 UrhG für Datenbankwerke (§ 4 Abs. 2 UrhG) — Einräumung und Rückruf von Nutzungsrechten, angemessene Vergütung (§ 32 UrhG), Bestseller-Klausel (§ 32a UrhG) und Verlagsrecht. Abgrenzung zur Übertragung des Datenbankherstellerrechts (§ 87a Abs. 2 UrhG). Erstellt Nutzungsrechtsklauseln für Datenbankverträge.

# Datenbankrecht und Urhebervertragsrecht — Nutzungsrechte für Datenbankwerke

## Mandantenfall

- Freiberuflicher Datenbankentwickler hat im Auftrag eine Datenbankstruktur erschaffen und streitet mit dem Auftraggeber darüber, wer Rechteinhaber ist und ob Nutzungsrechte eingeräumt wurden.
- Verlag hat einer Redakteurin die Erstellung einer Fachdatenbank beauftragt und fragt, ob er alle Nutzungsrechte ohne separaten Vertrag innehat.
- Startup überarbeitet seine Datenbankstruktur und fragt, ob der Ursprungs-Entwickler Rückrufrechte nach § 41 UrhG geltend machen kann.

## Erste Schritte

1. Urheberschaft am Datenbankwerk klären: Wer hat die schöpferische Auswahl oder Anordnung vorgenommen (§ 4 Abs. 2 UrhG) — Auftraggeber oder Auftragnehmer?
2. Nutzungsrechtseinräumung prüfen: Wurden Nutzungsrechte vertraglich eingeräumt (§ 31 UrhG) — ausschließlich oder einfach, zeitlich und räumlich?
3. Arbeitnehmerurheberrecht prüfen: § 43 UrhG — Arbeitgeber erhält Nutzungsrechte durch Arbeitsvertrag; gilt nicht für echte Auftragswerke.
4. Vergütungsangemessenheit prüfen: § 32 UrhG — angemessene Vergütung; Bestseller-Klausel (§ 32a UrhG) bei unerwartetem Erfolg.
5. Rückrufrecht prüfen: § 41 UrhG — Nichtausübung des eingeräumten Rechts über 2 Jahre; § 42 UrhG — gewandelte Überzeugung (selten bei Datenbanken).
6. Datenbankherstellerrecht vs. Urheberrecht trennen: § 87a Abs. 2 UrhG — Herstellerrecht ist übertragbar; Urheberrecht am Datenbankwerk ist unveräußerlich (§ 29 UrhG).

## Rechtsrahmen

- § 4 Abs. 2 UrhG: Datenbankwerk als urheberrechtlich schutzfähiges Werk — schöpferische Auswahl oder Anordnung.
- § 31 UrhG: Einräumung von Nutzungsrechten — ausschließlich oder einfach, zeitlich, räumlich, inhaltlich.
- § 43 UrhG: Arbeitnehmerurheberrecht — Arbeitgeber erhält Nutzungsrechte im Rahmen des Arbeitsverhältnisses.
- § 32 UrhG: Angemessene Vergütung für Nutzungsrechtseinräumung — Korrektionsanspruch.
- § 32a UrhG: Bestseller-Klausel — Anspruch auf weitere Beteiligung bei auffälligem Missverhältnis.
- § 41 UrhG: Rückrufsrecht wegen Nichtausübung — 2-Jahres-Frist nach Einräumung ohne Nutzung.

## Prüfraster

- Wurde das Datenbankwerk von einem Arbeitnehmer (§ 43 UrhG) oder einem Freiberufler (§ 31 UrhG) erstellt?
- Welche Nutzungsrechte wurden vertraglich eingeräumt — sind sie ausreichend für die geplante Nutzung?
- Ist die vereinbarte Vergütung nach § 32 UrhG angemessen, oder besteht ein Korrektionsanspruch?
- Wurde das Nutzungsrecht nach Einräumung über 2 Jahre nicht ausgeübt — kann der Rückruf nach § 41 UrhG erklärt werden?
- Ist das Datenbankherstellerrecht separat übertragen worden, oder ist nur das Urheberrecht am Datenbankwerk lizenziert?
- Enthält der Vertrag eine Regelung für die Weiterentwicklung der Datenbank — wer ist Urheber von Ergänzungen?
- Sind Unterlizenzen (§ 35 UrhG) für die geplante Nutzung zulässig?

## Typische Fallstricke

- Auftragswerk begründet kein automatisches Urheberrecht des Auftraggebers — explizite Nutzungsrechtseinräumung im Vertrag ist zwingend.
- Datenbankherstellerrecht und Urheberrecht am Datenbankwerk können bei verschiedenen Personen liegen (Investor vs. Schöpfer).
- Nutzungsrechts-AGB ohne hinreichende Bestimmtheit (fehlende Zweckbindung) greifen zu kurz — § 31 Abs. 5 UrhG Zweckübertragungslehre.
- Rückruf nach § 41 UrhG erfordert Fristsetzung und ist kostenlos für den Urheber — Auftraggeber unterschätzen dieses Risiko.
- Vergütungsanpassungsanspruch nach § 32a UrhG auch nach Vertragsabschluss möglich — bei erfolgreichen Datenbankprodukten relevant.

## Output

- Nutzungsrechtsklausel-Vorlage für Datenbankwerk-Auftragsvertrag
- Arbeitnehmerurheberrecht-Check (§ 43 UrhG) für Datenbankprojekte
- Vergütungsangemessenheitsprüfung (§ 32 UrhG)
- Rückrufrisiko-Bewertung (§ 41 UrhG) und Vermeidungsklausel
- Schnittstelle Herstellerrecht/Urheberrecht — Inhaberschaftsmatrix

## Quellen

- [§ 4 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/4.html)
- [§ 31 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/31.html)
- [§ 43 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/43.html)
- [§ 32 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/32.html)
- [§ 41 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/41.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
