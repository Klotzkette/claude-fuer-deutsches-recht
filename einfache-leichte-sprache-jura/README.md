# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`einfache-leichte-sprache-jura`) | [`einfache-leichte-sprache-jura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Übertragung juristischer Texte in **Einfache
Sprache** oder **Leichte Sprache**. Es richtet sich an Kanzleien, Behörden,
Beratungsstellen, Legal-Design-Teams und alle, die rechtliche Informationen
verständlich, respektvoll und rechtlich belastbar erklären müssen.

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

Automatisch generierte Komplett-Liste aller 70 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `annaeherung-quellenkarte` | Annaeherung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `bauen-fristennotiz-naechster-schritt` | Bauen: Fristennotiz und nächster Schritt: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-elsj-bescheidmodus-elsj` | Einfache Fristen Form Und Zustaendigkeit, Elsj Bescheidmodus, Elsj Kommandocenter: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `einfache-leichte-einfache-fristen-form-zustaendigkeit-rechtsweg` | Einfache: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-experimentelle-schriftsatz-brief-memo-bausteine` | Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-jura-mandantenkommunikation` | Jura: Mandantenkommunikation und Entscheidungsvorlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-juristische-erstpruefung-rollenklaerung` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-klaeren-compliance-dokumentation-aktenvermerk` | Klaeren: Compliance-Dokumentation und Aktenvermerk: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-leichte-risikoampel-gegenargumente` | Leichte: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-ls-juristisches-glossar-justizportal-pruefen` | Ls Juristisches Glossar Bauen / Ls Justizportal Pruefen Spezial / Ls Strafprozess Rechte Erklaeren Spezial: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `einfache-leichte-sichern-internationaler-bezug-schnittstellen` | Sichern: Internationaler Bezug und Schnittstellen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-dokumentenmatrix-lueckenliste` | Sprache: Dokumentenmatrix, Lückenliste und Nachforderung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `einfache-leichte-sprache-jura-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einfache-leichte-sprache-jura-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `einfache-leichte-sprache-jura-fristen-und-risikoampel` | Fristen- und Risikoampel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `einfache-leichte-sprache-jura-mandantenkommunikation` | Mandantenkommunikation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `einfache-leichte-sprache-jura-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `einfache-leichte-sprache-jura-standard` | Standard: Verhandlung, Vergleich und Eskalation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-texte` | Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-sprache-jura-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einfache-leichte-uebertragen-behoerden-gerichts-registerweg` | Uebertragen: Behörden-, Gerichts- oder Registerweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `einfache-leichte-zielgruppe-zahlen-schwellenwerte-berechnung` | Zielgruppe: Zahlen, Schwellenwerte und Berechnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `elsj-aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Auslaenderbehoerde Begleitschreiben fuer Mandanten. Vorlage Bescheid-Erklaerung. |
| `elsj-aufenthaltsrecht-mandant-betreuung` | Elsj Aufenthaltsrecht Mandant, Elsj Betreuung Vormundschaft, Elsj Einfache Sprache: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-bescheidmodus` | Bescheide einfach erlaeutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was muessen Sie tun? Bis wann? Was passiert sonst?'. |
| `elsj-betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behinder... |
| `elsj-familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo fuer den Mandanten: 'Was muessen Sie wissen, was muessen Sie entscheiden?' Sprachlich barrierearm. |
| `elsj-familienrecht-erstgespraech-juristische` | Elsj Familienrecht Erstgespraech, Elsj Juristische Sicherung, Elsj Kommunikation Mandant: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-... |
| `elsj-kommandocenter` | Kanzlei oder Behoerde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualit... |
| `elsj-kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information ueber das Verfahren. Pruefliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen fuer den naechsten Termin. |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. N... |
| `elsj-leichte-sprache-mietrecht` | Elsj Leichte Sprache, Elsj Mietrecht Kuendigungserklaerung, Elsj Pruefkriterien Für Qualitaet: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache fuer Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `elsj-pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Pruefliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `elsj-qualitaetsgate-rechtsnormen-einfach` | Elsj Qualitaetsgate, Elsj Rechtsnormen Einfach, Elsj Satzbau Regeln: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist... |
| `elsj-satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |
| `elsj-sozialgerichtsverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht'. |
| `elsj-sozialgerichtsverfahren-strafverfahren` | Elsj Sozialgerichtsverfahren, Elsj Strafverfahren Beschuldigter, Bauen Fristennotiz Und Naechster Schritt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-strafverfahren-beschuldigter` | Strafverfahren in Einfacher Sprache fuer Beschuldigte: Belehrung § 136 StPO, Rechte des Beschuldigten, Akteneinsicht, Wahlverteidiger/Pflichtverteidiger. Pflichtbelehrung in einfacher Sprache (BVerfG 2 BvR 1568/19). |
| `elsj-uebersetzungsablauf` | Standardablauf Uebersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz fuer Satz uebertragen, 4. Pruefen gegen Pruefliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Uebersetzung. |
| `elsj-uebersetzungsablauf-wortebene-haus` | Elsj Uebersetzungsablauf, Elsj Wortebene Haus Glossar, Elsj Zielgruppen Erkennen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `elsj-wortebene-haus-glossar` | Hauseigenes Glossar: typische juristische Begriffe und deren Uebersetzungen. Beispiele: 'Beklagter' = 'die Person, gegen die geklagt wird'; 'Frist' = 'Zeitraum, in dem etwas getan werden muss'. Aufnahme in Kanzlei-Wiki. |
| `elsj-zielgruppen-erkennen` | Zielgruppen erkennen: Einfache Sprache fuer geringe Lesekompetenz (B1), Leichte Sprache fuer Menschen mit Lernschwierigkeiten oder geringer Deutsch-Kenntnis. Wahl der richtigen Stufe pro Mandant/Adressat. Pruefraster und Beispiele. |
| `experimentelle-glossar-sonderfall-jura` | Experimentelle Schriftsatz Brief Und Memo Bausteine, Glossar Sonderfall Und Edge Case, Jura Mandantenkommunikation Entscheidungsvorlage: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `glossar-sonderfall-edge-case` | Glossar: Sonderfall und Edge-Case-Prüfung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `juristische-juristisches-beweislast-klaeren` | Juristische Erstpruefung Und Mandatsziel, Juristisches Beweislast Und Darlegungslast, Klaeren Compliance Dokumentation Und Akte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächst... |
| `juristisches-beweislast-darlegungslast` | Juristisches: Beweislast, Darlegungslast und Substantiierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `leichte-qualitaetsgate-rechtsinhalt` | Leichte Risikoampel Und Gegenargumente, Qualitaetsgate Formular Portal Und Einreichung, Rechtsinhalt Mehrparteien Konflikt Und Interessen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `leichte-sprache-jura-fristen-risiko-mandant` | Fristen Und Risikoampel, Mandantenkommunikation, Redteam Qualitygate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `leichte-sprache-jura-ls-bescheid-chronologie` | Allgemein, Ls Bescheid Uebersetzen Workflow, Chronologie Und Belegmatrix, ...: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `leichte-sprache-qualitaetsgate-verstaendlichkeit` | Qualitaetsgate: Fehlerbremse; Formular, Portal und Einreichungslogik: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `leichte-sprache-zielgruppe-zahlen-schwellen-berechnung` | Zielgruppe Zahlen Schwellen Und Berechnung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `ls-bescheid-uebersetzen-workflow` | Bescheid in Leichte Sprache uebersetzen Workflow: Originalbescheid, Kernaussagen extrahieren, je Aussage 1 kurzer Satz, Pruefung mit Zielgruppen-Vertreter, Layout (Bilder, Schriftgroesse), Pruefsiegel. Routet in einfache-leichte-sprache-... |
| `ls-juristisches-glossar-bauen` | Juristisches Glossar fuer Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext fuer 3... |
| `ls-justizportal-pruefen-spezial` | Spezialfall Justizportal in Leichte Sprache pruefen: Bayerisches Justizportal, JustizOnline, beA-Frontend. Konkrete Verbesserungsvorschlaege fuer Navigation, Wegleitsysteme, Antragsformulare. Pruefraster nach Inclusion Europe Regeln. |
| `ls-strafprozess-rechte-erklaeren-spezial` | Spezialfall Strafprozess-Rechte in Leichte Sprache erklaeren: § 136 StPO Belehrung, Recht zur Aussage und zum Schweigen, Pflichtverteidiger, Akteneinsicht. Mustertext und Pruefsiegel. Bedeutung fuer JVA-Insassen und Migrantinnen. |
| `nutzen-fehlerkatalog` | Nutzen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `rechtsinhalt-interessen` | Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `sichern-sprache-standard` | Sichern Internationaler Bezug Und Schnittstellen, Sprache Dokumentenmatrix Und Lueckenliste, Standard Verhandlung Vergleich Und Eskalation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `texte-uebertragen-zielgruppe-sprachniveau` | Texte Tatbestand Beweis Und Belege, Uebertragen Behörden Gericht Und Registerweg, Zielgruppe Sprachniveau Rechtsinhalt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belast... |
| `zielgruppe-sprachniveau-rechtsinhalt` | Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
