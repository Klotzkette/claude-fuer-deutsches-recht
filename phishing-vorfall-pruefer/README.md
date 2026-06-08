# Phishing-Vorfall-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`phishing-vorfall-pruefer`) | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin** (`phishing-vorfall-mayer-sparkasse-berlin`) | [Gesamt-PDF lesen](../testakten/phishing-vorfall-mayer-sparkasse-berlin/gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) | [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `675u-675w-banking` | 675U: Verhandlung, Vergleich und Eskalation im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pruefe... |
| `675v-quellenkarte` | 675v Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `675w-zahlen-schwellen-und-berechnung` | 675W: Zahlen, Schwellenwerte und Berechnung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pruefe... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `arbeitnehmer-haftung-bgb-675u-phish-ceo` | Phishing am Arbeitsplatz: Arbeitnehmer-Haftung für durch Phishing verursachten Schaden. Innerbetriebliche Schadensausgleichung (BAG-Rechtsprechung), gestufte Haftung. Empfehlung Schulungspflichten Arbeitgeber im Phishing Vorfall Pruefer:... |
| `aufsicht-bafin-bank-strategie-banking-app` | BaFin-Beschwerde gegen Bank bei verweigerter Rueckbuchung: § 4 Abs. 4 FinDAG, BaFin-Verbraucherbeschwerde. Output: Beschwerde-Entwurf, Eskalationsstrategie im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale,... |
| `banking-behoerden-gericht-und-registerweg` | Banking: Behörden-, Gerichts- oder Registerweg im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pru... |
| `bankpflichten-beweislast-bgb` | Bankpflichten: Beweislast, Darlegungslast und Substantiierung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phish... |
| `bea-notfall-bgb-675v-erstkontakt-mandant` | Phishing gegen Anwalts-beA: Sofort Karte sperren, BRAK informieren, Mandanten informieren, Datenschutzverstoss pruefen Art. 33 DSGVO (72h-Frist). Berufshaftpflicht informieren § 31 VVG. Output: Notfall-Ablaufplan im Phishing Vorfall Prue... |
| `beweislast-mandantenkommunikation-entscheidungsvorlage` | Beweislast: Mandantenkommunikation und Entscheidungsvorlage im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishin... |
| `bgb-schriftsatz-brief-und-memo-bausteine` | BGB: Schriftsatz-, Brief- und Memo-Bausteine im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pruef... |
| `call-interessen-faelle-freistehender` | Call: Mehrparteienkonflikt und Interessenmatrix im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pr... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `faelle-abschlussprodukt-und-uebergabe` | Faelle: Abschlussprodukt und Übergabe im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pruefer: prü... |
| `fahrlaessigkeit-fehlerkatalog` | Fahrlaessigkeit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing... |
| `grobe-online-phishing` | Grobe: Formular, Portal und Einreichungslogik im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Prue... |
| `klage-fristennotiz-vorfall-phish-banking` | Klage: Fristennotiz und nächster Schritt im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Pruefer:... |
| `online-risikoampel-und-gegenargumente` | Online: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishin... |
| `output-waehlen` | Output wählen im Plugin Phishing Vorfall Pruefer: Diese Output-Weiche für Phishing Vorfall Prüfer entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `phish-banking-trojaner-haftung-spezial` | Spezialfall Banking-Trojaner und Haftung bei nicht autorisierten Zahlungen § 675u BGB / § 675v BGB: grob fahrlaessig, starke Kundenauthentifizierung PSD2. Pruefraster Bank und Kunde im Phishing Vorfall Pruefer: prüft konkret die einschlä... |
| `phish-ceo-fraud-konzern-spezial` | Spezialfall CEO-Fraud im Konzern: interne Kontrollen, Vier-Augen-Prinzip, Schadensersatz Geschaeftsleitung, Versicherer D-and-O / Cyber. Pruefraster für Konzern im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerk... |
| `phish-incident-meldepflichten-arten-erkennen` | Bauleiter Phishing-Incident-Triage: Erstbewertung, Containment, Beweissicherung, betroffene Konten, Hauptansprechpartner. Pruefraster für IT-Sec und Datenschutz im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerk... |
| `phish-meldepflichten-leitfaden` | Leitfaden Meldepflichten Phishing: Art. 33 DSGVO Aufsichtsbehoerde 72 Stunden, Art. 34 Betroffene, BSI bei KRITIS, Versicherer. Pruefraster Eskalationsstufen im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmal... |
| `phishing-arten-erkennen` | Phishing-Arten erkennen: E-Mail-Phishing, Smishing (SMS), Vishing (Anruf), Spear-Phishing, Pharming, Man-in-the-Middle (Tan-Abfangen). Indikatoren pro Art. Speziell: pushTAN-Aktivierung auf Angreiferseite, Verifizierungsanruf 'Bank-Siche... |
| `phishing-bank-strategie` | Anschreiben an Bank bei Phishing-Vorfall: Sachverhalt, Forderung Rueckbuchung § 675u BGB, Fristsetzung, Hinweis auf BGB-Beweislastregel, ggf. Verbraucherzentrale-Andeutung. Output: Anschreiben-Geruest im Phishing Vorfall Pruefer: prüft k... |
| `phishing-banking-app-malware` | Banking-App-Malware (Anubis, Cerberus, BRATA): Trojaner uebernimmt App und pushTAN, Overlay-Attacke. Forensische Hinweise: ungewoehnliche App-Berechtigungen, beobachtete SMS. Beweis-Strategie bei Bank im Phishing Vorfall Pruefer: prüft k... |
| `phishing-bgb-675u-haftung` | § 675u BGB Haftung des Zahlungsdienstleisters bei nicht autorisierter Zahlung: Erstattungspflicht, Beweislast bei Bank, dass Kunde authentifiziert hat. Ausnahmen § 675v BGB. Pruefraster im Phishing Vorfall Pruefer: prüft konkret die eins... |
| `phishing-bgb-675v-grobfahrlaessig` | § 675v Abs. 3 BGB Haftung Kunde bei grober Fahrlaessigkeit: Vollhaftung. Pruefraster: PIN/TAN weitergegeben? Auf Phishing-Seite eingegeben? Bei pushTAN: Geraetebindung umgangen? Rechtsprechung BGH XI ZR 91/14, XI ZR 96/11 im Phishing Vor... |
| `phishing-erstkontakt-mandant` | Erstkontakt Mandant nach Phishing-Vorfall: Eilfragen, Schaden Vorfall, Bank kontaktiert (Sperre Konto, Sperre Karten), Polizei (Strafanzeige § 263a StGB), beA-Notruf (bei Anwalts-PC). Output: Sofortmassnahmen-Liste und Fakten-Aufnahme im... |
| `phishing-faelle-rentner-kryptowaehrung` | Phishing bei aelteren Mandanten: Enkeltrick per Mail, gefaelschte Bank-Schreiben, telefonische Bestaetigungs-Masche. Besonderheiten Beweisfuehrung Verbraucher und Schutzbeduerftigkeit. § 675v BGB-Wertung milder anwenden im Phishing Vorfa... |
| `phishing-kryptowaehrung-recovery` | Phishing mit Kryptowaehrung: Recovery praktisch unmoeglich, aber Blockchain-Forensik (Chainalysis, TRM) kann Empfaenger-Wallet identifizieren. Strafrechtlich § 263a StGB. Zivilrechtlich Verfolgung an Exchange-Adresse, ggf. einstweilige M... |
| `phishing-mit-geschaeftskonto` | Phishing gegen Geschaeftskonto: keine Verbraucherregeln § 675f BGB, ggf. abweichende AGB der Bank, hoehere Sorgfaltsanforderungen. Pruefraster: Haftung Geschaeftsfuehrer für Organisationsverschulden gegenueber Gesellschaft im Phishing Vo... |
| `phishing-praeventionscheckliste-strafanzeige` | Praeventionscheckliste für Kanzleien und Mandanten: 2FA, separate Geraete für Banking, Phishing-Filter, BSI-Hinweise, Mitarbeiterschulung. Speziell für Anwaelte: kein beA auf privatem PC, Updates beA-Client im Phishing Vorfall Pruefer: p... |
| `phishing-spoofing-internationaler-bezug-schnittstellen` | Spoofing Internationaler Bezug Schnittstellen im Plugin Phishing Vorfall Pruefer im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-... |
| `phishing-strafanzeige-vorbereiten` | Strafanzeige § 263a StGB (Computerbetrug) vorbereiten: Sachverhalt, Beweismittel (Mail-Header, Logs, Kontoauszug), Tatverdacht, Verfasser-Hinweise. Output: Strafanzeige-Entwurf an zuständige Staatsanwaltschaft mit Cybercrime-Zuständigkei... |
| `phishing-supply-chain-bec` | Business Email Compromise (BEC), Rechnungs-Phishing: gefaelschte Lieferantenrechnung mit geaenderter IBAN. Vertragsrechtliche Folgen, schuldbefreiende Zahlung an falsche IBAN. Pruefraster: Anscheinsbeweis Zahlung an Glaeubiger? Rueckford... |
| `phishing-tan` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsp... |
| `phishing-tan-verfahren-vergleich` | TAN-Verfahren vergleichen aus Haftungssicht: smsTAN (veraltet), pushTAN, photoTAN, chipTAN. Welches Verfahren wurde manipuliert? Geraetebindung pushTAN als Sicherheitsanker. Auswirkung auf § 675v BGB im Phishing Vorfall Pruefer: prüft ko... |
| `phishing-tatbestand-beweis-und-belege` | Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing... |
| `phishing-zivilklage-bank` | Zivilklage gegen Bank wenn Rueckbuchung verweigert: § 675u BGB Anspruch, Beweislast bei Bank Authentifizierung. Output: Klageentwurf vor LG. Streitwert Schadenshoehe. Mandantenrechtsanspruch auf Datenherausgabe (Logs, Beweise) im Phishin... |
| `pruefen` | Prüft Phishing-Vorfall im Online-Banking oder Zahlungsverkehr auf Erstattungsansprüche gegen Zahlungsdienstleister. Anwendungsfall Bankkunde ist Opfer von Phishing pushTAN-Betrug oder Call-ID-Spoofing und Bank verweigert Erstattung. Norm... |
| `pushtan-compliance-dokumentation-und-akte` | Pushtan: Compliance-Dokumentation und Aktenvermerk im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall... |
| `pushtan-schlichtung-sonderfall` | Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing V... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schlichtung-sonderfall-und-edge-case` | Schlichtung: Sonderfall und Edge-Case-Prüfung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfall Prue... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Phishing Vorfall Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Be... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `versicherer-cyber-phishing-vorfall-zivilklage` | Cyberversicherung pruefen: Deckungsumfang bei Phishing/Social Engineering, Selbstbehalt, Ausschluesse (z. B. grobfahrlaessige Pflichtverletzung). Pruefraster Versicherungsbedingungen. Schadenanzeige § 31 VVG im Phishing Vorfall Pruefer:... |
| `vorfall-fristen-form-und-zustaendigkeit` | Vorfall: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Phishing Vorfal... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Phishing Vorfall Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
