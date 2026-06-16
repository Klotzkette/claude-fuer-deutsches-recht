---
name: klagevorlage-aus-eigenen-mustern
description: "Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung online Sachverhalt-Dialog. Output: Klageschrift DOCX und Markdown plus Mini-Plugin ZIP für naechste Klagen ohne erneute Extraktion. Abgrenzung zu klage-aus-eigenem-skill (Nutzung des Plugins) und inkasso-zahlungsklage-ersteller."
---

# Klagewerkstatt — Lernlauf aus eigenen Mustern

## Zweck

Dieser Skill ist der **Lernlauf** der Klagewerkstatt. Er macht in einem Durchgang vier Dinge:

1. Aus eigenen Klagemustern, Urteilen, Kommentaren, Aufsätzen und Formatvorlagen wird eine **hauseigene generische Standardklage-Vorlage** destilliert (Markdown + DOCX, mit Platzhaltern).
2. Der Sachverhalt wird im Dialog und aus weiteren hochgeladenen Dokumenten eingesammelt und in die Vorlage gespiegelt.
3. **Online-Prüfung der Zuständigkeit** ist Pflicht: justizadressen.nrw.de und justiz.de Gerichtssuche. Streitwert → AG/LG; Beklagtenadresse → örtliche Zuständigkeit; Sondertatbestände beachten.
4. Aus den extrahierten Hausregeln wird ein **eigenes Mini-Plugin als ZIP** generiert (`klagewerkstatt-<kanzlei>.zip`), das in Claude Code direkt installierbar ist und beim nächsten Mal ohne erneute Extraktion in der hauseigenen Vorlage produziert (siehe Schwester-Skill `klage-aus-eigenem-skill`).

Memo (rechtliche Würdigung) wird **nur auf ausdrückliche Anfrage** erstellt.

## Ablauf

**Schritt 1 — Kanzlei-Profil**
Einmal abfragen und merken:

> Kanzleiname, Rechtsanwältin/Rechtsanwalt mit Anschrift, BeA-SAFE-ID, AGB-Klausel zum Gerichtsstand (sofern für Verbraucher unzulässig nach § 29c ZPO klar abgrenzen), übliche Mandantengruppe (B2B, B2C, gemischt), bevorzugte Zinsformel (Basiszins+5/+9, §§ 288 Abs. 1/2 BGB), Standard-Anlagenliste (z. B. Rechnung, Auftragsbestätigung, Mahnungen, Lieferschein, AGB).

**Schritt 2 — Materialaufnahme (Lernkorpus)**
Den Nutzer bitten, alle einschlägigen Eigenmaterialien hochzuladen oder per Pfad zu nennen:

- Eigene Klage-Muster (mind. 2, gern 5–15) als DOCX, PDF, MD, TXT.
- Urteile zur eigenen Forderungspraxis (Volltexte oder Auszüge).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Format- und Layout-Vorlagen (Briefkopf-DOCX, Schriftarten, Nummerierung).
- Optional: typische Mahnschreiben, Verzugsbriefe, RVG-Berechnungen.

Bei Schweigen mit den im Plugin liegenden Leervorlagen unter `assets/vorlagen-leer/` arbeiten und das im Endprodukt transparent kennzeichnen.

**Schritt 3 — Extraktion der Hausregeln**
Aus dem Lernkorpus extrahieren (Zusammenfassung am Schluss dem Nutzer vorlegen):

- Aufbau der Klageschrift (Rubrum, Anträge, Begründung, Beweismittel, Anlagen, Schluss).
- Standardklauseln: Antragswortlaut, Zinsantrag, vorgerichtliche RA-Kosten als Nebenforderung, Mahnverzugsbeginn, Verzugszinsen (§§ 286, 288 BGB), Verzugsschaden (§ 280 BGB).
- Tonalität: knapp/ausführlich; aktiv/passiv; Direktanrede des Gerichts.
- Zitierweise: Pinpoint, Randnummer, jüngere BGH-Entscheidungen zuerst, deutsche Kommentartradition.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anlagenstrategie und Anlagensigel (K1, K2, …).

