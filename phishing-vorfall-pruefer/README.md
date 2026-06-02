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

## Direkt-Download

[phishing-vorfall-pruefer.zip herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip)

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Phishing-Vorfall Mayer ./. Sparkasse Berlin** ([`testakten/phishing-vorfall-mayer-sparkasse-berlin/`](../testakten/phishing-vorfall-mayer-sparkasse-berlin/)).

Direkt-Download als ZIP: [testakte-phishing-vorfall-mayer-sparkasse-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

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
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Phishing Vorfall Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeit... |
| `phish-banking-trojaner-haftung-spezial` | Spezialfall Banking-Trojaner und Haftung bei nicht autorisierten Zahlungen § 675u BGB / § 675v BGB: grob fahrlaessig, starke Kundenauthentifizierung PSD2. Pruefraster Bank und Kunde. |
| `phish-ceo-fraud-konzern-spezial` | Spezialfall CEO-Fraud im Konzern: interne Kontrollen, Vier-Augen-Prinzip, Schadensersatz Geschaeftsleitung, Versicherer D-and-O / Cyber. Pruefraster fuer Konzern. |
| `phish-incident-triage-bauleiter` | Bauleiter Phishing-Incident-Triage: Erstbewertung, Containment, Beweissicherung, betroffene Konten, Hauptansprechpartner. Pruefraster fuer IT-Sec und Datenschutz. |
| `phish-meldepflichten-leitfaden` | Leitfaden Meldepflichten Phishing: Art. 33 DSGVO Aufsichtsbehoerde 72 Stunden, Art. 34 Betroffene, BSI bei KRITIS, Versicherer. Pruefraster Eskalationsstufen. |
| `phishing-arbeitnehmer-haftung` | Phishing am Arbeitsplatz: Arbeitnehmer-Haftung fuer durch Phishing verursachten Schaden. Innerbetriebliche Schadensausgleichung (BAG-Rechtsprechung), gestufte Haftung. Empfehlung Schulungspflichten Arbeitgeber. |
| `phishing-arten-erkennen` | Phishing-Arten erkennen: E-Mail-Phishing, Smishing (SMS), Vishing (Anruf), Spear-Phishing, Pharming, Man-in-the-Middle (Tan-Abfangen). Indikatoren pro Art. Speziell: pushTAN-Aktivierung auf Angreiferseite, Verifizierungsanruf 'Bank-Siche... |
| `phishing-aufsicht-bafin` | BaFin-Beschwerde gegen Bank bei verweigerter Rueckbuchung: § 4 Abs. 4 FinDAG, BaFin-Verbraucherbeschwerde. Output: Beschwerde-Entwurf, Eskalationsstrategie. |
| `phishing-bank-strategie` | Anschreiben an Bank bei Phishing-Vorfall: Sachverhalt, Forderung Rueckbuchung § 675u BGB, Fristsetzung, Hinweis auf BGB-Beweislastregel, ggf. Verbraucherzentrale-Andeutung. Output: Anschreiben-Geruest. |
| `phishing-banking-app-malware` | Banking-App-Malware (Anubis, Cerberus, BRATA): Trojaner uebernimmt App und pushTAN, Overlay-Attacke. Forensische Hinweise: ungewoehnliche App-Berechtigungen, beobachtete SMS. Beweis-Strategie bei Bank. |
| `phishing-bea-notfall-anwalt` | Phishing gegen Anwalts-beA: Sofort Karte sperren, BRAK informieren, Mandanten informieren, Datenschutzverstoss pruefen Art. 33 DSGVO (72h-Frist). Berufshaftpflicht informieren § 31 VVG. Output: Notfall-Ablaufplan. |
| `phishing-bgb-675u-haftung` | § 675u BGB Haftung des Zahlungsdienstleisters bei nicht autorisierter Zahlung: Erstattungspflicht, Beweislast bei Bank, dass Kunde authentifiziert hat. Ausnahmen § 675v BGB. Pruefraster. |
| `phishing-bgb-675v-grobfahrlaessig` | § 675v Abs. 3 BGB Haftung Kunde bei grober Fahrlaessigkeit: Vollhaftung. Pruefraster: PIN/TAN weitergegeben? Auf Phishing-Seite eingegeben? Bei pushTAN: Geraetebindung umgangen? Rechtsprechung BGH XI ZR 91/14, XI ZR 96/11. |
| `phishing-erstkontakt-mandant` | Erstkontakt Mandant nach Phishing-Vorfall: Eilfragen, Schaden Vorfall, Bank kontaktiert (Sperre Konto, Sperre Karten), Polizei (Strafanzeige § 263a StGB), beA-Notruf (bei Anwalts-PC). Output: Sofortmassnahmen-Liste und Fakten-Aufnahme. |
| `phishing-faelle-rentner` | Phishing bei aelteren Mandanten: Enkeltrick per Mail, gefaelschte Bank-Schreiben, telefonische Bestaetigungs-Masche. Besonderheiten Beweisfuehrung Verbraucher und Schutzbeduerftigkeit. § 675v BGB-Wertung milder anwenden. |
| `phishing-kryptowaehrung-recovery` | Phishing mit Kryptowaehrung: Recovery praktisch unmoeglich, aber Blockchain-Forensik (Chainalysis, TRM) kann Empfaenger-Wallet identifizieren. Strafrechtlich § 263a StGB. Zivilrechtlich Verfolgung an Exchange-Adresse, ggf. einstweilige M... |
| `phishing-mit-geschaeftskonto` | Phishing gegen Geschaeftskonto: keine Verbraucherregeln § 675f BGB, ggf. abweichende AGB der Bank, hoehere Sorgfaltsanforderungen. Pruefraster: Haftung Geschaeftsfuehrer fuer Organisationsverschulden gegenueber Gesellschaft. |
| `phishing-praeventionscheckliste` | Praeventionscheckliste fuer Kanzleien und Mandanten: 2FA, separate Geraete fuer Banking, Phishing-Filter, BSI-Hinweise, Mitarbeiterschulung. Speziell fuer Anwaelte: kein beA auf privatem PC, Updates beA-Client. |
| `phishing-strafanzeige-vorbereiten` | Strafanzeige § 263a StGB (Computerbetrug) vorbereiten: Sachverhalt, Beweismittel (Mail-Header, Logs, Kontoauszug), Tatverdacht, Verfasser-Hinweise. Output: Strafanzeige-Entwurf an zustaendige Staatsanwaltschaft mit Cybercrime-Zustaendigk... |
| `phishing-supply-chain-bec` | Business Email Compromise (BEC), Rechnungs-Phishing: gefaelschte Lieferantenrechnung mit geaenderter IBAN. Vertragsrechtliche Folgen, schuldbefreiende Zahlung an falsche IBAN. Pruefraster: Anscheinsbeweis Zahlung an Glaeubiger? Rueckford... |
| `phishing-tan-verfahren-vergleich` | TAN-Verfahren vergleichen aus Haftungssicht: smsTAN (veraltet), pushTAN, photoTAN, chipTAN. Welches Verfahren wurde manipuliert? Geraetebindung pushTAN als Sicherheitsanker. Auswirkung auf § 675v BGB. |
| `phishing-versicherer-cyber` | Cyberversicherung pruefen: Deckungsumfang bei Phishing/Social Engineering, Selbstbehalt, Ausschluesse (z. B. grobfahrlaessige Pflichtverletzung). Pruefraster Versicherungsbedingungen. Schadenanzeige § 31 VVG. |
| `phishing-vorfall-pruefen` | Prüft Phishing-Vorfall im Online-Banking oder Zahlungsverkehr auf Erstattungsansprüche gegen Zahlungsdienstleister. Anwendungsfall Bankkunde ist Opfer von Phishing pushTAN-Betrug oder Call-ID-Spoofing und Bank verweigert Erstattung. Norm... |
| `phishing-zivilklage-bank` | Zivilklage gegen Bank wenn Rueckbuchung verweigert: § 675u BGB Anspruch, Beweislast bei Bank Authentifizierung. Output: Klageentwurf vor LG. Streitwert Schadenshoehe. Mandantenrechtsanspruch auf Datenherausgabe (Logs, Beweise). |
| `spezial-675u-verhandlung-vergleich-und-eskalation` | 675U: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-675v-livequellen-und-rechtsprechungscheck` | 675V: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-675w-zahlen-schwellen-und-berechnung` | 675W: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-banking-behoerden-gericht-und-registerweg` | Banking: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bankpflichten-beweislast-und-darlegungslast` | Bankpflichten: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-beweislast-mandantenkommunikation-entscheidungsvorlage` | Beweislast: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bgb-schriftsatz-brief-und-memo-bausteine` | BGB: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-call-mehrparteien-konflikt-und-interessen` | Call: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-faelle-abschlussprodukt-und-uebergabe` | Faelle: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle` | Fahrlaessigkeit: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grobe-formular-portal-und-einreichung` | Grobe: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klage-fristennotiz-und-naechster-schritt` | Klage: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-online-risikoampel-und-gegenargumente` | Online: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-phishing-tatbestand-beweis-und-belege` | Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefer-dokumentenmatrix-und-lueckenliste` | Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pushtan-compliance-dokumentation-und-akte` | Pushtan: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schlichtung-sonderfall-und-edge-case` | Schlichtung: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-spoofing-internationaler-bezug-und-schnittstellen` | Spoofing: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vorfall-fristen-form-und-zustaendigkeit` | Vorfall: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin phishing-vorfall-pruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin phishing-vorfall-pruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin phishing-vorfall-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin phishing-vorfall-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin phishing-vorfall-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin phishing-vorfall-pruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin phishing-vorfall-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin phishing-vorfall-pruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin phishing-vorfall-pruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin phishing-vorfall-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
