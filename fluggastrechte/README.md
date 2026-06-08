# Fluggastrechte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fluggastrechte`) | [`fluggastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fluggastrechte – Familie Bräutigam-Zaytuna** (`fluggastrechte-familie-braeutigam`) | [Gesamt-PDF lesen](../testakten/fluggastrechte-familie-braeutigam/gesamt-pdf/fluggastrechte-familie-braeutigam_gesamt.pdf) | [`testakte-fluggastrechte-familie-braeutigam.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspätung prüfen außergewöhnliche Umstände Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstrukti… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Prüft die Einrede außergewöhnliche Umstände nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defek… |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Großkreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich o… |
| `forderungsschreiben-erste-stufe` | Erstes Forderungsschreiben an die Airline. Erfasst Anspruchsteller (alle Passagiere mit Vollmachten) Anspruchsgrundlage Art. 7 VO 261/2004 konkrete Berechnung Frist zur Zahlung (typisch zwei Wochen) Bankverbindung. In… |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und dr… |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klärt Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reise… |
| `klage-amtsgericht-fluggast` | Klageentwurf zum Amtsgericht in Fluggastrechtsangelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i. d. F. seit 01.01.2026). Örtlich wahlweise Abflughafen oder Zielflughafen … |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpässe PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankun… |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollm… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abtretung-an-fluggastportal-spezial` | Abtretung an Fluggastrechte-Portale (Flightright, EUclaim, AirHelp): Wirksamkeit nach RDG seit 2021, Provisionen, Vertragsklauseln gegenueber Mandanten. Eigene Vertretung gegen Portale, Vor- und Nachteile der Direktklage gegenueber Porta... |
| `airline-bonitaet-und-vollstreckung` | Airline-Bonitaetspruefung und Vollstreckung: Risikoliste bekannter Insolvenzen, Hinterlegung in dotierten Reisesicherungsfonds, EU-Garantien, Pruefraster bevor Klage erhoben wird. Vollstreckung im Ausland (Bruessel-I-VO, EuVTVO). Pruefli... |
| `airline-standardausreden-annullierung` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstruktionsfehler vorheriger... |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstruktionsfehler vorheriger... |
| `anlagen-bauen` | Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass Annullierungsbestätigung E-Mail-Ve... |
| `annullierung-oder-verspaetung-einordnen` | Prüfungslinie für annullierung oder verspaetung einordnen im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `annullierung-schriftsatz-brief-memo-bausteine` | Annullierung: Schriftsatz-, Brief- und Memo-Bausteine im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle,... |
| `annullierung-schriftsatz-brief-und-memo-bausteine` | Annullierung: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen... |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `anschlussflug-und-reiseplan` | Prüfungslinie für anschlussflug und reiseplan im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitssc... |
| `ausgleich-internationaler-bezug-schnittstellen` | Ausgleich: Internationaler Bezug und Schnittstellen im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Z... |
| `ausgleich-internationaler-bezug-und-schnittstellen` | Ausgleich: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Ta... |
| `ausnahmen-aussergewoehnliche-umstaende` | Prüfungslinie für ausnahmen aussergewoehnliche umstaende pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Fluggastrechte: prüft konkret... |
| `ausnahmen-aussergewoehnliche-umstaende-02` | Prüfungslinie für ausnahmen aussergewoehnliche umstaende pruefen im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `aussergewoehnliche-distanz-interessen` | Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägi... |
| `aussergewoehnliche-umstaende` | Aussergewoehnliche: Zahlen, Schwellenwerte und Berechnung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwe... |
| `aussergewoehnliche-umstaende-strikt` | Streng auszulegende aussergewoehnliche Umstaende Art. 5 Abs. 3 VO 261: Wetter, Streik nicht eigener Mitarbeiter, gerichtlich verfuegte Flugverbote, Wildschlag in Triebwerk. Keine aussergewoehnlichen Umstaende: technische Defekte (EuGH Wa... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Fluggastrechte: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereit... |
| `distanz-interessen` | Distanz: Mehrparteienkonflikt und Interessenmatrix im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Za... |
| `distanz-mehrparteien-konflikt-und-interessen` | Distanz: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tat... |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Grosskreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich oder 1500 bis 3500 km... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einfuehrung-vo-261` | Einfuehrung VO (EG) 261/2004: Anwendungsbereich (Abflug aus EU, Ankunft in EU mit EU-Carrier), Annullierung, Verspaetung ab 3 Stunden (EuGH-Sturgeon), Nichtbefoerderung. Ausgleichsstufen 250 Euro / 400 Euro / 600 Euro. Betreuungsleistung... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `erfassen-behoerden-gericht-und-registerweg` | Erfassen: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tatbes... |
| `erfassen-behoerden-gerichts-registerweg` | Erfassen: Behörden-, Gerichts- oder Registerweg im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlu... |
| `erstpruefung-rollenklaerung-mandatsziel` | Fluggastrechte: Erstprüfung, Rollenklärung und Mandatsziel im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schw... |
| `flug-anschlussflug-codeshare-anspruch` | Spezialfall Anschlussflug und Codeshare: einheitliche Buchung, ausfuehrendes Luftfahrtunternehmen, Drittland-Strecken nach EuGH wegfin. Pruefraster für Klagezuständigkeit im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerk... |
| `flug-anschlussflug-codeshare-spezial` | Spezialfall Anschlussflug und Codeshare: einheitliche Buchung, ausfuehrendes Luftfahrtunternehmen, Drittland-Strecken nach EuGH wegfin. Pruefraster für Klagezuständigkeit. |
| `flug-anspruch-uebersicht` | Uebersicht Fluggastrechte VO 261 / 2004: Annullierung, grosse Verspaetung ab drei Stunden, Nichtbefoerderung, Pauschalentschaedigung 250 Euro / 400 Euro / 600 Euro je nach Distanz. Pruefraster Anspruchsgrundlage. |
| `flug-ausserordentlicher-umstand-leitfaden` | Leitfaden ausserordentlicher Umstand: EuGH-Kasuistik Streik / Wetter / technischer Defekt, Beweislast Airline, zumutbare Massnahmen. Pruefraster für Klaegeranwalt. |
| `flug-massenklage-einfuehrung-vo` | Spezialfall Massenklage und Prozessfinanzierung in Fluggastrechten: Abtretung, Inkasso-Modelle, RDG-Grenzen, Anti-Claim-Klausel. Pruefraster für Verbraucher und Legal-Tech im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmer... |
| `flug-massenklage-prozessfinanzierung-spezial` | Spezialfall Massenklage und Prozessfinanzierung in Fluggastrechten: Abtretung, Inkasso-Modelle, RDG-Grenzen, Anti-Claim-Klausel. Pruefraster für Verbraucher und Legal-Tech. |
| `forderungsschreiben-airline` | Forderungsschreiben: Formular, Portal und Einreichungslogik im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `forderungsschreiben-erste-stufe` | Prüfungslinie für forderungsschreiben erste stufe im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbei... |
| `forderungsschreiben-formular-portal-und-einreichung` | Forderungsschreiben: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlä... |
| `forderungsschreiben-klage` | Fluggastrechte: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschläg... |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Sch... |
| `forderungsschreiben-mahnung-klage-amtsgericht` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Sch... |
| `fristen-risikoampel-mandantenkommunikation` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert pri... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Fluggastrechte: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `geltend-fristen-form-und-zustaendigkeit` | Geltend: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Ta... |
| `geltend-fristen-form-zustaendigkeit-rechtsweg` | Geltend: Fristen, Form, Zuständigkeit und Rechtsweg im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Z... |
| `kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Einstieg und Routing; Abschlussprodukt und Übergabe: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reiseplan-Konvention. Schr... |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Fluggastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument... |
| `klage` | Klage: Mandantenkommunikation und Entscheidungsvorlage im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `klage-amtsgericht-fluggast` | Prüfungslinie für klage amtsgericht fluggast im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitssch... |
| `klage-mandantenkommunikation-entscheidungsvorlage` | Klage: Mandantenkommunikation und Entscheidungsvorlage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen... |
| `live-sonderfall-edge-case` | Live: Sonderfall und Edge-Case-Prüfung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sankt... |
| `live-sonderfall-machen-mahnung-red-team-korrektur` | Live: Sonderfall und Edge-Case-Prüfung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerk... |
| `machen-dokumentenmatrix-lueckenliste` | Machen: Dokumentenmatrix, Lückenliste und Nachforderung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwell... |
| `machen-dokumentenmatrix-und-lueckenliste` | Machen: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägige... |
| `mahnung-fehlerkatalog` | Mahnung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `mahnung-red-team-und-qualitaetskontrolle` | Mahnung: Red-Team und Qualitätskontrolle; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsme... |
| `mandantenkommunikation` | Mandantenkommunikation im Fluggastrechte: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `output-waehlen` | Output wählen im Fluggastrechte: Diese Output-Weiche für Fluggastrechte entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `pauschalreise-statt-flug-pruefen` | Pauschalreise gegen Flug-Einzelbuchung: Reiseveranstalterhaftung nach §§ 651a ff. BGB, Pauschalreise-RL EU 2015 2302. Minderung, Schadensersatz, Ruecktritt. Verhaeltnis zur VO 261 (kumulativ moeglich, Anrechnung nach BGH). Pruefraster ob... |
| `pruefen-quellenkarte` | Prüfen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsprechung-beweislast-darlegungslast` | Rechtsprechung: Beweislast, Darlegungslast und Substantiierung im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `rechtsprechung-beweislast-vorverlegung-flug` | Rechtsprechung: Beweislast, Darlegungslast und Substantiierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einsc... |
| `rechtsweg-gerichtsstand-annullierung` | Rechtsweg und Gerichtsstand bei Flugverspaetung und Annullierung: Wohnsitz oder Flughafen Klaegerwahl nach EuGH Rehder. Amtsgericht bei bis 5000 Euro Streitwert. Zustaendige Schlichtungsstellen soep. Internationale Fragen Montrealer Uebe... |
| `rechtsweg-und-gerichtsstand-fluggast` | Rechtsweg und Gerichtsstand bei Flugverspaetung und Annullierung: Wohnsitz oder Flughafen Klaegerwahl nach EuGH Rehder. Amtsgericht bei bis 5000 Euro Streitwert. Zustaendige Schlichtungsstellen soep. Internationale Fragen Montrealer Uebe... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `selber-tatbestandsmerkmale-beweisfragen-beleglage` | Selber: Tatbestandsmerkmale, Beweisfragen und Beleglage im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwell... |
| `selber-tickets-umstaende` | Selber: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägige... |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse P... |
| `tickets-risikoampel-gegenargumente` | Tickets: Risikoampel, Gegenargumente und Verteidigungslinien im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sc... |
| `tickets-risikoampel-und-gegenargumente` | Tickets: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschl... |
| `umstaende-compliance-dokumentation-aktenvermerk` | Umstaende: Compliance-Dokumentation und Aktenvermerk im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle,... |
| `umstaende-compliance-dokumentation-und-akte` | Umstaende: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen T... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verifikation-fristennotiz-abtretung-an` | Verifikation: Fristennotiz und nächster Schritt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tatbes... |
| `verifikation-fristennotiz-naechster-schritt` | Verifikation: Fristennotiz und nächster Schritt im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlu... |
| `verspaetung-ticket-fluginformationen` | Verspaetung: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fluggastrechte: prüft konkret die einschlägigen Tat... |
| `verspaetung-verhandlung-vergleich-eskalation` | Verspaetung: Verhandlung, Vergleich und Eskalation im Fluggastrechte: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Za... |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollmacht mit Inhalt Bezug... |
| `vorverlegung-flug-rechtsprechung` | Vorverlegung des Fluges um mehr als 1 Stunde gilt als Annullierung nach EuGH C-188/20 Azurair. Pruefraster und Berechnungsbeispiel, wann Ausgleichsanspruch entsteht. Abgrenzung zur Umbuchung ohne Ausgleichsanspruch. Schriftsatzbausteine. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