**Schritt 4 — Hauseigene Standardvorlage erzeugen**
Aus den Hausregeln eine **generische Klage-Vorlage** schreiben:

- Format: Markdown (Vorlage in `assets/vorlagen-leer/standardklage.md`) und parallel DOCX (über `office/docx`-Skill). Layout aus dem mitgelieferten Briefkopf, sonst Klotzkette-Default.
- Platzhalter strikt in geschweiften Doppelklammern: `{{kanzlei.briefkopf}}`, `{{rubrum.klagepartei}}`, `{{rubrum.beklagte}}`, `{{rubrum.bevollmaechtigte}}`, `{{gericht.bezeichnung}}`, `{{gericht.adresse}}`, `{{gericht.bea_safe_id}}`, `{{streitwert.eur}}`, `{{antrag.hauptforderung}}`, `{{antrag.zinsen}}`, `{{antrag.kosten}}`, `{{sachverhalt}}`, `{{rechtliche_würdigung}}`, `{{anlagen.liste}}`, `{{ort_datum}}`, `{{unterschrift}}`.
- Standardabschnitte enthalten Hausregel-Bausteine.

**Schritt 5 — Sachverhalt einsammeln**
Strukturierte Rückfragen (alle als Liste auf einmal stellen, damit der Nutzer in einem Schwung antworten kann):

- Forderungsgrund (Kauf, Werkvertrag, Dienstvertrag, Darlehen, Miete, sonstiges) mit kurzer Vertragsbeschreibung.
- Beklagte(r): Name, Anschrift, Rechtsform, ggf. gesetzliche Vertretung; **Anschrift exakt** für die Zuständigkeitsprüfung.
- Hauptforderung in EUR, Fälligkeitsdatum, etwaige Teilzahlungen.
- Mahnungen mit Datum, Form und Inhalt; Mahnverzugseintritt.
- Vorgerichtliche RA-Kosten als Nebenforderung (Geschäftsgebühr Nr. 2300 VV RVG, Anrechnung Vorbem. 3 Abs. 4 VV RVG).
- Beweismittel: Urkunden, Zeugen, Sachverständige, Parteivernehmung, Augenschein.
- Besonderheiten: Verbrauchereigenschaft des Beklagten, AGB-Gerichtsstand, Erfüllungsort, ausländische Beteiligung (EuGVVO/Brüssel Ia VO 1215/2012).

Zusätzlich Dokumenten-Drop akzeptieren (Rechnungen, Mahnungen, Korrespondenz). Aus diesen Dokumenten Felder automatisch befüllen und die Belegung jeweils kennzeichnen.

**Schritt 6 — Zuständigkeit online prüfen (Pflicht)**

Pflichtschritt vor Auslieferung. Reihenfolge:

1. **Sachliche Zuständigkeit** rechnerisch: Streitwert ≤ 10.000 EUR → AG (§ 23 Nr. 1 GVG i. d. F. seit 1.1.2026); > 10.000 EUR → LG (§ 71 GVG). Sondertatbestände beachten: Wohnraummietsachen AG ohne Streitwertgrenze (§ 23 Nr. 2a GVG), Nachbarschaftsstreitigkeiten AG (§ 23 Nr. 2e GVG), Familiensachen FamG, Handelssachen Kammer für Handelssachen (§§ 95, 96 GVG).
2. **Örtliche Zuständigkeit** rechtlich: allgemeiner Gerichtsstand der Beklagten (§§ 12, 13 ZPO). Erfüllungsort (§ 29 ZPO) prüfen — bei Geldschulden Sitz der Klagepartei nur bei qualifizierter Schickschuld, sonst Wohnsitz Beklagte. Verbraucher-Sondertatbestand § 29c ZPO. AGB-Gerichtsstand prüfen, aber bei Verbrauchern nach § 38 ZPO unwirksam.
3. **Online-Adressrecherche** (immer ausführen):
   - Für NRW-Anschriften: `pplx content fetch "https://www.justizadressen.nrw.de/de/justiz/suche?suchbegriff=<PLZ_oder_Ort>"` (PLZ oder Ort der Beklagten). Wenn PLZ allein nicht reicht, mit Ort nachfassen.
   - Bundesweit ergänzend: `pplx content fetch "https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php"` und Landes-Justizportale.
   - Treffer prüfen und Bezeichnung, Postanschrift, Telefax und — wo bekannt — die BeA-EGVP-SAFE-ID (Bundesweites elektronisches Adressverzeichnis SAFE, abrufbar in beA bzw. unter justiz.de) einsetzen. Wenn keine SAFE-ID gelistet, mit dem Hinweis "EGVP-Adresse über beA-Adressbuch (SAFE-ID) zu ergänzen" markieren.
