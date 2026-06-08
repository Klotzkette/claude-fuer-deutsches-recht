# E-Mail-Umformulierer (Berufsrechtskonform)

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`email-umformulierer-berufsrecht`) | [`email-umformulierer-berufsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/email-umformulierer-berufsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Eskalations-E-Mails Mandantenstreit — Erbengemeinschaft Aufhauser-Trenkler vs. Kanzlei Rosenmühle & Partner** (`eskalations-emails-mandantenstreit-aufhauser-kanzlei-rosenmuehle`) | [Gesamt-PDF lesen](../testakten/eskalations-emails-mandantenstreit-aufhauser-kanzlei-rosenmuehle/gesamt-pdf/eskalations-emails-mandantenstreit-aufhauser-kanzlei-rosenmuehle_gesamt.pdf) | [`testakte-eskalations-emails-mandantenstreit-aufhauser-kanzlei-rosenmuehle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-eskalations-emails-mandantenstreit-aufhauser-kanzlei-rosenmuehle.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Formuliert unfreundliche, emotionale oder unsachliche E-Mails in höfliche, sachliche und berufsrechtskonform formulierte Texte um. Der Fokus liegt auf dem anwaltlichen Berufsrecht (BRAO/BORA), mit spezialisierten Modi für Steuerberater (StBerG/BOStB), Notare (BNotO) und allgemeine berufliche Korrespondenz.

## Enthaltene Skills

| Skill | Beschreibung |
|---|---|
| `email-berufsrecht-berufliche-korrespondenz` | Höflichkeitsstandards für Korrespondenz mit Mandanten, Mitarbeitern und Geschäftspartnern ohne Berufsrechtsbezug |
| `anrede-und-grussformeln` | Hierarchie der Anreden und Schlussformeln für alle beruflichen Konstellationen |
| `bora-konformitaetspruefung` | Prüfung auf BORA-Konformität: Verschwiegenheit, Sachlichkeit, Kollegialität |
| `brao-konformitaetspruefung` | Prüfung auf BRAO-Konformität: Sachlichkeitsgebot, Werberegeln, allgemeine Berufspflichten |
| `email-eingangsanalyse` | Analyse eingehender Texte auf Konfliktgrad und emotionale Trigger |
| `emotionale-trigger-katalog` | Wörterbuch mit Ersatzformulierungen für über 25 typische Trigger |
| `frist-und-mahnung-hoeflich` | Dreistufige Mahnvorlagen von der Erinnerung bis zur Fristsetzung mit Folgehinweis |
| `ironie-und-sarkasmus-eliminieren` | Erkennung und sachliche Ersetzung ironischer und sarkastischer Stilfiguren |
| `klare-bitte-formulieren` | Sachliche Aufforderungen mit konkretem Zeitrahmen statt Forderungen |
| `kollegialitaetsgebot-pruefung` | Prüfung auf Einhaltung des § 25 BORA Kollegialitätsgebots |
| `kompetenz-zweifel-respektvoll` | Respektvolle Formulierung von Zweifeln an der fachlichen Leistung |
| `konfliktdeeskalation-formulierungen` | Über 30 deeskalierende Bausteine für angespannte Situationen |
| `kooperativer-abschluss` | Positive Schlusspassagen für konstruktive Korrespondenz |
| `mehrsprachige-umformulierung` | Höflichkeitsformeln in Englisch, Französisch, Italienisch und Spanisch |
| `notare-bnotk-modus` | Spezialmodus für notarielle Korrespondenz nach BNotO und BNotK-Richtlinien |
| `persoenlichen-angriff-entschaerfen` | Techniken: Vorwurf zur Beobachtung, Urteil zur Frage, Angriff zur Ich-Botschaft |
| `sachlichkeitsgebot-anwendung` | Tiefe Anwendung des § 43a Abs. 3 BRAO mit BVerfG-Rechtsprechung |
| `sachverhalt-neutral-darstellen` | Passivkonstruktionen, Datumsbezüge und Distanzierungsformeln |
| `steuerberater-stberg-modus` | Spezialmodus für Steuerberater-Korrespondenz nach § 57 StBerG und BOStB |
| `vorher-nachher-tabelle` | Standardisiertes Ausgabeformat mit Analyse, Änderungstabelle und überarbeitetem Text |

## Berufsrechtliche Grundlagen

### § 43a BRAO — Sachlichkeitsgebot

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### § 25 BORA — Kollegialitätsgebot

§ 25 BORA kodifiziert das Kollegialitätsgebot im Umgang unter Rechtsanwälten. Herabsetzende Äußerungen über Kollegen — auch in Mandantenschreiben — verstoßen gegen dieses Gebot. Das Eigenverschulden des Kollegen rechtfertigt keine Herabsetzung (OLG Frankfurt, mehrere Entscheidungen).

### § 57 StBerG — Gewissenhafte Berufsausübung

§ 57 Abs. 1 StBerG verpflichtet Steuerberater zu Unabhängigkeit, Gewissenhaftigkeit und Verschwiegenheit. Die Kommunikation mit Mandanten, Finanzämtern und Kollegen muss dem Vertrauen in den Berufsstand entsprechen.

### BNotO — Unparteilichkeit des Notars

§ 14 BNotO verpflichtet Notare zur unparteiischen Amtsausübung. Notarielle Korrespondenz muss diese besondere Neutralitätspflicht widerspiegeln und darf keine Parteinahme erkennen lassen.

### Rechtsprechung

Verfassungsrechtliche Aussagen zur Meinungsfreiheit und zu berufsrechtlichen Sachlichkeitspflichten werden nur nach Live-Verifikation der einschlägigen Entscheidung ausgegeben.

## Verwendung

### Beispiel-Prompt

```
Ich habe folgende E-Mail erhalten, die ich höflich und BRAO-konform beantworten möchte.
Bitte analysiere zunächst den Konfliktgrad, formuliere dann meine Antwort um und
zeige mir die Änderungen in der Vorher-Nachher-Tabelle:

[E-Mail-Text einfügen]
```

Alternativ zur direkten Umformulierung eines Eingangstexts:

```
Bitte überarbeite mein folgendes Schreiben auf BORA-Konformität und prüfe
insbesondere auf Verletzungen des Kollegialitätsgebots:

[Schreiben einfügen]
```

## Anwendungsbereiche

**Rechtsanwälte:** Überarbeitung von Mandantenschreiben, Korrespondenz mit gegnerischen Anwälten, Schreiben an Behörden und Gerichte. Fokus auf BRAO/BORA-Konformität.

**Steuerberater:** Mandantenkorrespondenz, Schreiben an Finanzämter und Finanzkassation, kollegialer Austausch. Fokus auf § 57 StBerG und BOStB.

**Notare:** Schreiben an Beteiligte, Anfragen bei Registergerichten, Amtshilfekommunikation. Fokus auf Unparteilichkeit nach § 14 BNotO.

**Allgemeine berufliche Korrespondenz:** Mitarbeiterkommunikation, Geschäftspartnerschreiben, Mandantenanschreiben ohne berufsrechtliche Anforderungen.

## Hinweis

Dieses Plugin enthält keine Testakte. Es handelt sich um Formulierungswerkzeuge für die eigenverantwortliche Anwendung durch Fachleute. Die Verantwortung für die berufsrechtliche Konformität des jeweiligen Schreibens verbleibt beim jeweiligen Berufsträger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 83 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemeine-sonderfall-edge-case` | Allgemeine: Sonderfall und Edge-Case-Prüfung im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustel... |
| `anrede-und-grussformeln` | Anrede und Grussformeln in Anwaltskorrespondenz prufen und berufsrechtskonform optimieren. § 43a BRAO § 26 BORA Kollegialitätsgebot. Prüfraster: korrekte Anrede Titel akademischer Grad Kollegialformel Schlussformel Mandantensprache. Outp... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `berufliche-fristennotiz-emotionale` | Berufliche: Fristennotiz und nächster Schritt im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrechts-E... |
| `berufliche-fristennotiz-naechster-schritt` | Berufliche: Fristennotiz und nächster Schritt im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `berufsrechtskonform-verhandlung-vergleich-und-eskalation` | Berufsrechtskonform: Verhandlung, Vergleich und Eskalation im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im B... |
| `bora-internationaler-bezug-und-schnittstellen` | Bora: Internationaler Bezug und Schnittstellen im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrechts-... |
| `bora-konformitaetspruefung` | E-Mail auf BORA-Konformität prüfen bevor sie versandt wird. §§ 6 ff. BORA allgemeine Berufspflichten § 26 BORA Werbung § 43 BORA Vertretungsverbot. Prüfraster: Sachlichkeitsgebot Werbeverbot Verschwiegenheit Interessenkonflikt unzulässig... |
| `bora-konformitaetspruefung-brao-email` | E-Mail auf BORA-Konformität prüfen bevor sie versandt wird. §§ 6 ff. BORA allgemeine Berufspflichten § 26 BORA Werbung § 43 BORA Vertretungsverbot. Prüfraster: Sachlichkeitsgebot Werbeverbot Verschwiegenheit Interessenkonflikt unzulässig... |
| `brao-interessen-fokus-formuliert` | Brao: Mehrparteienkonflikt und Interessenmatrix im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrechts... |
| `brao-konformitaetspruefung` | E-Mail auf BRAO-Konformität prüfen bevor sie versandt wird. §§ 43 43a 43b BRAO Grundpflichten Sachlichkeitsgebot Werbung. Prüfraster: Verschwiegenheitspflicht Interessenkonflikt unabhängige Berufsausübung Werbegrenzen Mandatsbeziehung. O... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin Email Umformulierer Berufsrecht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten o... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `edge-case-verhandlung-bora-international` | Allgemeine: Sonderfall und Edge-Case-Prüfung im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrechts-E-... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `email-berufsrecht-berufliche-korrespondenz` | Allgemeine berufliche E-Mail-Korrespondenz von Anwaelten professionell und berufsrechtskonform umformulieren. § 43a BRAO allgemeine Berufspflichten § 26 BORA Sachlichkeitsgebot. Prüfraster: Sachlichkeit Professionalitaet Ton Empfaengeror... |
| `email-berufsrecht-berufsrechtskonform-verhandlung-vergleich` | Berufsrechtskonform: Verhandlung, Vergleich und Eskalation im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche... |
| `email-berufsrecht-bora-internationaler-bezug-schnittstellen` | Bora: Internationaler Bezug und Schnittstellen im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `email-berufsrecht-brao-mehrparteienkonflikt-interessenmatrix` | Brao: Mehrparteienkonflikt und Interessenmatrix im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zus... |
| `email-berufsrecht-emotionale-fristen-form-zustaendigkeit` | Emotionale: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `email-berufsrecht-fokus-compliance-dokumentation-aktenvermerk` | Fokus: Compliance-Dokumentation und Aktenvermerk im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `email-berufsrecht-formuliert-erstpruefung-rollenklaerung` | Formuliert: Erstprüfung, Rollenklärung und Mandatsziel im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `email-berufsrecht-hoefliche-behoerden-gerichts-registerweg` | Hoefliche: Behörden-, Gerichts- oder Registerweg im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `email-berufsrecht-konformitaet-formular-portal-einreichungslogik` | Konformitaet: Formular, Portal und Einreichungslogik im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist... |
| `email-berufsrecht-mails-risikoampel-gegenargumente` | Mails: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche... |
| `email-berufsrecht-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechu... |
| `email-berufsrecht-sachliche-schriftsatz-brief-memo-bausteine` | Sachliche: Schriftsatz-, Brief- und Memo-Bausteine im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `email-berufsrecht-start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Email Umformulierer Berufsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsp... |
| `email-berufsrecht-unfreundliche-tatbestandsmerkmale-beweisfragen` | Unfreundliche: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. We... |
| `email-berufsrecht-unsachliche-dokumentenmatrix-lueckenliste` | Unsachliche: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welc... |
| `email-eingangsanalyse` | Eingehende E-Mail analysieren und Tonalitaet Konfliktpotenzial und Handlungsbedarf bestimmen. § 43a BRAO Berufsrecht. Prüfraster: Tonalitaet emotionale Trigger versteckte Forderungen Fristen Eskalationspotenzial. Output: Analyse-Memo Han... |
| `emotionale-fristen-form-und-zustaendigkeit` | Emotionale: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Beruf... |
| `emotionale-trigger-ironie-sarkasmus-klare` | Emotionale Trigger-Woerter und -Phrasen in Anwaltskorrespondenz identifizieren und neutralisieren. § 26 BORA Sachlichkeit § 43a BRAO Berufspflichten. Prüfraster: aggressive Formulierungen persönliche Angriffe emotionale Übertreibungen Ab... |
| `emotionale-trigger-katalog` | Emotionale Trigger-Woerter und -Phrasen in Anwaltskorrespondenz identifizieren und neutralisieren. § 26 BORA Sachlichkeit § 43a BRAO Berufspflichten. Prüfraster: aggressive Formulierungen persönliche Angriffe emotionale Übertreibungen Ab... |
| `fokus-compliance-dokumentation-und-akte` | Fokus: Compliance-Dokumentation und Aktenvermerk im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrecht... |
| `formuliert-erstpruefung-und-mandatsziel` | Formuliert: Erstprüfung, Rollenklärung und Mandatsziel im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Beruf... |
| `formulierte-quellenkarte` | Formulierte Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `frist-und-mahnung-hoeflich` | Fristsetzungen und Mahnungen in Anwaltskorrespondenz hoeflich und dennoch rechtsverbindlich formulieren. § 286 BGB Schuldnerverzug § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Fristklarheit Verbindlichkeit Ton kollegiale Formulierung f... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin Email Umformulierer Berufsrecht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder... |
| `hoefliche-konformitaet-mails` | Hoefliche: Behörden-, Gerichts- oder Registerweg im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrecht... |
| `ironie-und-sarkasmus-eliminieren` | Ironische oder sarkastische Formulierungen in Anwaltskorrespondenz erkennen und berufsrechtlich einwandfrei neutralisieren. § 26 BORA Sachlichkeitsgebot § 43a BRAO. Prüfraster: Ironie-Erkennung Sarkasmus versteckte Abwertungen implizite... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Email Umformulierer Berufsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsp... |
| `klare-bitte-formulieren` | Unklare oder versteckte Bitten und Forderungen in Anwaltskorrespondenz klar und direkt formulieren. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Klarheit der Bitte Unmissverstaendlichkeit Handlungsaufforderung Reaktionsfrist. Output: k... |
| `kollegialitaetsgebot-kompetenz-zweifel` | E-Mail auf Einhaltung des Kollegialitätsgebots gegenüber Kollegen und Kolleginnen prüfen. § 43a Abs. 3 BRAO § 26 BORA Kollegialität. Prüfraster: kollegiale Formulierungen fehlende Abwertungen sachliche Kritik professioneller Umgangston.... |
| `kollegialitaetsgebot-pruefung` | E-Mail auf Einhaltung des Kollegialitätsgebots gegenüber Kollegen und Kolleginnen prüfen. § 43a Abs. 3 BRAO § 26 BORA Kollegialität. Prüfraster: kollegiale Formulierungen fehlende Abwertungen sachliche Kritik professioneller Umgangston.... |
| `kompetenz-zweifel-respektvoll` | Zweifel an Kompetenz oder Entscheidung des Gegners oder Kollegen respektvoll und sachlich aeussern. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: sachliche Kritik ohne Abwertung Begründung Quellenangabe professioneller Ton. Output: uebe... |
| `konfliktdeeskalation-formulierungen` | Eskalierte oder hitzige Korrespondenz deeskalieren und konstruktive Kommunikationsbasis herstellen. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Eskalationsniveau Interessenidentifikation deeskalierende Formulierungen Angebote zur Lösu... |
| `konformitaet-formular-portal-und-einreichung` | Konformitaet: Formular, Portal und Einreichungslogik im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsr... |
| `kooperativer-abschluss` | E-Mail oder Schreiben mit kooperativem und prozessfoerderlichem Abschluss versehen. § 43a BRAO § 26 BORA. Prüfraster: offen für Gespraeich konstruktiver Ausblick ohne Überversprechung. Output: optimierter Abschlusssatz mit Erklärung. Abg... |
| `kooperativer-abschluss-mehrsprachige` | E-Mail oder Schreiben mit kooperativem und prozessfoerderlichem Abschluss versehen. § 43a BRAO § 26 BORA. Prüfraster: offen für Gespraeich konstruktiver Ausblick ohne Überversprechung. Output: optimierter Abschlusssatz mit Erklärung. Abg... |
| `mails-risikoampel-und-gegenargumente` | Mails: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im B... |
| `mandantenkommunikation` | Mandantenkommunikation im Plugin Email Umformulierer Berufsrecht: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder B... |
| `mehrsprachige-umformulierung` | Anwaltskorrespondenz in einer anderen Sprache berufsrechtskonform und sachgerecht umformulieren. § 43a BRAO §§ 26 ff. BORA internat. Anwaltsstandards. Prüfraster: Aequivalenz der Rechtsbegriffe Sachlichkeit Kollegialität Zielkultur. Outp... |
| `notare-beweislast-darlegungslast` | Notare: Beweislast, Darlegungslast und Substantiierung im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fri... |
| `notare-beweislast-sachliche-texte` | Notare: Beweislast, Darlegungslast und Substantiierung im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Beruf... |
| `notare-bnotk-modus` | Korrespondenz von Notaren und Notarinnen auf notarrechtliche Besonderheiten und BNotK-Vorgaben anpassen. §§ 14 17 BNotO § 26 BRAO analog. Prüfraster: neutrale Beurkundsrolle Unparteilichkeit Gebotes zur Unabhängigkeit Urkundssprache. Out... |
| `output-waehlen` | Output wählen im Plugin Email Umformulierer Berufsrecht: Diese Output-Weiche für Email Umformulierer Berufsrecht entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schrit... |
| `persoenlichen-angriff-entschaerfen` | Persoenliche Angriffe und Beleidigungen in Anwaltskorrespondenz erkennen und durch sachliche Formulierungen ersetzen. § 43a BRAO § 26 BORA Sachlichkeitsgebot. Prüfraster: persönliche Angriffe Beleidigungen herabsetzende Formulierungen. O... |
| `persoenlichen-angriff-sachlichkeitsgebot` | Persoenliche Angriffe und Beleidigungen in Anwaltskorrespondenz erkennen und durch sachliche Formulierungen ersetzen. § 43a BRAO § 26 BORA Sachlichkeitsgebot. Prüfraster: persönliche Angriffe Beleidigungen herabsetzende Formulierungen. O... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `sachliche-schriftsatz-brief-und-memo-bausteine` | Sachliche: Schriftsatz-, Brief- und Memo-Bausteine im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrec... |
| `sachlichkeitsgebot-anwendung` | Sachlichkeitsgebot nach § 26 BORA auf konkrete Korrespondenz anwenden und Verbesserungen vornehmen. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: unsachliche Formulierungen Emotionalisierung Abwertungen Versachlichungspotenzial. Output:... |
| `sachverhalt-neutral-darstellen` | Sachverhalt in Anwaltskorrespondenz neutral und ohne wertende Parteinahme darstellen. § 43a BRAO Sachlichkeit §§ 86 ff. ZPO Sachverhaltspflicht. Prüfraster: Parteinahme Wertungen Auslassungen Einseitigkeit neutrale Formulierungen. Output... |
| `steuerberater-mandantenentscheidung` | Steuerberater: Mandantenkommunikation und Entscheidungsvorlage im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung... |
| `steuerberater-stberg-allgemeine-berufliche` | Korrespondenz von Steuerberatern auf StBerG- und Berufsrechts-Konformität anpassen. §§ 57 57a StBerG Berufspflichten DVStB. Prüfraster: Verschwiegenheit Sachlichkeit Werbegrenzen fachliche Kompetenz Unabhängigkeit. Output: angepasste Ver... |
| `steuerberater-stberg-modus` | Korrespondenz von Steuerberatern auf StBerG- und Berufsrechts-Konformität anpassen. §§ 57 57a StBerG Berufspflichten DVStB. Prüfraster: Verschwiegenheit Sachlichkeit Werbegrenzen fachliche Kompetenz Unabhängigkeit. Output: angepasste Ver... |
| `texte` | Texte: Zahlen, Schwellenwerte und Berechnung im Plugin Email Umformulierer Berufsrecht: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustel... |
| `texte-zahlen-schwellen-und-berechnung` | Texte: Zahlen, Schwellenwerte und Berechnung im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Berufsrechts-E-... |
| `umform-anwaltsbrief-an-gegner-spezial` | Spezialfall Anwaltsbrief an Gegner: anwaltliche Sorgfaltspflicht, kein unsachlicher Vorwurf, klare Forderung mit Frist. Pruefraster für Risikomanagement. |
| `umform-eilgespraech-zusammenfassung` | Spezialfall Zusammenfassung eines Eilgespraechs als E-Mail an Mandant: Sachverhalt, Optionen, Entscheidungsvorschlag, Frist. Pruefraster für Mandant im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Be... |
| `umform-eilgespraech-zusammenfassung-spezial` | Spezialfall Zusammenfassung eines Eilgespraechs als E-Mail an Mandant: Sachverhalt, Optionen, Entscheidungsvorschlag, Frist. Pruefraster für Mandant. |
| `umform-tonalitaet-bauleiter` | Bauleiter Tonalitaet für Anwalts-E-Mail: sachlich, foerdernd, deeskalierend. Pruefraster für Mandanten- und Kollegenkorrespondenz. |
| `umform-vertraulichkeitshinweise-leitfaden` | Leitfaden Vertraulichkeits- und Geheimnishinweise in Anwalts-E-Mails: Mandantengeheimnis, Datenschutz, Disclaimer. Pruefraster für Standardsignatur. |
| `unfreundliche-unsachliche-umform-anwaltsbrief` | Unfreundliche: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung... |
| `unsachliche-dokumentenmatrix-und-lueckenliste` | Unsachliche: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin email umformulierer berufsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `varianten-fehlerkatalog` | Varianten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `vorher-nachher` | Vorher Nachher im Plugin Email Umformulierer Berufsrecht im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nä... |
| `vorher-nachher-tabelle` | Vorher-Nachher-Vergleich für umformulierte Anwaltskorrespondenz erstellen und Aenderungen erklären. § 43a BRAO § 26 BORA. Prüfraster: Vollständigkeit Erklärbarkeit jeder Aenderung Berufsrechtsbezug. Output: Tabelle mit Original Überarbei... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefer... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Berufsrechts-E-Mail: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
