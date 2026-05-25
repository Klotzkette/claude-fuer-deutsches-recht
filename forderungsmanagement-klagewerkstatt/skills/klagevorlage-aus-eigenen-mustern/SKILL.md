---
name: klagevorlage-aus-eigenen-mustern
description: "Lernlauf der Klagewerkstatt für Forderungsmanagement-Klagen. Frisst eigene Klagemuster, Urteile, Kommentare, Aufsätze und Formatvorlagen des Nutzers (DOCX, PDF, MD, TXT), destilliert daraus eine hauseigene generische Standardklage-Vorlage mit Platzhaltern, sammelt den Sachverhalt im Dialog oder aus weiteren Dokumenten, prüft online die sachliche und örtliche Zuständigkeit (justizadressen.nrw.de und justiz.de Gerichtssuche; §§ 12/13/29/29c ZPO; §§ 23 und 71 GVG) und liefert die fertige Klageschrift als DOCX und Markdown. Erzeugt zusätzlich ein eigenes Mini-Plugin als ZIP, das in Claude Code direkt installierbar ist und die nächste Klage ohne erneute Extraktion in der hauseigenen Vorlage produziert. Memo nur auf Anfrage."
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
- Kommentar- und Aufsatz-Auszüge im Bearbeiterstil.
- Format- und Layout-Vorlagen (Briefkopf-DOCX, Schriftarten, Nummerierung).
- Optional: typische Mahnschreiben, Verzugsbriefe, RVG-Berechnungen.

Bei Schweigen mit den im Plugin liegenden Leervorlagen unter `assets/vorlagen-leer/` arbeiten und das im Endprodukt transparent kennzeichnen.

**Schritt 3 — Extraktion der Hausregeln**
Aus dem Lernkorpus extrahieren (Zusammenfassung am Schluss dem Nutzer vorlegen):

- Aufbau der Klageschrift (Rubrum, Anträge, Begründung, Beweismittel, Anlagen, Schluss).
- Standardklauseln: Antragswortlaut, Zinsantrag, vorgerichtliche RA-Kosten als Nebenforderung, Mahnverzugsbeginn, Verzugszinsen (§§ 286, 288 BGB), Verzugsschaden (§ 280 BGB).
- Tonalität: knapp/ausführlich; aktiv/passiv; Direktanrede des Gerichts.
- Zitierweise: Pinpoint, Randnummer, jüngere BGH-Entscheidungen zuerst, deutsche Kommentartradition.
- Belegmuster: bevorzugte Fundstellen für Standardprobleme (Verzug, Beweislast, RVG-VV-Nrn., Anwaltskosten als Verzugsschaden BGH NJW 2008, 1888; Mahnung BGH NJW 2008, 50).
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
   - Treffer prüfen und Bezeichnung, Postanschrift, Telefax und — wo bekannt — die BeA-EGVP-SAFE-ID (Bundesweites elektronisches Adressverzeichnis SAFE, abrufbar in beA bzw. unter justiz.de) einsetzen. Wenn keine SAFE-ID gelistet, mit dem Hinweis „EGVP-Adresse über beA-Adressbuch (SAFE-ID) zu ergänzen" markieren.
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
  - `klagewerkstatt-<slug>/README.md` mit Direkt-Download-Hinweis und Installationsanleitung.
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
- BGH, Urt. v. 22.01.2008 – VIII ZR 6/06, NJW 2008, 1888 — vorgerichtliche RA-Kosten als Verzugsschaden.
- BGH, Urt. v. 04.10.2007 – III ZR 180/06, NJW 2008, 50 — Anforderungen an Mahnung.
- BGH, Urt. v. 25.06.2020 – VII ZR 308/19, NJW 2020, 2884 — Verzugspauschale § 288 Abs. 5 BGB nicht im Arbeitsrecht; Reichweite.
- BGH, Beschl. v. 23.06.2022 – V ZB 12/22 — Anforderungen elektronische Einreichung § 130a ZPO.
- BGH, Beschl. v. 31.01.2023 – XI ZB 23/22 — Sorgfaltspflichten bei beA-Übermittlung.

### Kommentarliteratur (Bearbeiterstil)
- *Greger*, in: Zöller, ZPO, 35. Aufl. 2024, § 253 ZPO Rn. 1–60.
- *Toussaint*, in: BeckOK ZPO, 53. Ed. Stand 03.2025, § 130a Rn. 1–35.
- *Patzina*, in: MüKo-ZPO, 6. Aufl. 2024, §§ 12, 13 Rn. 1–25.
- *Grüneberg*, in: Grüneberg, BGB, 84. Aufl. 2025, § 286 Rn. 1–35; § 288 Rn. 1–18.

## Ausgabeformat

1. **Klageschrift** als DOCX (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und Markdown-Spiegel.
2. **Anlage Zuständigkeitsprüfung** mit Online-Quellen und Abrufdatum.
3. **Hauseigenes Mini-Plugin** als ZIP (`klagewerkstatt-<slug>.zip`) mit Standardvorlage, Hausregeln und sofort installierbarem Skill `klage-erstellen`.
4. **Optional**: HTML-Padlet zur Pflege, DOCX-Anlagenkopfbogen, Memo im Gutachtenstil.

## Quellenpflicht

Mindestens zwei BGH-Belege (jüngere zuerst) und zwei Kommentarbelege im Bearbeiterstil. Online-Adressquelle (justizadressen.nrw.de bzw. justiz.de) mit Abrufdatum zwingend. PDFs unter `references/rechtsprechung/` belegen die zitierten Leitentscheidungen.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`) zur Schnellprüfung.
- Bei einstweiligem Rechtsschutz/Mahnverfahren an `prozessrecht` (Plugin) oder das freistehende
  Plugin `zwangsvollstreckung` (`zv-mahnbescheid-online`, `zv-vollstreckungsbescheid-folge`) verweisen.
- Nach Rechtskraft des Titels an `zwangsvollstreckung` zur operativen Durchsetzung (`zv-pfueb-bank`,
  `zv-pfueb-arbeitsentgelt`, `zv-vermoegensauskunft-gv`).
- Wenn der Nutzer beim nächsten Mal nur den Sachverhalt einreichen will: Schwester-Skill `klage-aus-eigenem-skill` mit dem im Schritt 8 erzeugten Plugin verwenden.
