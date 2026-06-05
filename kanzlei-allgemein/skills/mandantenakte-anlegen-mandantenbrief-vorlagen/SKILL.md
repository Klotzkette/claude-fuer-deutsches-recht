---
name: mandantenakte-anlegen-mandantenbrief-vorlagen
description: "Mandantenakte Anlegen Mandantenbrief Vorlagen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenakte Anlegen Mandantenbrief Vorlagen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Mandantenakte Anlegen Mandantenbrief Vorlagen** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandantenakte-anlegen` | Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmaechtigte Mandatsumfang Konfliktprüfung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwäsche-Identifizierung (§§ 10 11 GwG) Honorarvereinbarung oder RVG-Hinweis. Erzeugt Aktenstruktur unter mandate/Aktenzeichen/ mit Standardunterordnern Vollmachts-Entwurf Datenschutzhinweis Geldwäsche-Prüfbeleg. Eintrag im Mandantenstamm. Verbindung zum Fristenbuch falls Fristen mitgeliefert. |
| `mandantenbrief-vorlagen` | Standardvorlagen für den Mandantenbrief der Kanzlei. Aufbau Anrede Bezug Sachstand Empfehlung naechste Schritte Frist Kostenhinweis Unterschrift mit Berufsbezeichnung. Verschiedene Vorlagen für Mandatseroeffnung Zwischenbericht Beratungsergebnis Abschlussbericht Schlussrechnung. Hauptregel klar verstaendlich kein Juristenjargon ohne Erklärung. Bei Mandantenkommunikation auf Mandantenseite Rolle prüfen (Verbraucher vs Geschäftskunde). Disclaimer und Kostenhinweis Pflicht. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Mandantenakte Anlegen Mandantenbrief Vorlagen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandantenakte-anlegen`

**Fokus:** Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmaechtigte Mandatsumfang Konfliktprüfung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwäsche-Identifizierung (§§ 10 11 GwG) Honorarvereinbarung oder RVG-Hinweis. Erzeugt Aktenstruktur unter mandate/Aktenzeichen/ mit Standardunterordnern Vollmachts-Entwurf Datenschutzhinweis Geldwäsche-Prüfbeleg. Eintrag im Mandantenstamm. Verbindung zum Fristenbuch falls Fristen mitgeliefert.

# Mandantenakte anlegen

## Konfliktprüfung (§ 43a Abs. 4 BRAO)

**Vor jeder Mandatsannahme** Pflichtschritt:

- Prüfung im Mandantenstamm ob Mandat gegen einen bisherigen oder laufenden Mandanten der Kanzlei.
- Prüfung ob Mandatsannahme gegen § 3 BORA (widerstreitende Interessen) verstoesst.
- Bei Konflikt: Mandat ablehnen oder schriftliches Einverständnis aller Betroffenen.
- Prüfer-Eintrag mit Datum Initialen.

## Aktennummernsystem

Empfehlung:

`<Jahr>/<lfd. Nr.>` (z. B. `2026/0042`)

oder

`<RG>-<Jahr>-<Nr>` (z. B. `Z-2026-0042` für Zivilrecht).

## Verzeichnisstruktur

Unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandate/<az>/`:

```
01_stammdaten/
 mandatsblatt.md
 vollmacht.docx
 vollmacht-unterschrieben.pdf
 datenschutzhinweis.md
 gwg-identifizierung.pdf
 konfliktprüfung.md
 honorarvereinbarung.docx (falls Vereinbarung)
02_eingaenge/
03_schriftsaetze/
04_anlagen/
05_fristen/
06_honorar/
 rechnungen/
 zahlungseingang.yaml
07_korrespondenz_mandant/
08_korrespondenz_dritte/
09_aktennotizen/
_archiv/
```

## Mandatsblatt

```yaml
mandat-az: 2026/0042
mandat-eroeffnet: 2026-05-20
zustaendiger-anwalt: RA Mueller
sekretariat: Frau Schmidt

mandant:
 typ: juristische-person # juristische-person / natürliche-person / ehepaare-vergleichsweise
 name: Mueller GmbH
 anschrift: ...
 rechtsform: GmbH
 vertretungsberechtigte: Hans Mueller (Geschäftsführer)
 registergericht: HRB ... AG München
 ust-id: DE...
 steuernummer: ...

ansprechpartner:
 name: Hans Mueller
 funktion: Geschäftsführer
 telefon: ...
 e-mail: ...

mandatsumfang:
 beschreibung: Verteidigung in Zivilrechtsstreit gegen ABC GmbH (Klage)
 rechtsgebiet: Zivilrecht / Vertragsrecht
 instanz: 1. Instanz LG München
 streitwert: 35.000 EUR

honorar:
 basis: rvg # rvg / vereinbarung
 stundensatz: 320 # bei Vereinbarung
 pkh-pruefung: nein

konfliktpruefung:
 erfolgt-am: 2026-05-20
 ergebnis: kein-konflikt
 geprueft-von: RA Mueller
```