4. Quelle und Abrufdatum stets im Output ausweisen (Anlage `Zuständigkeitsprüfung`).

**Schritt 7 — Klageschrift erzeugen**

- **Immer**: `Klage-<Beklagte>-<YYYYMMDD>.docx` (über `office/docx`) und Spiegel `Klage-<Beklagte>-<YYYYMMDD>.md`.
- Anlagenkonvolut als Liste mit K-Sigeln; Anlagenkopfbogen optional.
- **Padlet** (auf Wunsch): single-file HTML aus `assets/padlet/klage-padlet.html` mit Live-Vorschau und Pflegefeldern; speichert in `localStorage`.

**Schritt 8 — Eigenes Mini-Plugin als ZIP erzeugen**

Aus den Hausregeln und der Standardvorlage wird ein eigenes Plugin gepackt:

- Skript: `python scripts/plugin_aus_hausregeln.py --kanzlei "<Name>" --vorlage <pfad.md> --regeln <regeln.json> --ziel <ziel.zip>`.
- Inhalt des ZIP:
  - `klagewerkstatt-<slug>/.claude-plugin/plugin.json` (Name `klagewerkstatt-<slug>`, Version 0.1.0).
  - `klagewerkstatt-<slug>/skills/klage-erstellen/SKILL.md` (siehe Schwester-Skill `klage-aus-eigenem-skill` als Bauanleitung; im erzeugten Plugin lebt die Skill-Datei eigenständig).
  - `klagewerkstatt-<slug>/assets/vorlage/standardklage.md` und `.docx`.
  - `klagewerkstatt-<slug>/references/hausregeln.json`, `belegmuster.md`, `anlagenliste.md`, `zustaendigkeit-quellen.md`.
  - `klagewerkstatt-<slug>/README.md` mit Abrufhinweis und Installationsanleitung.
- ZIP-Dateiname `klagewerkstatt-<slug>.zip`. Datei dem Nutzer zum Download geben mit Installationsanweisung für Claude Code (`Customize Plugins → Install from .zip`).

**Schritt 9 — Memo (nur auf Anfrage)**

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Anspruchsgrundlagen, Beweislage und Prozessrisiken erstellen?

Bei Zustimmung: zwei Seiten, DOCX oder Markdown.

## Rechtlicher Rahmen

### Pflichtinhalte und Form der Klageschrift
- **§ 253 Abs. 2 ZPO** Klageinhalt (Parteien, Gericht, Anträge, Sachverhalt, Beweismittel).
- **§ 130 ZPO** Form der Schriftsätze; **§ 130a ZPO** elektronisches Dokument; **§ 130d ZPO** Pflicht zur elektronischen Einreichung für Rechtsanwältinnen und Rechtsanwälte (beA).
- **§ 78 ZPO** Anwaltszwang vor LG aufwärts.
- **§ 12 RVG / Anlage 2 VV RVG**: Gebührentabelle; **Nr. 2300 VV RVG** Geschäftsgebühr; **Vorbem. 3 Abs. 4 VV RVG** Anrechnung 0,65; **Nr. 3100 VV RVG** Verfahrensgebühr.

