# Phishing-Vorfall-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB § 675u, § 675v, § 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer-werkstatt.md" download><code>phishing-vorfall-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer-schnellstart.md" download><code>phishing-vorfall-pruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) (Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für anwaltliche Prüfung von Online-Banking-Phishing, pushTAN-/photoTAN-Vorfällen, Call-ID-Spoofing, gefälschten Bankhotlines, Social Engineering und streitigen Erstattungsansprüchen gegen Zahlungsdienstleister.

Das Plugin arbeitet entlang des typischen Mandats:

1. Intake: Konto, Zahlungsinstrument, Schaden, Autorisierung, Sperr- und Anzeigeverlauf.
2. Rechtsrahmen: § 675u BGB, § 675v BGB, § 675w BGB, § 675l BGB, § 676b BGB und § 55 ZAG.
3. Beweisprüfung: TAN-Dialog, App-Screens, Banklogs, IP-Adressen, Device-Binding, SCA, Transaktionsmonitoring, Warnhinweise.
4. Risikomatrix: nicht autorisierter Zahlungsvorgang, grobe Fahrlässigkeit, Bankpflichtverletzung, Mitverschulden/Quotelung, Ombudsmann oder Klage.
5. Output: Erstbewertung, Bankaufforderung, Ombudsmann-Antrag, Klagegerüst, Beweisantritts- und Log-Anforderung.

## Inhalt

- `skills/phishing-vorfall-pruefen/SKILL.md` - geführter Hauptworkflow.
- `references/rechtsrahmen.md` - Arbeitsrahmen mit amtlichen Normlinks.
- `assets/checklisten/` - Intake, Beweis- und Logmatrix, grobe-Fahrlässigkeit-Ampel.
- `assets/vorlagen/` - Bankaufforderung, Ombudsmann-Antrag, Klagegerüst.
- `scripts/phishing_case_gate.py` - kleines Offline-Gate für strukturierte Fallbewertung.

## Arbeitsprinzip

Das Plugin entscheidet keinen Fall automatisch. Es zwingt zur sauberen Trennung:

- Hat der Kunde den konkreten Zahlungsvorgang autorisiert?
- Liegt ein Einwand aus § 675v BGB vor?
- Was ist bewiesen, was nur behauptet?
- Welche Banklogs müssen verlangt werden?
- Ist Schlichtung, Teilvergleich oder Klage der bessere nächste Schritt?