## Vollmacht

Vollmachtstext mit:

- Beauftragung des Rechtsanwalts der Kanzlei.
- Mandatsumfang konkret bezeichnet (Vorverfahren Klage Vergleich auch über Klageweg hinaus).
- Untervollmacht und Substituierung.
- Empfangsvollmacht für Zustellungen.
- beA-Vollmacht.
- Datum und Unterschrift des Mandanten.

## Datenschutzhinweis (Art. 13 DSGVO)

Standardhinweis mit:

- Identität des Verantwortlichen (Kanzlei).
- Zweck der Verarbeitung (Mandatsdurchführung).
- Rechtsgrundlage (Art. 6 Abs. 1 lit. b DSGVO + § 50 BRAO Aktenführung).
- Empfänger (Gericht Behörde Steuerberater Gegenseite — je nach Bedarf).
- Speicherdauer (mindestens 6 Jahre nach Mandatsende § 50 Abs. 1 BRAO).
- Betroffenenrechte (Auskunft Berichtigung Löschung Widerspruch).

## Geldwäsche-Identifizierung (§§ 10 11 GwG)

Bei Mandaten die unter GwG fallen (z. B. Immobilientransaktionen Bargeldgeschäfte ab Schwellenwert):

- Identifizierung der natürlichen Person mit Lichtbildausweis Kopie.
- Bei juristischer Person Registerauszug HRB plus wirtschaftlich Berechtigte nach Transparenzregister.
- Prüfung gegen Sanktionslisten EU und nationale.
- Prüfer-Eintrag mit Datum Initialen.

## Mandantenstamm-Eintrag

In `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandantenstamm.yaml`:

```yaml
- mandant-id: M-00874
 name: Mueller GmbH
 typ: juristische-person
 mandate:
 - 2026/0042
 konfliktstatus: kein-konflikt
 letzte-pruefung: 2026-05-20
```

## Audit

- Aktenanlage mit Audit-Eintrag (Datum Anwalt Sekretariat).
- Änderungen mit Audit-Trail.

## Ausgabe

- Vollständige Aktenstruktur.
- Mandatsblatt und Pflichtdokumente.
- Eintrag im Mandantenstamm.
- Hinweis ans Fristenbuch falls Fristen sofort relevant.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `mandantenbrief-vorlagen`

**Fokus:** Standardvorlagen für den Mandantenbrief der Kanzlei. Aufbau Anrede Bezug Sachstand Empfehlung naechste Schritte Frist Kostenhinweis Unterschrift mit Berufsbezeichnung. Verschiedene Vorlagen für Mandatseroeffnung Zwischenbericht Beratungsergebnis Abschlussbericht Schlussrechnung. Hauptregel klar verstaendlich kein Juristenjargon ohne Erklärung. Bei Mandantenkommunikation auf Mandantenseite Rolle prüfen (Verbraucher vs Geschäftskunde). Disclaimer und Kostenhinweis Pflicht.

# Mandantenbrief-Vorlagen


## Triage zu Beginn
1. Welcher Brieftyp wird benoetigt: Mandatseröffnung, Zwischenbericht, Beratungsergebnis, Abschlussbericht oder Schlussrechnung?
2. Ist der Mandant Verbraucher (§ 13 BGB) oder Unternehmer (§ 14 BGB) — wegen Sprache und Belehrungspflichten?
3. Muss eine Kostenbelehrung (§ 49b Abs. 5 BRAO) oder ein Datenschutzhinweis (Art. 13 DSGVO) beigefuegt werden?
4. Soll das Schreiben postalisch, per E-Mail oder ueber beA versandt werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 49b Abs. 5 BRAO — Pflicht zur Kostenbelehrung bei Auftragsannahme
- Art. 13 DSGVO — Informationspflicht bei Ersterhebung personenbezogener Daten (Mandantenaufnahme)
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch fuer Inhalte im Mandantenbrief
- § 2 BORA — Gewissenhaftigkeit: verstaendliche und klare Kommunikation mit dem Mandanten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Allgemeine Aufbauregel

```
[Briefkopf der Kanzlei]

[Datum]
[Mandantenadresse]

Aktenzeichen: 2026/0042

In dem Mandat ... / In Sachen ...

[Anrede]

[Sachstand: knapp und chronologisch]

[Empfehlung: konkret und begründet]

[Nächste Schritte / Frist]

[Kostenhinweis]

[Schluss / Unterschrift mit Berufsbezeichnung]
```

## Sprachregeln

