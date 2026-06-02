# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`einfache-leichte-sprache-jura`) | [`einfache-leichte-sprache-jura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Juristischer Mandantenbrief in Einfacher und Leichter Sprache** (`einfache-leichte-sprache-jura-mandantenbrief`) | [Gesamt-PDF lesen](../testakten/einfache-leichte-sprache-jura-mandantenbrief/gesamt-pdf/einfache-leichte-sprache-jura-mandantenbrief_gesamt.pdf) | [`testakte-einfache-leichte-sprache-jura-mandantenbrief.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-einfache-leichte-sprache-jura-mandantenbrief.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Übertragung juristischer Texte in **Einfache
Sprache** oder **Leichte Sprache**. Es richtet sich an Kanzleien, Behörden,
Beratungsstellen, Legal-Design-Teams und alle, die rechtliche Informationen
verständlich, respektvoll und rechtlich belastbar erklären müssen.

## Direkt herunterladen

- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip)
- [Beispielakte Mandantenbrief](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-einfache-leichte-sprache-jura-mandantenbrief.zip)

## Showcase-Hinweis

Dieses Plugin ist ein Experiment und ein Showcase. Es ist ein Versuch, sich der
Ergebnisrichtung von Einfacher Sprache und Leichter Sprache anzunähern, ohne
eine Standardprüfung oder Konformitätsaussage zu behaupten. Make of this what
you will, dear users: Ihr müsst selbst beurteilen, ob Verfahren, Sprache und
Ergebnis für eure Zielgruppe, euer Medium und euren Rechtstext passen. You are
on your own.

## Zwei Modi

| Modus | Ziel |
| --- | --- |
| Einfache Sprache | Standardsprache bleibt erkennbar. Fachsprache wird erklärt. Der Text wird klarer, kürzer, besser gegliedert und zielgruppenorientiert. |
| Leichte Sprache | Deutlich stärkere Vereinfachung. Kurze Sätze, klare Zeilen, viel Orientierung, erklärtes Fachwort, möglichst eine Aussage pro Satz. Eine Prüfung durch Personen aus der Zielgruppe wird empfohlen. |

## Workflow

1. Ausgangstext hochladen oder einfügen.
2. Zielgruppe, Anlass, Medium und gewünschte Tiefe klären.
3. Juristische Bedeutungen sichern: Rechte, Pflichten, Fristen, Beträge,
   Rechtsfolgen, Zuständigkeiten und Handlungsoptionen.
4. Modus wählen: Einfache Sprache oder Leichte Sprache.
5. Übertragung erstellen.
6. Glossar und Warnhinweise ergänzen.
7. Qualitätsgate laufen lassen.
8. Bei Leichter Sprache: Nutzerprüfung als offenen Schritt markieren, wenn sie
   nicht tatsächlich erfolgt ist.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `elsj-kommandocenter` | steuert Intake, Moduswahl, Zielgruppe, Rechtsinhalt und Ausgabeformat |
| `elsj-einfache-sprache` | überträgt juristische Texte in Einfache Sprache |
| `elsj-leichte-sprache` | überträgt juristische Texte in Leichte Sprache |
| `elsj-juristische-sicherung` | verhindert Bedeutungsverlust bei Rechten, Pflichten, Fristen und Rechtsfolgen |
| `elsj-qualitaetsgate` | prüft Verständlichkeit, Struktur, Glossar, Ton und rechtliche Vollständigkeit |

## Hilfsskript

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py \
  testakten/einfache-leichte-sprache-jura-mandantenbrief/02_einfache_sprache.md \
  --mode einfache
