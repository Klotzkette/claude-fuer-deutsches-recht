# BAV Strategie Konzern — Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB

Dieses Plugin stellt 21 spezialisierte Skills für die strategische Beratung zur betrieblichen Altersversorgung (BAV) in Konzernen bereit. Es spiegelt den Beratungsansatz der Boutique-Großkanzlei **Treuenfels Yamamoto Rechtsanwälte Partnerschaft mbB**, Königsallee 92, 40212 Düsseldorf (Zweigbüro: Gion-Higashi, Shijō-dōri, Kyoto).

**Namens-Partner:**
- Dr. Dr. Hartwig Treuenfels-Ostermann, LL.M. (Cambridge), Of Counsel, Honorarprofessor Düsseldorf für Arbeits- und Vergütungsrecht
- Yuki Yamamoto-Brennecke, bengoshi + Rechtsanwältin (Tokyo Bar), Leiterin Kyoto-Büro

**Federführender Partner BAV/Versorgung:**
Prof. Dr. Adalbert von Sompeh-Ostermann, LL.M. (Oxford), Versorgungs- und Transaktionsspezialist

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| BAV Strategie Konzern (`bav-strategie-konzern`) | [bav-strategie-konzern.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bav-strategie-konzern.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Betriebliche Altersversorgung – MEISSNER RHEINWERK AG** ([`testakten/bav-strategie-konzern-meissner-rheinwerk-ag/`](../testakten/bav-strategie-konzern-meissner-rheinwerk-ag/)).

Direkt-Download als ZIP: [testakte-bav-strategie-konzern-meissner-rheinwerk-ag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bav-strategie-konzern-meissner-rheinwerk-ag.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `bav-strategie-konzern.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe unsere Konzern-Versorgungsordnung und schlage eine Harmonisierungsstrategie vor.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Block A — Pensionsmodelle & Versorgungsarchitektur

| # | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------------|
| 1 | `pensionsmodelle-fuenf-durchfuehrungswege` | Direktzusage vs. Unterstützungskasse vs. Pensionskasse vs. Pensionsfonds vs. Direktversicherung; Entscheidungsmatrix, Bilanz- und Risiko-Tradeoffs, IFRS/HGB |
| 2 | `versorgungsordnung-und-betriebsvereinbarung-drafting` | Volltext-Templates Versorgungsordnung und Betriebsvereinbarung (Düsseldorfer Schule), Anpassungsklauseln § 16 BetrAVG, Spätehenklauseln, Hinterbliebenenversorgung |
| 3 | `governance-und-anpassungsmechanismen` | Pension Committee Charter, Trustee-Boards, Anpassungsentscheidungen § 16 BetrAVG, sachlich-billige Ermessensausübung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 5 | `internationale-harmonisierung-konzern-bav` | Konzernweite Plan-Inventory, Country-by-Country Matrix DE/UK/USA/FR/SG/JP, Global Benefits Policy, Local-vs-Group Governance |

## Block B — Pension Buyouts

| # | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------------|
| 6 | `pension-buyout-strukturierung-und-de-risking` | Buy-in vs. Buy-out vs. Longevity Swap, Versichererauswahl, Term Sheets, BaFin-Genehmigung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 9 | `buyout-im-ma-deal-asset-vs-share` | Pension Liabilities in Carve-outs, § 613a BGB, ABC-Klauseln, Garantien/Indemnities, W&I-Versicherung |
| 10 | `internationale-buyout-datenflows-und-datenschutz` | Art. 9 DSGVO, Drittlandtransfer Art. 46 SCC, APPI/PIPC Japan, Schrems II Workaround |

## Block C — Komplexe Versorgungssysteme

| # | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------------|
| 11 | `historisch-gewachsene-altsysteme-due-diligence` | Inventory-Methodik, Altzusagen 1970er/1980er, Versorgungstarifverträge, Sonderzusagen Führungskräfte, Risk Map |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 13 | `mitbestimmung-betriebsrat-einigungsstelle-bav` | § 87 Abs. 1 Nr. 8/10 BetrVG, Initiativrecht, Einigungsstellenverfahren, Spruch-Templates |
| 14 | `kollektivrechtliche-loesungen-und-sozialplan` | § 112 BetrVG, pensionsspezifische Sozialplanbestandteile, Abfindungsmodelle vs. Versorgungserhalt |

## Block D — Internationale Benefits-Strukturen

| # | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------------|
| 15 | `country-by-country-benefits-matrix-konzern` | Standardisierte Tabelle DE/UK/US/FR/SG/JP/NL/CH, lokale zwingende Vorschriften, Expat-Behandlung |
| 16 | `expatriate-pensionsplanung-und-totalization` | Sozialversicherungsabkommen, A1-Bescheinigung, Doppelbesteuerungsabkommen, Stranded Pensions |
| 17 | `japan-bav-und-corporate-pension-iorp` | Kakutei-kyuufu kigyou nenkin, Tax-Qualified Pension Plan Sunset, japanische DC-Pläne, Düsseldorf-Kyoto-Kollaboration |
| 18 | `post-merger-bav-integration-global` | HR-Transformation, Global-Mobility-Bezug, Reward-Harmonisierung, Day-1/Day-100/Day-365-Plan |

## Block E — Restrukturierungen & Kanzlei-Werkzeuge

| # | Skill-Name | Kurzbeschreibung |
|---|-----------|-----------------|
| 19 | `db-zu-dc-umstellung-mit-besitzstand` | DB-Schließung mit Past-Service-Schutz und Future-Service-DC, BAG-konforme Umstellung |
| 20 | `anpassungspruefung-paragraph-16-betravg` | Drei-Jahres-Rhythmus, wirtschaftliche Lage des Arbeitgebers, Reallohn-Bezugsgrößen-Verfahren |
| 21 | `mandantenkorrespondenz-bav-grosskanzlei-stil` | Briefkopf-Templates Treuenfels Yamamoto (deutsch/japanisch/englisch), Engagement Letter mit Stundensätzen, KYC |

---

*Alle Mandantennamen und Beratungsbeispiele in den Skills sind fiktiv. Die zitierten Gerichtsentscheidungen und Gesetze sind reale Quellen.*

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 18 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im bAV Strategie Konzern-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `buyout-im-ma-deal-asset-vs-share` | Betriebliche Altersversorgung im M-und-A-Deal strukturieren: Haftungsuebernahme bei Asset- vs. Share-Deal. Normen: §§ 4 28 BetrAVG, UmwG. Prüfraster: Haftungsuebergang, Versorgungsverpflichtungen, PSV-Haftung, Bilanzrisiken. Output: Haft... |
| `country-by-country-benefits-matrix-konzern` | Laenderuebergreifende Benefits-Matrix für internationalen Konzern erstellen: Versorgungsniveaus im Vergleich. Normen: IORP-II, lokale Pensionsgesetze. Prüfraster: Leistungsebenen, gesetzliche Mindeststandards, Harmonisierungsbedarf. Outp... |
| `cta-contractual-trust-arrangement-strukturierung` | CTA-Struktur für Auslagerung von Pensionsverpflichtungen aufsetzen: Treuhandmodell, IFRS-Saldierung. Normen: § 6a EStG, IFRS, BetrAVG. Prüfraster: Treuhandvertragsstruktur, Insolvenzsicherung, Bilanzauswirkung. Output: CTA-Strukturierung... |
| `drei-stufen-theorie-eingriffsanalyse` | Drei-Stufen-Theorie bei Eingriffen in Versorgungsanwartschaften anwenden: erdiente und noch erdienbare Anwartschaften. Normen: §§ 2 7 BetrAVG, BVerfG-Rechtsprechung. Prüfraster: Stufen-Einordnung, Eingriffsrechtfertigung, Verhältnismäßig... |
| `expatriate-pensionsplanung-und-totalization` | Pensionsplanung für Expatriates: Totalisierungsabkommen, Doppelversicherungsvermeidung, Pensionsluecken. Normen: EG-VO 883/2004, bilaterale SV-Abkommen. Prüfraster: Entsendelaender, Sozialversicherungsrecht, Pensionsbeitraege, Lueckenana... |
| `governance-und-anpassungsmechanismen` | Governance-Strukturen und Anpassungsmechanismen für Versorgungsordnung im Konzern entwerfen. Normen: §§ 1 ff. BetrAVG, BetrVG. Prüfraster: Anpassungsbeschlussprozesse, Mitbestimmungsrechte, Informationspflichten. Output: Governance-Handb... |
| `harmonisierung-und-migration-rechtssicher` | bAV-Systeme nach Unternehmensrestrukturierung rechtssicher harmonisieren und migrieren. Normen: §§ 4 17 BetrAVG, UmwG. Prüfraster: Bestandsschutz, Unverfallbarkeit, Migrationsschritte. Output: Harmonisierungsplan bAV. Abgrenzung: nicht M... |
| `historisch-gewachsene-altsysteme-due-diligence` | Due Diligence historisch gewachsener bAV-Altsysteme im Konzern: Bestandsanalyse, Haftungsrisiken. Normen: §§ 2 6a EStG, BetrAVG. Prüfraster: Durchführungswege, ungedeckte Verpflichtungen, Altregelungen. Output: Due-Diligence-Bericht bAV-... |
| `internationale-buyout-datenflows-und-datenschutz` | Datenfluesse bei internationalem bAV-Buyout datenschutzrechtlich absichern: DSGVO, Drittlandtransfers. Normen: DSGVO Art. 44 ff., BDSG. Prüfraster: Datenkategorie, Transfermechanismen, Einwilligung vs. Vertrag. Output: Datenschutz-Memo i... |
| `internationale-harmonisierung-konzern-bav` | Internationale bAV-Systeme im Konzern harmonisieren: Governance, Finanzierungsniveaus, lokale Compliance. Normen: IORP-II, lokale Pensionsgesetze, BetrAVG. Prüfraster: Harmonisierungsziele, rechtliche Grenzen, Umsetzungsplan. Output: Int... |
| `japan-bav-und-corporate-pension-iorp` | Japanisches betriebliches Altersversorgungssystem und IORP-Vergleich für europaeische Konzerne. Normen: IORP-II, japanisches Pensionsrecht DB-Pensions-Act. Prüfraster: Leistungsunterschiede, Finanzierungsanforderungen, Konvergenz. Output... |
| `kollektivrechtliche-loesungen-und-sozialplan` | Kollektivrechtliche Lösungen für bAV-Einschnitte: Betriebsvereinbarung, Sozialplan, Einigungsstelle. Normen: §§ 77 112 BetrVG, BetrAVG. Prüfraster: Mitbestimmungsrechte, Sozialplanvolumen, Ausgleichszahlungen. Output: Betriebsvereinbarun... |
| `mitbestimmung-betriebsrat-einigungsstelle-bav` | Betriebsratsbeteiligung bei bAV-Einführung und -Aenderung sicherstellen: Mitbestimmungsrechte. Normen: §§ 87 Abs. 1 Nr. 8 sowie 77 112 BetrVG. Prüfraster: Mitbestimmungstatbestaende, Informationspflichten, Einigungsstelle. Output: Beteil... |
| `pension-buyout-strukturierung-und-de-risking` | Pensionsbuyout und De-Risking strukturieren: Risikoauslagerung an Versicherungsunternehmen oder CTA. Normen: §§ 4 BetrAVG, VAG, IFRS. Prüfraster: Buyout-Voraussetzungen, Versicherungslösungen, Bilanzbereinigung. Output: Buyout-Strukturie... |
| `pensionsmodelle-fuenf-durchfuehrungswege` | Fuenf Durchführungswege der betrieblichen Altersversorgung vergleichen und waehlen. Normen: §§ 1 1b BetrAVG. Prüfraster: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds - Vor- und Nachteile. Output: D... |
| `psv-pensionssicherungsverein-und-haftungsketten` | PSV-Pflichtversicherung und Haftungsketten bei Insolvenz des Arbeitgebers analysieren. Normen: §§ 7 ff. BetrAVG, PSVaG-Satzung. Prüfraster: Insolvenzsicherungspflicht, gesicherte Leistungen, Haftungsquoten. Output: PSV-Haftungsanalyse. A... |
| `versorgungsordnung-und-betriebsvereinbarung-drafting` | Versorgungsordnung und Betriebsvereinbarung zur bAV-Einführung entwerfen. Normen: §§ 1 17 BetrAVG, §§ 77 87 BetrVG. Prüfraster: Leistungszusagen, Unverfallbarkeit, Mitbestimmung, Finanzierungsklauseln. Output: Versorgungsordnungs-Entwurf... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