Alle rechtlichen Bewertungen sind Arbeitsentwürfe und müssen durch eine qualifizierte Person geprüft werden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `675u-675w-banking` | 675U: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `675v-quellenkarte` | 675v Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `675w-zahlen-schwellen-und-berechnung` | 675W: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anschluss-routing` | Anschluss-Routing für Phishing-Vorfall-Prüfer: wählt den nächsten Spezial-Skill nach Engpass (Art. 33 DSGVO 72h, Vorfallsbericht, Logs, Bank-Korrespondenz), dokumentiert Router-Entscheidung mit Begründung. |
| `arbeitnehmer-haftung-bgb-675u-phish-ceo` | Phishing am Arbeitsplatz: Arbeitnehmer-Haftung für durch Phishing verursachten Schaden. Innerbetriebliche Schadensausgleichung (BAG-Rechtsprechung), gestufte Haftung. Empfehlung Schulungspflichten Arbeitgeber im Phishing Vorfall Prüfer. |
| `aufsicht-bafin-bank-strategie-banking-app` | BaFin-Beschwerde gegen Bank bei verweigerter Rueckbuchung: § 4 Abs. 4 FinDAG, BaFin-Verbraucherbeschwerde. Output: Beschwerde-Entwurf, Eskalationsstrategie im Phishing Vorfall Prüfer. |
| `banking-behoerden-gericht-und-registerweg` | Banking: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `bankpflichten-beweislast-bgb` | Bankpflichten: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `bea-notfall-bgb-675v-erstkontakt-mandant` | Phishing gegen Anwalts-beA: Sofort Karte sperren, BRAK informieren, Mandanten informieren, Datenschutzverstoss prüfen Art. 33 DSGVO (72h-Frist). Berufshaftpflicht informieren § 31 VVG. Output: Notfall-Ablaufplan im Phishing Vorfall Prüfer. |
| `beweislast-mandantenkommunikation-entscheidungsvorlage` | Beweislast: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `bgb-schriftsatz-brief-und-memo-bausteine` | BGB: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `call-interessen-faelle-freistehender` | Call: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Phishing-Vorfall-Prüfer: sortiert Vorfallsbericht, Logs, Bank-Korrespondenz, prüft Datum, Absender, Frist und Beweiswert (Mail-Forensik, Server-Logs); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-routing` | Einstieg, Triage und Routing für Phishing-Vorfall-Prüfer: ordnet Rolle (Geschädigtes Unternehmen, Mitarbeiter, Bank), markiert Frist (Art. 33 DSGVO 72h), wählt Norm (DSGVO Art. 33 Meldung, NIS2, § 8b BSIG) und Zuständigkeit (BSI), leitet... |
| `faelle-abschlussprodukt-und-uebergabe` | Faelle: Abschlussprodukt und Übergabe. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `fahrlaessigkeit-fehlerkatalog` | Fahrlaessigkeit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `grobe-online-phishing` | Grobe: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `klage-fristennotiz-vorfall-phish-banking` | Klage: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `online-risikoampel-und-gegenargumente` | Online: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Phishing-Vorfall-Prüfer: stimmt Adressat (Geschädigtes Unternehmen, Mitarbeiter, Bank), Frist (Art. 33 DSGVO 72h) und Form auf den Zweck ab — typische Outputs: Vorfallsmeldung Art. 33 DSGVO, BSI-Meldung NIS2, Strafanzeige... |
| `phish-banking-trojaner-haftung-spezial` | Spezialfall Banking-Trojaner und Haftung bei nicht autorisierten Zahlungen § 675u BGB / § 675v BGB: grob fahrlaessig, starke Kundenauthentifizierung PSD2. Prüfraster Bank und Kunde im Phishing Vorfall Prüfer. |
| `phish-ceo-fraud-konzern-spezial` | Spezialfall CEO-Fraud im Konzern: interne Kontrollen, Vier-Augen-Prinzip, Schadensersatz Geschäftsleitung, Versicherer D-and-O / Cyber. Prüfraster für Konzern im Phishing Vorfall Prüfer. |
| `phish-incident-meldepflichten-arten-erkennen` | Bauleiter Phishing-Incident-Triage: Erstbewertung, Containment, Beweissicherung, betroffene Konten, Hauptansprechpartner. Prüfraster für IT-Sec und Datenschutz im Phishing Vorfall Prüfer. |
| `phish-meldepflichten-leitfaden` | Leitfaden Meldepflichten Phishing: Art. 33 DSGVO Aufsichtsbehoerde 72 Stunden, Art. 34 Betroffene, BSI bei KRITIS, Versicherer. Prüfraster Eskalationsstufen im Phishing Vorfall Prüfer. |
| `phishing-arten-erkennen` | Phishing-Arten erkennen: E-Mail-Phishing, Smishing (SMS), Vishing (Anruf), Spear-Phishing, Pharming, Man-in-the-Middle (Tan-Abfangen). Indikatoren pro Art. Speziell: pushTAN-Aktivierung auf Angreiferseite, Verifizierungsanruf 'Bank-Siche... |
| `phishing-bank-strategie` | Anschreiben an Bank bei Phishing-Vorfall: Sachverhalt, Forderung Rueckbuchung § 675u BGB, Fristsetzung, Hinweis auf BGB-Beweislastregel, ggf. Verbraucherzentrale-Andeutung. Output: Anschreiben-Geruest im Phishing Vorfall Prüfer. |
| `phishing-banking-app-malware` | Banking-App-Malware (Anubis, Cerberus, BRATA): Trojaner uebernimmt App und pushTAN, Overlay-Attacke. Forensische Hinweise: ungewoehnliche App-Berechtigungen, beobachtete SMS. Beweis-Strategie bei Bank im Phishing Vorfall Prüfer. |
| `phishing-bgb-675u-haftung` | § 675u BGB Haftung des Zahlungsdienstleisters bei nicht autorisierter Zahlung: Erstattungspflicht, Beweislast bei Bank, dass Kunde authentifiziert hat. Ausnahmen § 675v BGB. Prüfraster im Phishing Vorfall Prüfer. |
| `phishing-bgb-675v-grobfahrlaessig` | § 675v Abs. 3 BGB Haftung Kunde bei grober Fahrlaessigkeit: Vollhaftung. Prüfraster: PIN/TAN weitergegeben? Auf Phishing-Seite eingegeben? Bei pushTAN: Geraetebindung umgangen? Rechtsprechung BGH XI ZR 91/14, XI ZR 96/11 im Phishing Vorf... |
| `phishing-erstkontakt-mandant` | Erstkontakt Mandant nach Phishing-Vorfall: Eilfragen, Schaden Vorfall, Bank kontaktiert (Sperre Konto, Sperre Karten), Polizei (Strafanzeige § 263a StGB), beA-Notruf (bei Anwalts-PC). Output: Sofortmassnahmen-Liste und Fakten-Aufnahme im... |
| `phishing-faelle-rentner-kryptowaehrung` | Phishing bei aelteren Mandanten: Enkeltrick per Mail, gefaelschte Bank-Schreiben, telefonische Bestaetigungs-Masche. Besonderheiten Beweisfuehrung Verbraucher und Schutzbeduerftigkeit. § 675v BGB-Wertung milder anwenden im Phishing Vorfa... |
| `phishing-kryptowaehrung-recovery` | Phishing mit Kryptowaehrung: Recovery praktisch unmoeglich, aber Blockchain-Forensik (Chainalysis, TRM) kann Empfaenger-Wallet identifizieren. Strafrechtlich § 263a StGB. Zivilrechtlich Verfolgung an Exchange-Adresse, ggf. einstweilige M... |
| `phishing-mit-geschaeftskonto` | Phishing gegen Geschäftskonto: keine Verbraucherregeln § 675f BGB, ggf. abweichende AGB der Bank, hoehere Sorgfaltsanforderungen. Prüfraster: Haftung Geschäftsführer für Organisationsverschulden gegenueber Gesellschaft im Phishing Vorfal... |
| `phishing-praeventionscheckliste-strafanzeige` | Praeventionscheckliste für Kanzleien und Mandanten: 2FA, separate Geraete für Banking, Phishing-Filter, BSI-Hinweise, Mitarbeiterschulung. Speziell für Anwaelte: kein beA auf privatem PC, Updates beA-Client im Phishing Vorfall Prüfer. |
| `phishing-strafanzeige-vorbereiten` | Strafanzeige § 263a StGB (Computerbetrug) vorbereiten: Sachverhalt, Beweismittel (Mail-Header, Logs, Kontoauszug), Tatverdacht, Verfasser-Hinweise. Output: Strafanzeige-Entwurf an zuständige Staatsanwaltschaft mit Cybercrime-Zuständigkei... |
| `phishing-supply-chain-bec` | Business Email Compromise (BEC), Rechnungs-Phishing: gefaelschte Lieferantenrechnung mit geaenderter IBAN. Vertragsrechtliche Folgen, schuldbefreiende Zahlung an falsche IBAN. Prüfraster: Anscheinsbeweis Zahlung an Gläubiger? Rueckforder... |
| `phishing-tan` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Phishing Vorfall Prüfer. |
| `phishing-tan-verfahren-vergleich` | TAN-Verfahren vergleichen aus Haftungssicht: smsTAN (veraltet), pushTAN, photoTAN, chipTAN. Welches Verfahren wurde manipuliert? Geraetebindung pushTAN als Sicherheitsanker. Auswirkung auf § 675v BGB im Phishing Vorfall Prüfer. |
| `phishing-tatbestand-beweis-und-belege` | Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `phishing-versicherer-cyber` | Cyberversicherung pruefen: Deckungsumfang bei Phishing/Social Engineering, Selbstbehalt, Ausschluesse (z. B. grobfahrlaessige Pflichtverletzung). Pruefraster Versicherungsbedingungen. Schadenanzeige § 31 VVG. |
| `phishing-zivilklage-bank` | Zivilklage gegen Bank wenn Rueckbuchung verweigert: § 675u BGB Anspruch, Beweislast bei Bank Authentifizierung. Output: Klageentwurf vor LG. Streitwert Schadenshoehe. Mandantenrechtsanspruch auf Datenherausgabe (Logs, Beweise) im Phishin... |
| `pruefen` | Prüft Phishing-Vorfall im Online-Banking oder Zahlungsverkehr auf Erstattungsansprüche gegen Zahlungsdienstleister. Anwendungsfall Bankkunde ist Opfer von Phishing pushTAN-Betrug oder Call-ID-Spoofing und Bank verweigert Erstattung. Norm... |
| `pushtan-compliance-dokumentation-und-akte` | Pushtan: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `pushtan-schlichtung-sonderfall` | Prüfer: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `quellen-livecheck` | Quellen-Live-Check für Phishing-Vorfall-Prüfer: prüft Normen (DSGVO Art. 33 Meldung, NIS2, § 8b BSIG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BSI und Quellenhygiene nach references/quellenhygiene.md. |
| `schlichtung-sonderfall-und-edge-case` | Schlichtung: Sonderfall und Edge-Case-Prüfung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `spezial-675v-livequellen-und-rechtsprechungscheck` | 675V: Livequellen- und Rechtsprechungscheck. |
| `spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle` | Fahrlaessigkeit: Red-Team und Qualitätskontrolle. |
| `spezial-pruefer-dokumentenmatrix-und-lueckenliste` | Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `spoofing-internationaler-bezug-und-schnittstellen` | Spoofing: Internationaler Bezug und Schnittstellen: Spoofing: Internationaler Bezug und Schnittstellen. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Phishing Vorfall Prüfer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Phishing-Vorfall-Prüfer: trennt fehlende Tatsachen von fehlenden Belegen (Vorfallsbericht, Logs, Bank-Korrespondenz), nennt pro Lücke Beweisthema, Beschaffungsweg (BSI), Frist und Ersatznachweis. |
| `versicherer-cyber-phishing-vorfall-zivilklage` | Cyberversicherung prüfen: Deckungsumfang bei Phishing/Social Engineering, Selbstbehalt, Ausschluesse (z. B. grobfahrlaessige Pflichtverletzung). Prüfraster Versicherungsbedingungen. Schadenanzeige § 31 VVG im Phishing Vorfall Prüfer. |
| `vorfall-fristen-form-und-zustaendigkeit` | Vorfall: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Phishing Vorfall Prüfer. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Phishing Vorfall Prüfer. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Phishing Vorfall Prüfer. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
