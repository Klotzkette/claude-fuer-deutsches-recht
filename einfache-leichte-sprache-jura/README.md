# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`einfache-leichte-sprache-jura.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/einfache-leichte-sprache-jura.md) (46 KB)
- Im Repo: [`testakten/megaprompts/einfache-leichte-sprache-jura.md`](../testakten/megaprompts/einfache-leichte-sprache-jura.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 83 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `annaeherung-quellenkarte` | Annaeherung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `anschluss-routing` | Anschluss-Routing für Einfache/Leichte Sprache Jura: wählt den nächsten Spezial-Skill nach Engpass (keine harten Fristen, Originalbescheid, Vereinfachte Fassung, Lese-Test), dokumentiert Router-Entscheidung mit Begründung. |
| `aufenthaltsrecht-mandant` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Ausländerbehoerde Begleitschreiben für Mandanten. Vorlage Bescheid-Erklaerung. |
| `aufenthaltsrecht-mandant-betreuung` | Aufenthaltsrechtliche Mandantenkommunikation: AufenthG, Asyl, Familiennachzug. Anschreiben Ausländerbehoerde Begleitschreiben für Mandanten. Vorlage Bescheid-Erklaerung im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen T... |
| `bauen-fristennotiz-naechster-schritt` | Bauen: Fristennotiz und nächster Schritt im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `bauen-fristennotiz-und-naechster-schritt` | Bauen: Fristennotiz und nächster Schritt: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `bescheidmodus` | Bescheide einfach erläutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was müssen Sie tun? Bis wann? Was passiert sonst?'. |
| `bescheidmodus-02` | Bescheide einfach erläutern: typische Bescheide (Bafoeg, Wohngeld, Arbeitsamt-Eingliederungsmassnahme, Steuerbescheid). Vorlage Adressaten-Erklaerung mit 'Was sagt der Bescheid? Was müssen Sie tun? Bis wann? Was passiert sonst?' im Ein... |
| `betreuung-vormundschaft` | Mandanten in Betreuung oder Vormundschaft: spezifische Regeln BGB §§ 1814 ff., Beruecksichtigung Wuensche § 1821, Genehmigungspflichten. Sprache muss die Person selbst erreichen. Vorlage Anschreiben Betreuter. |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten od... |
| `dokumente-intake` | Dokumentenintake für Einfache/Leichte Sprache Jura: sortiert Originalbescheid, Vereinfachte Fassung, Lese-Test, prüft Datum, Absender, Frist und Beweiswert (Verständlichkeits-Test, Lese-Probanden-Feedback); markiert Lücken; berücksichtig... |
| `einfache-sprache` | Kanzlei oder Behörde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11 Leichte Sprache Behindert... |
| `einstieg-routing` | Einstieg, Triage und Routing für Einfache/Leichte Sprache Jura: ordnet Rolle (Adressat mit Lese-/Lernbeeinträchtigung, Anwalt/Behörde, Übersetzer), markiert Frist (keine harten Fristen), wählt Norm (BGG § 11 Leichte Sprache, UN-BRK Art.... |
| `experimentelle-glossar-sonderfall-jura` | Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `experimentelle-schriftsatz-brief-memo-bausteine` | Experimentelle: Schriftsatz-, Brief- und Memo-Bausteine im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `familienrecht-erstgespraech` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo für den Mandanten: 'Was müssen Sie wissen, was müssen Sie entscheiden?' Sprachlich barrierearm. |
| `familienrecht-erstgespraech-juristische` | Familienrecht Erstgespraech in Einfacher Sprache: Trennung, Scheidung, Unterhalt, Sorgerecht, Umgang. Vorlage Memo für den Mandanten: 'Was müssen Sie wissen, was müssen Sie entscheiden?' Sprachlich barrierearm im Einfache/Leichte Sprac... |
| `fristen-form-zustaendigkeit-rechtsweg` | Einfache: Fristen, Form, Zuständigkeit und Rechtsweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder... |
| `glossar-sonderfall-edge-case` | Glossar: Sonderfall und Edge-Case-Prüfung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung... |
| `glossar-sonderfall-und-edge-case` | Glossar: Sonderfall und Edge-Case-Prüfung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `jura-mandantenkommunikation` | Jura: Mandantenkommunikation und Entscheidungsvorlage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist... |
| `jura-mandantenkommunikation-entscheidungsvorlage` | Jura: Mandantenkommunikation und Entscheidungsvorlage: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `juristische-erstpruefung-rollenklaerung` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `juristische-juristisches-beweislast-klaeren` | Juristische: Erstprüfung, Rollenklärung und Mandatsziel: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-... |
| `juristisches-beweislast-darlegungslast` | Juristisches: Beweislast, Darlegungslast und Substantiierung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welch... |
| `juristisches-beweislast-und-darlegungslast` | Juristisches: Beweislast, Darlegungslast und Substantiierung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `klaeren-compliance-dokumentation-aktenvermerk` | Klären: Compliance-Dokumentation und Aktenvermerk im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Z... |
| `klaeren-compliance-dokumentation-und-akte` | Klären: Compliance-Dokumentation und Aktenvermerk: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `kommandocenter` | Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl Skill-Routing Qualita... |
| `kommunikation-mandant` | Mandantenkommunikation in Einfacher Sprache: Telefon-Leitfaden, E-Mail-Templates, schriftliche Information über das Verfahren. Prüfliste: Verstehen Sie das? Brauchen Sie eine Wiederholung? Notizen für den naechsten Termin. |
| `leichte-qualitaetsgate-rechtsinhalt` | Leichte: Risikoampel, Gegenargumente und Verteidigungslinien: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `leichte-sprache` | Kanzlei oder Behörde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. No... |
| `leichte-sprache-jura-fristen-risiko-mandant` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `leichte-sprache-jura-ls-bescheid-chronologie` | Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `leichte-sprache-mietrecht` | Kanzlei oder Behörde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur erklärte Woerter. No... |
| `leichte-sprache-qualitaetsgate-verstaendlichkeit` | Qualitaetsgate: Fehlerbremse; Formular, Portal und Einreichungslogik: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `ls-bescheid-uebersetzen-workflow` | Bescheid in Leichte Sprache übersetzen Workflow: Originalbescheid, Kernaussagen extrahieren, je Aussage 1 kurzer Satz, Prüfung mit Zielgruppen-Vertreter, Layout (Bilder, Schriftgroesse), Prüfsiegel. Routet in einfache-leichte-sprache-... |
| `ls-juristisches-glossar-bauen` | Juristisches Glossar für Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext für 30... |
| `ls-juristisches-glossar-justizportal-pruefen` | Juristisches Glossar für Einfache und Leichte Sprache aufbauen: Schlagwort, Schwerverstaendliche Definition, Variante Einfache Sprache, Variante Leichte Sprache. Pro Eintrag Beispielssatz. Strukturierter CSV-Output und Mustertext für 30... |
| `ls-justizportal-pruefen-spezial` | Spezialfall Justizportal in Leichte Sprache prüfen: Bayerisches Justizportal, JustizOnline, beA-Frontend. Konkrete Verbesserungsvorschlaege für Navigation, Wegleitsysteme, Antragsformulare. Prüfraster nach Inclusion Europe Regeln. |
| `ls-strafprozess-rechte-erklaeren-spezial` | Spezialfall Strafprozess-Rechte in Leichte Sprache erklaeren: § 136 StPO Belehrung, Recht zur Aussage und zum Schweigen, Pflichtverteidiger, Akteneinsicht. Mustertext und Prüfsiegel. Bedeutung für JVA-Insassen und Migrantinnen. |
| `mandantenkommunikation` | Mandantenkommunikation im Einfache und leichte Sprache im Recht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Be... |
| `mietrecht-kuendigungserklaerung` | Wohnungsmietrecht in einfacher Sprache für Mieter: Kuendigung erklaert (Frist, Form, Schriftform § 568 BGB), Schonfristzahlung § 569 Abs. 3 BGB, Mieterhoehung, Betriebskostenabrechnung. Mandantenformularsatz. |
| `nutzen-fehlerkatalog` | Nutzen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `output-waehlen` | Output-Wahl für Einfache/Leichte Sprache Jura: stimmt Adressat (Adressat mit Lese-/Lernbeeinträchtigung, Anwalt/Behörde, Übersetzer), Frist (keine harten Fristen) und Form auf den Zweck ab — typische Outputs: Bescheid in Leichter Sprache... |
| `pruefkriterien-fuer-qualitaet` | Qualitaetspruefung Einfache/Leichte Sprache: Prüfliste mit Wortlaenge, Satzlaenge, Verbquote, Fremdwortquote, Anteil Aktiv-/Passivsaetze. Empfehlung Tools (LIX-Index, Hohenheimer Verstaendlichkeitsindex). |
| `qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `qualitaetsgate-formular-portal-und-einreichung` | Qualitaetsgate: Formular, Portal und Einreichungslogik: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `qualitaetsgate-rechtsnormen-einfach` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen BITV 2.0 BGG § 11 N... |
| `quellen-livecheck` | Quellen-Live-Check für Einfache/Leichte Sprache Jura: prüft Normen (BGG § 11 Leichte Sprache, UN-BRK Art. 9/21, BFSG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Behörden mit Verständlichkeitspflicht und Quell... |
| `rechtsinhalt-interessen` | Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `rechtsinhalt-mehrparteien-konflikt-und-interessen` | Rechtsinhalt: Mehrparteienkonflikt und Interessenmatrix: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `rechtsnormen-einfach` | Rechtsnormen in Einfacher/Leichter Sprache wiedergeben: § 17 InsO wird zu 'Eine Firma muss Insolvenz anmelden, wenn sie ihre Rechnungen nicht mehr bezahlen kann. Das gilt drei Wochen nach dem Tag, an dem klar wurde, dass kein Geld da ist... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `risikoampel-gegenargumente` | Leichte: Risikoampel, Gegenargumente und Verteidigungslinien im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welch... |
| `satzbau-regeln` | Satzbau-Regeln: maximal ein Komma pro Satz in Einfacher Sprache, ueberhaupt keine Kommata in Leichter Sprache, kurze Saetze, aktive Formulierung, Subjekt vor Praedikat. Vermeidung Passiv, Substantivketten, Genitiv. |
| `sichern-internationaler-bezug-schnittstellen` | Sichern: Internationaler Bezug und Schnittstellen im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `sichern-sprache-standard` | Sichern: Internationaler Bezug und Schnittstellen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `sozialgerichtsverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht'. |
| `sozialgerichtsverfahren-strafverfahren` | Sozialgerichtsverfahren in Einfacher Sprache: Klageeinreichung Niederschrift § 90 SGG, kein Anwaltszwang, ehrenamtliche Richter. Vorlage Mandanteninformation 'Was passiert vor dem Sozialgericht' im Einfache/Leichte Sprache Jura: prüft ko... |
| `sprache-dokumentenmatrix-lueckenliste` | Sprache: Dokumentenmatrix, Lückenliste und Nachforderung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fr... |
| `sprache-dokumentenmatrix-und-lueckenliste` | Sprache: Dokumentenmatrix, Lückenliste und Nachforderung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `standard` | Standard: Verhandlung, Vergleich und Eskalation im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `standard-verhandlung-vergleich-und-eskalation` | Standard: Verhandlung, Vergleich und Eskalation: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `strafverfahren-beschuldigter` | Strafverfahren in Einfacher Sprache für Beschuldigte: Belehrung § 136 StPO, Rechte des Beschuldigten, Akteneinsicht, Wahlverteidiger/Pflichtverteidiger. Pflichtbelehrung in einfacher Sprache (BVerfG 2 BvR 1568/19). |
| `texte` | Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fris... |
| `texte-uebertragen-zielgruppe-sprachniveau` | Texte: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `uebersetzungsablauf` | Standardablauf Übersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz für Satz uebertragen, 4. Prüfen gegen Prüfliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Übersetzung. |
| `uebersetzungsablauf-wortebene-haus` | Standardablauf Übersetzung: 1. Original lesen, 2. Kernaussage extrahieren, 3. Satz für Satz uebertragen, 4. Prüfen gegen Prüfliste, 5. mit Zielgruppe gegenpruefen. Empfehlung: parallele Textspalten Original/Übersetzung im Einfache/Le... |
| `uebertragen-behoerden-gericht-und-registerweg` | Uebertragen: Behörden-, Gerichts- oder Registerweg: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `uebertragen-behoerden-gerichts-registerweg` | Uebertragen: Behörden-, Gerichts- oder Registerweg im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Z... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Einfache/Leichte Sprache Jura: trennt fehlende Tatsachen von fehlenden Belegen (Originalbescheid, Vereinfachte Fassung, Lese-Test), nennt pro Lücke Beweisthema, Beschaffungsweg (Behörden mit Verständlich... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec... |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Re... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. |
| `wortebene-haus-glossar` | Hauseigenes Glossar: typische juristische Begriffe und deren Übersetzungen. Beispiele: 'Beklagter' = 'die Person, gegen die geklagt wird'; 'Frist' = 'Zeitraum, in dem etwas getan werden muss'. Aufnahme in Kanzlei-Wiki. |
| `zielgruppe-sprachniveau-rechtsinhalt` | Zielgruppe, Sprachniveau und gesicherter Rechtsinhalt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Einfache/Leichte Sprache Jura: prüft konkret die einschlägigen Ta... |
| `zielgruppe-zahlen-schwellen-und-berechnung` | Zielgruppe: Zahlen, Schwellenwerte und Berechnung: Zielgruppe: Zahlen, Schwellenwerte und Berechnung. |
| `zielgruppe-zahlen-schwellenwerte-berechnung` | Zielgruppe: Zahlen, Schwellenwerte und Berechnung im Einfache und leichte Sprache im Recht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `zielgruppen-erkennen` | Zielgruppen erkennen: Einfache Sprache für geringe Lesekompetenz (B1), Leichte Sprache für Menschen mit Lernschwierigkeiten oder geringer Deutsch-Kenntnis. Wahl der richtigen Stufe pro Mandant/Adressat. Prüfraster und Beispiele. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