### Sachliche Zuständigkeit
- **§ 23 Nr. 1 GVG** AG bis 10.000 EUR (i. d. F. seit 1.1.2026).
- **§ 71 GVG** LG über 10.000 EUR.
- **§ 23 Nr. 2a GVG** Wohnraummietsachen AG ohne Streitwertgrenze.

### Örtliche Zuständigkeit
- **§§ 12, 13 ZPO** allgemeiner Gerichtsstand der Beklagten.
- **§ 17 ZPO** Sitz juristischer Personen.
- **§ 29 ZPO** besonderer Gerichtsstand des Erfüllungsortes.
- **§ 29c ZPO** Verbraucherverträge (Wohnsitz Verbraucher).
- **§ 38 ZPO** Gerichtsstandsvereinbarung (zwischen Vollkaufleuten zulässig, gegenüber Verbraucher gemäß § 38 Abs. 3 ZPO eingeschränkt).
- **§ 17 ZPO** Sitz; **§ 24 ZPO** dinglicher Gerichtsstand.
- Bei grenzüberschreitenden Sachverhalten **Brüssel Ia VO (EU) 1215/2012**, insb. Art. 7 Nr. 1 lit. a und b (Erfüllungsort), Art. 17–19 (Verbrauchersachen), Art. 25 (Gerichtsstandsvereinbarung).

### Materielle Anspruchsgrundlagen (Standard)
- **§ 433 Abs. 2 BGB** Kaufpreisanspruch; **§ 631 Abs. 1 BGB** Werklohnanspruch; **§ 611a Abs. 2 BGB** Vergütungsanspruch Dienstvertrag; **§ 535 Abs. 2 BGB** Miete; **§ 488 BGB** Darlehensrückzahlung.
- **§ 286 BGB** Verzug; **§ 288 Abs. 1 BGB** Verzugszinsen 5 Prozentpunkte über Basiszins; **§ 288 Abs. 2 BGB** 9 Prozentpunkte zwischen Unternehmern für Entgeltforderung; **§ 288 Abs. 5 BGB** Verzugspauschale 40 EUR (B2B).
- **§ 280 BGB** Schadensersatz inkl. vorgerichtlicher RA-Kosten.

### Leitentscheidungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabeformat

1. **Klageschrift** als DOCX (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und Markdown-Spiegel.
2. **Anlage Zuständigkeitsprüfung** mit Online-Quellen und Abrufdatum.
3. **Hauseigenes Mini-Plugin** als ZIP (`klagewerkstatt-<slug>.zip`) mit Standardvorlage, Hausregeln und sofort installierbarem Skill `klage-erstellen`.
4. **Optional**: HTML-Padlet zur Pflege, DOCX-Anlagenkopfbogen, Memo im Gutachtenstil.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`) zur Schnellprüfung.
- Bei einstweiligem Rechtsschutz/Mahnverfahren an `prozessrecht` (Plugin) oder das freistehende
  Plugin `zwangsvollstreckung` (`zv-mahnbescheid-online`, `zv-vollstreckungsbescheid-folge`) verweisen.
- Nach Rechtskraft des Titels an `zwangsvollstreckung` zur operativen Durchsetzung (`zv-pfueb-bank`,
  `zv-pfueb-arbeitsentgelt`, `zv-vermoegensauskunft-gv`).
- Wenn der Nutzer beim nächsten Mal nur den Sachverhalt einreichen will: Schwester-Skill `klage-aus-eigenem-skill` mit dem im Schritt 8 erzeugten Plugin verwenden.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweise (27.05.2026)

Drei halluzinierte Rechtsprechungsbelege wurden im Abschnitt "Leitentscheidungen" korrigiert:

| # | Fehlerhaftes AZ | Status | Korrektur |
|---|---|---|---|
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Recherchequelle: dejure.org (Abruf 27.05.2026). Frontmatter unveraendert. Kein Commit.