```

Das Skript ist kein Normprüfer. Es findet typische Warnsignale:
lange Sätze, sehr lange Wörter, Passiv-Kandidaten, Nominalstil und fehlende
Orientierungselemente.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren A... |
| `elsj-aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung. |
| `elsj-bescheidmodus` | Bescheide einfach erlaeutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was muessen Sie tun? Bis wann? Was passiert sonst?'. |
| `elsj-betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behinder... |
| `elsj-familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm. |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-... |
| `elsj-kommandocenter` | Kanzlei oder Behoerde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualit... |
| `elsj-kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin. |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. N... |
| `elsj-mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `elsj-pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `elsj-rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist... |
| `elsj-satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |
| `elsj-sozialgerichtsverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht'. |
| `elsj-strafverfahren-beschuldigter` | Strafverfahren in Einfacher Sprache fuer Beschuldigte: Belehrung § 136 StPO, Rechte des Beschuldigten, Akteneinsicht, Wahlverteidiger/Pflichtverteidiger. Pflichtbelehrung in einfacher Sprache (BVerfG 2 BvR 1568/19). |
| `elsj-uebersetzungsablauf` | Standardablauf Uebersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz fuer Satz uebertragen, 4. Pruefen gegen Pruefliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Uebersetzung. |
| `elsj-wortebene-haus-glossar` | Hauseigenes Glossar: typische juristische Begriffe und deren Uebersetzungen. Beispiele: 'Beklagter' = 'die Person, gegen die geklagt wird'; 'Frist' = 'Zeitraum, in dem etwas getan werden muss'. Aufnahme in Kanzlei-Wiki. |
| `elsj-zielgruppen-erkennen` | Zielgruppen erkennen: Einfache Sprache fuer geringe Lesekompetenz (B1), Leichte Sprache fuer Menschen mit Lernschwierigkeiten oder geringer Deutsch-Kenntnis. Wahl der richtigen Stufe pro Mandant/Adressat. Pruefraster und Beispiele. |
| `ls-bescheid-uebersetzen-workflow` | Bescheid in Leichte Sprache uebersetzen Workflow: Originalbescheid, Kernaussagen extrahieren, je Aussage 1 kurzer Satz, Pruefung mit Zielgruppen-Vertreter, Layout (Bilder, Schriftgroesse), Pruefsiegel. Routet in einfache-leichte-sprache-... |
| `ls-juristisches-glossar-bauen` | Juristisches Glossar fuer Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext fuer 3... |
| `ls-justizportal-pruefen-spezial` | Spezialfall Justizportal in Leichte Sprache pruefen: Bayerisches Justizportal, JustizOnline, beA-Frontend. Konkrete Verbesserungsvorschlaege fuer Navigation, Wegleitsysteme, Antragsformulare. Pruefraster nach Inclusion Europe Regeln. |
| `ls-strafprozess-rechte-erklaeren-spezial` | Spezialfall Strafprozess-Rechte in Leichte Sprache erklaeren: § 136 StPO Belehrung, Recht zur Aussage und zum Schweigen, Pflichtverteidiger, Akteneinsicht. Mustertext und Pruefsiegel. Bedeutung fuer JVA-Insassen und Migrantinnen. |
| `spezial-annaeherung-livequellen-und-rechtsprechungscheck` | Annaeherung: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bauen-fristennotiz-und-naechster-schritt` | Bauen: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-einfache-fristen-form-und-zustaendigkeit` | Einfache: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-experimentelle-schriftsatz-brief-und-memo-bausteine` | Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-glossar-sonderfall-und-edge-case` | Glossar: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-jura-mandantenkommunikation-entscheidungsvorlage` | Jura: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-juristische-erstpruefung-und-mandatsziel` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-juristisches-beweislast-und-darlegungslast` | Juristisches: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klaeren-compliance-dokumentation-und-akte` | Klaeren: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-leichte-risikoampel-und-gegenargumente` | Leichte: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nutzen-red-team-und-qualitaetskontrolle` | Nutzen: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-qualitaetsgate-formular-portal-und-einreichung` | Qualitaetsgate: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsinhalt-mehrparteien-konflikt-und-interessen` | Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sichern-internationaler-bezug-und-schnittstellen` | Sichern: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sprache-dokumentenmatrix-und-lueckenliste` | Sprache: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-standard-verhandlung-vergleich-und-eskalation` | Standard: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-texte-tatbestand-beweis-und-belege` | Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-uebertragen-behoerden-gericht-und-registerweg` | Uebertragen: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zielgruppe-sprachniveau-rechtsinhalt` | Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-zielgruppe-zahlen-schwellen-und-berechnung` | Zielgruppe: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin einfache-leichte-sprache-jura: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin einfache-leichte-sprache-jura: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin einfache-leichte-sprache-jura: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin einfache-leichte-sprache-jura: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin einfache-leichte-sprache-jura: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin einfache-leichte-sprache-jura: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin einfache-leichte-sprache-jura: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin einfache-leichte-sprache-jura: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin einfache-leichte-sprache-jura: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin einfache-leichte-sprache-jura: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
