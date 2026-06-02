# Betreuungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`betreuungsrecht`) | [`betreuungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betreuungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Betreuungsfall Hildegard Sauer** (`betreuung-hildegard-sauer`) | [Gesamt-PDF lesen](../testakten/betreuung-hildegard-sauer/gesamt-pdf/betreuung-hildegard-sauer_gesamt.pdf) | [`testakte-betreuung-hildegard-sauer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-hildegard-sauer.zip) |
| **Akte Betreuung Schmalfeld: Kontodaten und verdächtige Verträge** (`betreuung-schmalfeld-kontodaten-vertraege`) | [Gesamt-PDF lesen](../testakten/betreuung-schmalfeld-kontodaten-vertraege/gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf) | [`testakte-betreuung-schmalfeld-kontodaten-vertraege.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Skills für **berufliche Betreuerinnen und Betreuer** nach dem Betreuungsorganisationsgesetz
(BtOG) und den §§ 1814 ff. BGB in der Fassung der Reform 2023.

> ⚠️ **Experimentell — keine Fachgutachten.** Die Skills sind generalisierte
> Beispiele. Jede Berufsbetreuerin und jeder Berufsbetreuer kalibriert die
> Skills selbst für die eigene Praxis und prüft jeden generierten Bericht
> vor Einreichung beim Betreuungsgericht.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Betreuungsrecht (`betreuungsrecht`, dieses Plugin) | [betreuungsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/betreuungsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

### Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-betreuung-hildegard-sauer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-hildegard-sauer.zip)

Fiktive Akte einer Berufsbetreuung einer 87-jährigen Mandantin (Hildegard Sauer): Bestellungsbeschluss, Vermögensverzeichnis, erster Jahresbericht, Genehmigungsanträge.

[testakte-betreuung-schmalfeld-kontodaten-vertraege.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip)

Fiktive Akte einer Vermögenssorge-Prüfung bei Herbert Wilhelm Schmalfeld:
Kontoauszüge 2023 bis 2025, Vertragsregister, verdächtige Zahlungen,
Fernwartung, Auslandsanlage, Immobilienreservierung und Maßnahmenplan.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakten

Zu diesem Plugin existieren 2 vollständige Beispielakten:

| Akte | Quelle | Direkt-Download |
|---|---|---|
| Betreuungsfall Hildegard Sauer | [`testakten/betreuung-hildegard-sauer/`](../testakten/betreuung-hildegard-sauer/) | [testakte-betreuung-hildegard-sauer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-hildegard-sauer.zip) |
| Betreuung Schmalfeld: Kontodaten und verdächtige Verträge | [`testakten/betreuung-schmalfeld-kontodaten-vertraege/`](../testakten/betreuung-schmalfeld-kontodaten-vertraege/) | [testakte-betreuung-schmalfeld-kontodaten-vertraege.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip) |

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Enthaltene Skills

| Skill | Gegenstand | Rechtsnorm |
|---|---|---|
| `jahresbericht-betreuungsgericht` | Strukturierter Jahresbericht ans Betreuungsgericht aus Ereignissen, E-Mails, Quittungen und Aktenvermerken | § 1863 BGB |
| `vermoegensverzeichnis-pruefung` | Erstellung und Aktualisierung des Vermögensverzeichnisses bei Übernahme der Betreuung | §§ 1835, 1839 BGB |
| `genehmigungspflicht-pruefung` | Prüfung, ob ein konkretes Rechtsgeschäft (Grundstücksverkauf, Erbausschlagung, Darlehen, Wohnungsauflösung, Heimvertrag) der Genehmigung des Betreuungsgerichts bedarf | §§ 1848–1858 BGB |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen auf verdächtige Vermögensabflüsse, Fernwartung, Hochrisikoanlagen, Auslandszahlungen und Schutzmaßnahmen prüfen | §§ 1821, 1825, 1835, 1865 BGB |

## Adressatenkreis

- Berufsbetreuerinnen und Berufsbetreuer mit Sachkundenachweis nach § 23 BtOG
- Vereinsbetreuerinnen und Vereinsbetreuer (§ 18 BtOG)
- Mitarbeitende von Betreuungsbehörden (§§ 6 ff. BtOG)
- Ehrenamtliche Betreuer (eingeschränkt; gerichtliche Beratung empfohlen)

## Wichtige Rechtsgrundlagen

- **BGB Buch 4 Abschnitt 3 (§§ 1814–1881)** — Rechtliche Betreuung (Reform 2023)
- **BtOG** — Betreuungsorganisationsgesetz (registrierte Berufsbetreuer, Vergütung, Aufsicht)
- **VBVG** — Vormünder- und Betreuervergütungsgesetz
- **FamFG §§ 271 ff.** — Verfahren in Betreuungssachen

## Zitierhinweise

Alle Skills zitieren nach den in der deutschen Rechtspraxis üblichen Konventionen:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

## Datenschutz und Vertraulichkeit

Berichte an das Betreuungsgericht enthalten Gesundheits-, Vermögens- und Sozialdaten.
Beim Einsatz von KI-Tools sind insbesondere zu beachten:

- Art. 9 DSGVO (besondere Kategorien personenbezogener Daten)
- § 203 StGB (Verletzung von Privatgeheimnissen — gilt für Berufsbetreuer)
- Empfehlung: Personenbezogene Daten vor Übergabe an KI pseudonymisieren
  (siehe Skill `playbook-aus-eigenen-daten` im Plugin `kanzlei-builder-hub`)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Betreuungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Be... |
| `aufgabenkreise-festlegen` | Aufgabenkreise einer Betreuung festlegen: Vermoegensvorsorge, Gesundheitsvorsorge, Aufenthaltsbestimmung, Postangelegenheiten, Wohnungsangelegenheiten. Empfehlung: nur erforderliche Kreise (Erforderlichkeitsgrundsatz § 1814 BGB). |
| `betreuer-als-erbe` | Workflow-Skill zu betreuer als erbe. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `betreuer-registrierung` | Erklärt die Abgrenzung beruflicher / ehrenamtlicher (privater) Betreuer nach BtOG seit 01.01.2023 sowie den Weg zur Registrierung als beruflicher Betreuer nach Paragraphen 23 ff. BtOG und der Betreuerregistrierungsverordnung. Behandelt S... |
| `betreuung-anwaltskosten-rvg` | Anwaltskosten im Betreuungsverfahren: RVG, Verfahrenspflegerbestellung, Verfahrenskostenhilfe nach § 76 FamFG. Empfehlung Mandantenkommunikation Kosten. |
| `betreuung-bei-demenz` | Betreuung bei Demenz: Geschaeftsfaehigkeit § 104 BGB, Lichte-Momente-Lehre, Einwilligung Aerztliche Behandlung, Pflegeentscheidungen. Vorgehen bei spaet diagnostizierter Demenz und Wirksamkeit frueherer Vertraege. |
| `betreuung-erbe-werden` | Betreuer als Erbe oder Beschenkter: § 1825 BGB Verbot, Genehmigungspflicht, Anfechtbarkeit. Pruefraster fuer Notarpraxis und Konflikt-Anzeige beim Betreuungsgericht. |
| `betreuung-fuer-erwachsene-kinder` | Betreuung fuer erwachsene Kinder mit Behinderung: Uebergang Vormundschaft zu Betreuung mit 18. Geburtstag, Erfordernis fruehzeitiger Antrag. Vorlage Mandantenkommunikation Eltern. |
| `betreuung-grenzueberschreitend` | Grenzueberschreitende Betreuung: Haager Erwachsenenschutzuebereinkommen 2000, Anerkennung in Deutschland und im EU-Ausland, anwendbares Recht. Output: Pruefraster fuer im Ausland lebende Betroffene. |
| `betreuung-im-strafverfahren` | Betreuung im Strafverfahren des Betroffenen: Schuldfaehigkeit nach §§ 20 und 21 StGB, Verteidigerbestellung, Vertretung Betreuer im Hauptverfahren. Schnittstelle Strafrecht und Betreuungsrecht. |
| `betreuungsantrag-erstellen` | Betreuungsantrag § 1814 BGB: Antragsteller, Betroffener, Aufgabenkreise, vorhandene Vorsorgevollmacht, gewuenschte Person als Betreuer, Begruendung Erforderlichkeit. Output: Antragsschriftsatz an Betreuungsgericht. |
| `betreuungsrecht-kaltstart-interview` | Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md mit Angaben zur Betreuerrolle (Berufsbetreuer / ehrenamtlich / Vereinsbetre... |
| `btr-aufgabenkreise-formulierung` | Aufgabenkreise praezise formulieren: Vermoegenssorge, Gesundheitssorge, Aufenthaltsbestimmung, Wohnungsangelegenheiten, Vertretung gegenueber Behoerden, Postangelegenheiten. Pruefraster fuer Mass und Mindestmass nach Reform 2023. |
| `btr-betreuer-gegen-vorsorgevollmacht` | Spezialfall Konflikt Berufsbetreuer gegen Bevollmaechtigten aus Vorsorgevollmacht: Vorrang Vorsorgevollmacht § 1814 Abs. 3 BGB, Pruefung Eignung Bevollmaechtigter, Kontrollbetreuung, Widerruf Vollmacht. Pruefraster und Beispielsfall. |
| `btr-erstantrag-und-eilantrag` | Erstantrag auf Betreuung beim Amtsgericht: § 1814 BGB Voraussetzungen seit Reform 2023, Eilantrag bei Gefahr im Verzug, einstweilige Anordnung § 300 FamFG. Strukturierte Antragsvorlage und Erfordernisse Sachverstaendigengutachten. |
| `btr-zwangsmedikation-genehmigung-spezial` | Spezialfall Genehmigung Zwangsmedikation § 1832 BGB nach Reform: enge Voraussetzungen, Erforderlichkeit, weniger eingreifende Mittel, gerichtliche Anhoerung Betroffener, Verfahrenspflegerbestellung. Pruefraster und Mustertexte. |
| `ehegattenvertretung-1358-bgb` | Notvertretungsrecht Ehegatten § 1358 BGB seit 01.01.2023: Voraussetzungen, sechsmonatige Befristung, Pflichten, Abgrenzung zur Betreuung. Vorlage Information Mandanten. |
| `freiheitsentziehende-massnahmen-1831` | Freiheitsentziehende Massnahmen § 1831 BGB: Fixierung, geschlossene Unterbringung, sedierende Medikation. Voraussetzungen Genehmigung Betreuungsgericht, regelmaessige Pruefung. EuGH-/EGMR-Vorgaben. |
| `genehmigungspflicht-pruefung` | 'Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung, Heimvertragsabschluss, Wohnungsauflös... |
| `jahresbericht-betreuungsgericht` | Jahresbericht für Betreuungsgericht nach § 1840 BGB erstellen: Anwendungsfall Betreuer muss jaehrlichen Rechenschaftsbericht über persoenliche und wirtschaftliche Verhältnisse der betreuten Person beim Betreuungsgericht einreichen. § 184... |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen in Betreuungsfällen auf Missbrauch prüfen: Anwendungsfall Betreuer oder Betreuungsgericht hat Verdacht auf ungewöhnliche Zahlungen verdächtige Dauerverträge oder Anlagegeschäfte zum Nachteil der betreu... |
| `spezial-bericht-mandantenkommunikation-entscheidungsvorlage` | Bericht: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betreuer-zahlen-schwellen-und-berechnung` | Betreuer: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betreuerpflichten-formular-portal-und-einreichung` | Betreuerpflichten: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betreuerpflichten-genehmigung-und-bericht` | Betreuerpflichten, Genehmigung und Berichtswesen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-betreuung-mehrparteien-konflikt-und-interessen` | Betreuung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betreuungsrecht-livequellen-und-rechtsprechungscheck` | Betreuungsrecht: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-betreuungsrechtliche-erstpruefung-und-mandatsziel` | Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bgb-verhandlung-vergleich-und-eskalation` | BGB: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-btog-schriftsatz-brief-und-memo-bausteine` | Btog: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-demenz-internationaler-bezug-und-schnittstellen` | Demenz: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-erbe-compliance-dokumentation-und-akte` | Erbe: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-genehmigung-red-team-und-qualitaetskontrolle` | Genehmigung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-genehmigungspflichten-dokumentenmatrix-und-lueckenliste` | Genehmigungspflichten: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-jahresbericht-tatbestand-beweis-und-belege` | Jahresbericht: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kontoanalyse-risikoampel-und-gegenargumente` | Kontoanalyse: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-livecheck-fristennotiz-und-naechster-schritt` | Livecheck: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verdachtsvertraege-behoerden-gericht-und-registerweg` | Verdachtsvertraege: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vermoegensverzeichnis-fristen-form-und-zustaendigkeit` | Vermoegensverzeichnis: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zwangsbehandlung-beweislast-und-darlegungslast` | Zwangsbehandlung: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `vermoegensverzeichnis-pruefung` | Vermögensverzeichnis für Betreuung prüfen und erstellen: Anwendungsfall Betreuer muss nach § 1835 BGB Vermögensverzeichnis aufnehmen oder bestehendes Verzeichnis auf Vollständigkeit und Richtigkeit prüfen. § 1835 BGB Vermögensverzeichnis... |
| `vorsorgevollmacht-pruefen` | Vorsorgevollmacht pruefen: § 1820 BGB, Reichweite, Form (Schriftform fuer Bank/Personalsorge), Beglaubigung, Hinterlegung im Zentralen Vorsorgeregister. Vorrang vor Betreuung. Pruefraster fuer den Vergleich Vollmacht/Betreuungsbedarf. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin betreuungsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin betreuungsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin betreuungsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin betreuungsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin betreuungsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin betreuungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin betreuungsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin betreuungsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin betreuungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin betreuungsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zwangsbehandlung-1832-bgb` | Zwangsbehandlung § 1832 BGB: Voraussetzungen, Genehmigung Betreuungsgericht, Verfahren § 312 FamFG. BVerfG-Linien zu Patientenautonomie (BVerfG 2 BvR 882/09). Output: Antragsentwurf an Gericht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