- **Klar verständlich**: kein Juristenjargon ohne Erklärung in Klammern.
- **Aktiv statt passiv**: "Wir haben Berufung eingelegt" statt "Es wurde Berufung eingelegt".
- **Konkrete Daten und Fristen**: "bis 15.06.2026" statt "in den nächsten Wochen".
- **Kostenhinweis pflichtig**: Hinweis auf RVG oder Honorarvereinbarung.
- **Disclaimer bei rechtlich schwierigen Punkten**: Empfehlung wird benannt aber Letztentscheidung beim Mandanten.

## Vorlagen

### V1 — Mandatseröffnung

```
Sehr geehrter Herr Mueller,

vielen Dank für das uns entgegengebrachte Vertrauen. Wir haben das
Mandat in der Sache (...) unter dem oben genannten Aktenzeichen
eroeffnet.

Vereinbarung der Sache nach Ihrer Schilderung:
- Sachverhalt: ...
- Ihr Ziel: ...
- Nächste Schritte aus unserer Sicht: ...
- Voraussichtliche Dauer: ...

Honorar:
Wir rechnen nach RVG / nach Honorarvereinbarung (siehe beiliegende
Vereinbarung). Voraussichtliche Kosten in dieser Sache: (Betrag) EUR
plus Auslagen plus Umsatzsteuer.

Vollmacht:
Anbei finden Sie unsere Vollmacht zur Unterschrift. Bitte senden Sie
diese unterzeichnet binnen einer Woche an uns zurück.

Wir melden uns spaetestens am (Datum) bei Ihnen mit dem ersten
Zwischenbericht.

Mit freundlichen Grüßen

[Anwalt]
Rechtsanwalt
Fachanwalt für ...
```

### V2 — Zwischenbericht

```
Sehr geehrter Herr Mueller,

in der oben bezeichneten Sache geben wir Ihnen folgenden Zwischenbericht:

Sachstand:
- (Datum) wir haben (Schritt) durchgeführt
- (Datum) Gegenseite / Behörde / Gericht hat (Schritt) eingeleitet
- aktueller Stand: ...

Nächste Schritte:
Wir werden (Schritt) bis (Datum) erledigen.

Wenn Sie nichts unternehmen sollten oder wir von Ihnen nichts hoeren
gehen wir wie folgt vor: ...

Kostenstand bisher:
Aufgewendete Stunden: (Anzahl)
Voraussichtliche Zwischenrechnung: (Betrag) EUR

Bei Rückfragen melden Sie sich gerne.

Mit freundlichen Grüßen

[Anwalt]
```

### V3 — Beratungsergebnis (kurze Rechtsauskunft)

```
Sehr geehrter Herr Mueller,

zu Ihrer Anfrage vom (Datum) teile ich Ihnen meine rechtliche
Einschätzung mit:

Frage:
[Präzise Frage des Mandanten]

Kurzantwort (eine Zeile):
[Ja / Nein / Differenziert]

Begründung (vereinfacht):
[Klar und verstaendlich, ohne unnoetigen Jargon. Bei Verwendung
juristischer Begriffe in Klammern erklaeren]

Nächste Schritte:
[Konkret]

Risiken:
[Was könnte schiefgehen oder unsicher sein]

Kostenhinweis:
Diese Beratung wird nach RVG / Honorarvereinbarung mit (Betrag) EUR
zuzueglich Umsatzsteuer berechnet.

Mit freundlichen Grüßen

[Anwalt]
```

### V4 — Abschlussbericht

```
Sehr geehrter Herr Mueller,

mit dem heutigen Tag ist das Mandat in der Sache (...) abgeschlossen.

Ergebnis:
[Was erreicht wurde]

Verbleibende offene Punkte:
[Falls vorhanden]

Schlussrechnung:
Die Schlussrechnung über den noch offenen Honorarbetrag finden Sie als
Anlage. Bitte überweisen Sie den Betrag bis (Datum).

Aktenherausgabe:
Sollten Sie Original-Belege aus der Akte zurückhaben wollen teilen Sie
uns dies bitte mit. Die Akte wird im Uebrigen sechs Jahre lang
aufbewahrt § 50 BRAO.

Wir bedanken uns für das uns entgegengebrachte Vertrauen.

Mit freundlichen Grüßen

[Anwalt]
```

### V5 — Eilbenachrichtigung

```
Sehr geehrter Herr Mueller,

EILT — bitte heute oder morgen reagieren.

In der Sache (...) ist heute eine wichtige Nachricht / Zustellung
eingegangen die eine kurzfristige Reaktion erfordert.

Sachverhalt:
[knapp]

Empfehlung:
[knapp]

Bitte melden Sie sich bis (Datum) telefonisch oder per E-Mail bei uns.
Bei Nichterreichen versuchen wir es weiter und werden zur Wahrung der
Frist (Schritt) unternehmen.

Mit freundlichen Grüßen

[Anwalt]
```

## Versand

Vor Versand der Skill `versand-vor-check` aus diesem Plugin. Eintrag im Postausgang.
