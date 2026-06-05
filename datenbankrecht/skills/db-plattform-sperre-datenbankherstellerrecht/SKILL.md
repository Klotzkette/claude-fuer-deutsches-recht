---
name: db-plattform-sperre-datenbankherstellerrecht
description: "DB Plattform Sperre Datenbankherstellerrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Plattform Sperre Datenbankherstellerrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **DB Plattform Sperre Datenbankherstellerrecht** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-043-plattform-sperre-wegen-data-extraction` | Rechtliche Bewertung von Plattformsperren wegen Data Extraction: Berechtigung zur IP-Sperre und Account-Kündigung bei Datenbankrechts-Verletzungen (§§ 87a-87e UrhG), AGB-Grundlage, Kartellrechtliche Grenzen bei marktbeherrschenden Plattformen (Art. 102 AEUV) und Abwehr gegen unberechtigte Sperren. Erstellt Sperre-Dokumentation und Wiederherstellungsantrag. |
| `db-044-datenbankherstellerrecht-gegen-ex-mitarbeiter` | Datenbankherstellerrecht und arbeitsrechtliche Ansprüche gegen ausscheidende Mitarbeiter: § 87b UrhG bei Datenexport, GeschGehG § 4 bei Geheimnisverrat, nachvertragliches Wettbewerbsverbot (§ 74 HGB), Herausgabe- und Unterlassungsansprüche sowie Kündigung und Schadensersatz. Erstellt Präventionsplan und Sofortmaßnahmen-Checkliste bei vermutetem Datenabfluss. |
| `db-045-beweissicherung-durch-testcrawler` | Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testcrawlers zur Verletzungsdokumentation, Verwertbarkeit der Ergebnisse als Beweismittel, notarielle Begleitung und Verhältnis zu § 202a StGB und DSGVO. Erstellt Testcrawler-Protokoll und rechtliche Bewertung der Zulässigkeit dieser Beweismethode. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Plattform Sperre Datenbankherstellerrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-043-plattform-sperre-wegen-data-extraction`

**Fokus:** Rechtliche Bewertung von Plattformsperren wegen Data Extraction: Berechtigung zur IP-Sperre und Account-Kündigung bei Datenbankrechts-Verletzungen (§§ 87a-87e UrhG), AGB-Grundlage, Kartellrechtliche Grenzen bei marktbeherrschenden Plattformen (Art. 102 AEUV) und Abwehr gegen unberechtigte Sperren. Erstellt Sperre-Dokumentation und Wiederherstellungsantrag.

# Plattformsperre wegen Data Extraction — Berechtigung und Rechtsschutz

## Mandantenfall

- Plattformbetreiber will einen Nutzer sperren, der systematisch Daten extrahiert hat — wie dokumentiert er die Sperre rechtlich?
- Unternehmen wurde von einer Datenbank-Plattform gesperrt und bestreitet die Verletzungsvorwürfe — welche rechtlichen Mittel gegen die Sperre bestehen?
- Startup betreibt einen Aggregationsdienst und hat von einer marktbeherrschenden Plattform eine Sperrdrohung erhalten — ist die Sperre kartellrechtlich zulässig?

## Erste Schritte

1. Sperrberechtigung prüfen: Liegt eine vertragliche Grundlage (AGB) für die Sperre vor — Kündigung aus wichtigem Grund (§ 314 BGB) bei Datenbankrechts-Verletzung?
2. Urheberrechtliche Verletzung als Sperrgrundlage: § 87b UrhG-Verletzung durch Data Extraction als sachlicher Grund für außerordentliche Kündigung.
3. Verhältnismäßigkeit der Sperre prüfen: Sofortige Komplettsperre oder abgestufte Maßnahmen (Warnung, Drosselung, temporäre Sperre)?
4. Kartellrechtliche Grenzen: Marktbeherrschende Plattform kann nicht beliebig sperren — Art. 102 AEUV, § 19 GWB; Diskriminierungsverbot, Digital Markets Act (DMA).
5. Sperrung anfechten: Einstweilige Verfügung auf Wiederherstellung des Zugangs bei unberechtigter Sperre; vertragliche Schadensersatzansprüche.
6. Dokumentation der Sperre: Beweise für Verletzung sichern, Sperrbenachrichtigung, Frist zur Stellungnahme (für den Betreiber).

## Rechtsrahmen

- § 87b UrhG: Verletzung des Datenbankherstellerrechts als sachlicher Grund für Vertragsbeendigung.
- § 314 BGB: Außerordentliche Kündigung des Nutzungsvertrags aus wichtigem Grund — unverzüglich nach Kenntnis.
- § 307 BGB: AGB-Sperr- und Kündigungsklausel muss verhältnismäßig und transparent sein.
- Art. 102 AEUV: Marktmissbrauchsverbot — marktbeherrschende Plattform kann Zugang nicht willkürlich verweigern.
- § 19 GWB: Missbrauchsverbot für marktbeherrschende Unternehmen — Zugangsverweigerung als Diskriminierung?
- DMA Art. 5-6: Digital Markets Act — Gatekeeper-Verpflichtungen; Diskriminierungsverbote für große Plattformen.

## Prüfraster

- Liegt eine nachgewiesene Datenbankrechts-Verletzung (§ 87b UrhG) als Grundlage der Sperre vor?
- Enthält der AGB-Vertrag eine klare Sperr- und Kündigungsklausel für Datenverletzungen?
- Ist die Sperre verhältnismäßig — war eine vorherige Abmahnung oder Warnung möglich und zumutbar?
- Hat der Betreiber eine marktbeherrschende Stellung — gelten Art. 102 AEUV oder DMA-Verpflichtungen?
- Wird die Sperre diskriminierungsfrei angewandt — werden ähnliche Verletzungen anderer Nutzer gleich behandelt?
- Hat der gesperrte Nutzer eine Möglichkeit zur Stellungnahme erhalten (Anforderung nach DMA und P2B-VO)?
- Bestehen Alternativen zur vollständigen Sperre (Drosselung, Datenextraktions-Limitierung)?

## Typische Fallstricke

- Sperre ohne vorherige Abmahnung oder Kündigungsfristsetzung kann als unverhältnismäßig angesehen werden — insb. bei erstmaligem Verstoß.
- Marktbeherrschende Plattformen müssen bei Sperrungen besondere Verhältnismäßigkeit wahren und DMA-Anforderungen beachten.
- Diskriminierende Sperrpolitik (nur bestimmte Aggregatoren werden gesperrt, andere nicht) ist kartellrechtlich angreifbar.
- Unberechtigte Sperre kann Schadensersatzansprüche des gesperrten Nutzers auslösen (§ 280 BGB).
- DMA-Gatekeeper haben zusätzliche Verfahrenspflichten bei Sperrungen — Verletzung führt zu DMA-Bußgeldern.

## Output

- Sperrbenachrichtigungs-Vorlage mit Rechtsgrundsatz und Fristsetzung
- Sperr-Berechtigung-Prüfprotokoll (AGB + § 314 BGB + § 87b UrhG)
- Kartellrechtliche Sperrgrenzenbewertung (Art. 102 AEUV / § 19 GWB)
- Widerspruch gegen unberechtigte Sperre — Musterbrief
- Einstweiliger Verfügungsantrag auf Zugangswiederherstellung

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [Art. 102 AEUV — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A12012E102)
- [§ 19 GWB — dejure.org](https://dejure.org/gesetze/GWB/19.html)
- [DMA-Verordnung 2022/1925 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R1925)

## 2. `db-044-datenbankherstellerrecht-gegen-ex-mitarbeiter`

**Fokus:** Datenbankherstellerrecht und arbeitsrechtliche Ansprüche gegen ausscheidende Mitarbeiter: § 87b UrhG bei Datenexport, GeschGehG § 4 bei Geheimnisverrat, nachvertragliches Wettbewerbsverbot (§ 74 HGB), Herausgabe- und Unterlassungsansprüche sowie Kündigung und Schadensersatz. Erstellt Präventionsplan und Sofortmaßnahmen-Checkliste bei vermutetem Datenabfluss.

# Datenbankherstellerrecht gegen Ex-Mitarbeiter — Datenexport und Wettbewerbsverbot

## Mandantenfall

- Vertriebsleiter hat beim Ausscheiden den vollständigen Datenbankexport aller Kundendaten mitgenommen und arbeitet nun beim direkten Wettbewerber.
- Unternehmen entdeckt erst drei Monate nach Ausscheiden eines Mitarbeiters, dass Teile der proprietären Produktdatenbank beim Wettbewerber aufgetaucht sind.
- IT-Sicherheitsbeauftragter stellt nach forensischer Analyse fest, dass ein Mitarbeiter kurz vor Kündigung ungewöhnlich viele Datenbankabfragen getätigt hat.

## Erste Schritte

1. Forensische Sofortmaßnahmen: IT-Forensik, Zugriffsloganalyse, USB-Port-Protokolle, E-Mail-Export-Logs sichern — zeitkritisch.
2. Verletzungstatbestand bestimmen: § 87b UrhG (Datenbankherstellerrecht), GeschGehG § 4 (Geschäftsgeheimnis), § 241 Abs. 2 BGB (nachvertragliche Treuepflicht).
3. Beweise sichern: Forensisch gesicherte Kopien der Logs, eidesstattliche Versicherungen von Kollegen, Zugriffsprotokoll.
4. Ansprüche gegen Mitarbeiter formulieren: Unterlassung (§ 97 UrhG / §§ 6-7 GeschGehG), Herausgabe der kopierten Daten, Schadensersatz.
5. Ansprüche gegen neuen Arbeitgeber: Mitstörerhaftung, wenn er von der rechtswidrigen Herkunft wusste oder wissen musste.
6. Arbeitsrechtliche Maßnahmen: Fristlose Kündigung (§ 626 BGB) wenn noch im Arbeitsverhältnis; nachvertragliches Wettbewerbsverbot (§ 74 HGB) durchsetzen.

## Rechtsrahmen

- § 87b UrhG: Verletzung des Datenbankherstellerrechts durch Mitarbeiter-Datenexport — Unterlassung und Schadensersatz.
- GeschGehG § 4: Rechtswidrige Erlangung und Nutzung — Mitarbeiter verletzt GeschGehG durch unbefugten Export von Kundendaten.
- § 626 BGB: Fristlose Kündigung aus wichtigem Grund bei Datenexport während des Arbeitsverhältnisses.
- § 74 HGB: Nachvertragliches Wettbewerbsverbot — wirksam nur mit Karenzentschädigung; schützt Datenbanken vor Einsatz beim Wettbewerber.
- § 241 Abs. 2 BGB: Nebenpflichten im Arbeitsverhältnis — Geheimhaltungspflicht und Loyalitätspflicht.
- § 97 Abs. 1 UrhG: Unterlassungsanspruch bei Datenbankherstellerrechts-Verletzung — gegen Mitarbeiter und neuen Arbeitgeber.

## Prüfraster

- Belegen IT-Forensik-Daten (Logs, USB-Protokoll, E-Mail-Analyse) den Datenexport des Mitarbeiters?
- Ist das Datenbankherstellerrecht des Unternehmens nachweisbar (wesentliche Investition, § 87a UrhG)?
- Waren ausreichende Geheimhaltungsmaßnahmen vorhanden (NDA, Zugangsbeschränkungen, Datenschutzrichtlinien)?
- Liegt ein wirksames nachvertragliches Wettbewerbsverbot mit Karenzentschädigung (§ 74 HGB) vor?
- Sind die gestohlenen Datenbankteile beim neuen Arbeitgeber nachweisbar in Verwendung?
- Hat der neue Arbeitgeber Kenntnis oder fahrlässige Unkenntnis von der Datenherkunft?
- Ist die fristlose Kündigung noch möglich (§ 626 Abs. 2 BGB — 2-Wochen-Frist nach Kenntnis)?

## Typische Fallstricke

- 2-Wochen-Frist für fristlose Kündigung (§ 626 Abs. 2 BGB) läuft ab Kenntnis — verzögertes Handeln nach IT-Forensik führt zu Fristversäumnis.
- Nachvertragliches Wettbewerbsverbot ohne Karenzentschädigung ist nach § 74a HGB unverbindlich — für den Mitarbeiter freibleibend.
- Ansprüche gegen neuen Arbeitgeber als Mitstörer setzen Kenntnis oder grobe Fahrlässigkeit voraus — ohne Beweis keine Haftung.
- Forensische Beweise müssen unter Wahrung des Persönlichkeitsrechts des Mitarbeiters erhoben werden — Verwertungsverbote im Prozess möglich.
- GeschGehG-Ansprüche verjähren nach § 9 GeschGehG i.V.m. §§ 195-199 BGB — Fristen frühzeitig prüfen.

## Output

- Sofortmaßnahmen-Checkliste bei Datenabfluss-Verdacht (IT-Forensik, Beweis)
- Fristlose Kündigungs-Muster (§ 626 BGB mit Sachverhaltsschilderung)
- Unterlassungs- und Herausgabe-Klage-Muster (§ 87b UrhG + GeschGehG)
- Nachvertragliches-Wettbewerbsverbot-Muster (§ 74 HGB)
- Mitstörerhaftungs-Klage gegen neuen Arbeitgeber

## Quellen

- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [GeschGehG § 4 — dejure.org](https://dejure.org/gesetze/GeschGehG/4.html)
- [§ 626 BGB — dejure.org](https://dejure.org/gesetze/BGB/626.html)
- [§ 74 HGB — dejure.org](https://dejure.org/gesetze/HGB/74.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)

## 3. `db-045-beweissicherung-durch-testcrawler`

**Fokus:** Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testcrawlers zur Verletzungsdokumentation, Verwertbarkeit der Ergebnisse als Beweismittel, notarielle Begleitung und Verhältnis zu § 202a StGB und DSGVO. Erstellt Testcrawler-Protokoll und rechtliche Bewertung der Zulässigkeit dieser Beweismethode.

# Beweissicherung durch Testcrawler — Zulässigkeit und Verwertbarkeit

## Mandantenfall

- Datenbankbetreiber will einen eigenen Testcrawler einsetzen, der die Verletzungen eines Wettbewerbers dokumentiert — ist das rechtlich zulässig?
- Anwalt fragt, ob durch einen Testcrawler gewonnene Beweise im Datenbankrechts-Prozess vor dem LG Hamburg verwertbar sind.
- IT-Abteilung soll einen Testcrawler entwickeln, der regelmäßig Wettbewerber-Websites auf Datenbankübereinstimmungen prüft.

## Erste Schritte

1. Zulässigkeit des Testcrawlers prüfen: Ist das Crawlen der Wettbewerber-Website erlaubt — AGB-Bindung, robots.txt, § 202a StGB bei Zugangssicherungen?
2. Beweisziel definieren: Was soll der Testcrawler nachweisen — Übernahme eigener Datenbankeinträge, systematische Entnahme, Honey-Pot-Treffer?
3. Testcrawler-Protokoll aufsetzen: Zeitstempel, Hashwerte der abgerufenen Daten, Vergleich mit eigener Datenbank, Abrufvolumen und Herkunft.
4. Notarielle oder technische Zertifizierung: Einsatz eines qualifizierten Zeitstempels (eIDAS-VO) oder notarielle Protokollierung des Crawling-Vorgangs.
5. Honey-Pot-Vergleich integrieren: Wenn eigene Datenbank Honey-Pot-Einträge enthält, können diese bei Wettbewerber nachgewiesen werden.
6. Verwertbarkeit im Prozess sichern: § 286 ZPO — technische Protokolle als Augenscheinsbeweis; Sachverständigen-Gutachten über die Vergleichsmethodik.

## Rechtsrahmen

- § 286 ZPO: Freie Beweiswürdigung — technische Protokolle und Crawl-Ergebnisse als Augenscheinsbeweis verwertbar.
- § 202a StGB: Ausspähen von Daten — Testcrawler darf keine Zugangssicherungen (Passwort, CAPTCHA, technische Sperre) überwinden.
- § 1 UWG: Unlautere Mittel — Testcrawler ohne Täuschung ist kein UWG-Verstoß, wenn nur öffentlich zugängliche Daten abgerufen werden.
- DSGVO Art. 6: Personenbezogene Daten — Testcrawler darf keine personenbezogenen Daten ohne Rechtsgrundlage erheben.
- eIDAS-VO Art. 41: Qualifizierter elektronischer Zeitstempel für Nachweis des Abrufzeitpunkts.
- § 87b UrhG: Verletzungstatbestand als Beweisziel — Testcrawler dokumentiert Entnahme von Teilen der eigenen Datenbank.

## Prüfraster

- Ist die Zielwebsite öffentlich zugänglich ohne Zugangssicherung (kein Login, kein CAPTCHA, keine technische Blockade)?
- Verletzt der Testcrawler die AGB der Zielwebsite — kann der Betreiber des Testcrawlers deshalb haftbar werden?
- Ist § 202a StGB ausgeschlossen — werden keine Zugangssicherungen überwunden?
- Enthält das Crawl-Protokoll alle für die Beweiswürdigung erforderlichen Daten (Zeitstempel, URLs, abgerufene Inhalte, Hashwerte)?
- Wurden Honey-Pot-Datensätze bei der Zielwebsite gefunden — sind diese eindeutig identifizierbar?
- Ist das Protokoll von einem neutralen Dritten (Notar, IT-Sachverständiger) zertifiziert?
- Enthält der Testcrawler-Abruf personenbezogene Daten — welche DSGVO-Rechtsgrundlage gilt?

## Typische Fallstricke

- Testcrawler, der robots.txt ignoriert, kann AGB-Verletzung begehen — Testcrawler-AGB-Compliance prüfen.
- Ohne neutrale Zertifizierung kann der Gegner die Authentizität der Crawl-Ergebnisse im Prozess angreifen.
- Honey-Pot-Datensätze müssen vor dem Verdachtsfall in der eigenen Datenbank vorhanden sein — nachträgliches Einpflegen entwertet den Beweis.
- DSGVO-Verletzung durch personenbezogene Datenabrufe im Testcrawler kann die Beweise unverwertbar machen.
- Sachverständiger muss die Crawl-Vergleichsmethodik vor Gericht erklären können — Briefing ist entscheidend.

## Output

- Testcrawler-Zulässigkeitsprüfung (§ 202a StGB / AGB / DSGVO)
- Testcrawler-Protokollvorlage (Zeitstempel, Hashwerte, Honey-Pot-Vergleich)
- Notarielle Beweissicherungs-Briefing-Vorlage für Crawl-Dokumentation
- Sachverständigen-Briefing für technischen Datenbankvergleich
- Prozessvorbereitung: Crawl-Beweis als Augenscheinsbeweis nach § 286 ZPO

## Quellen

- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [eIDAS-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0910)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 371 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/371.html)
