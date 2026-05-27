# Forderungsmanagement — Klagewerkstatt

**Generalisierter Klage-Assistent für Inkasso- und Forderungsmanagement-Klagen mit eigenem Plugin-Generator.** Aus eigenen Mustern eine hauseigene Standardvorlage destillieren, online die Zuständigkeit prüfen, die Klage erzeugen und als sofort installierbares Mini-Plugin verpacken. Neu hinzu kommt ein direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper und der harten Regel: nur klare, fällige und belegte Ansprüche einklagen.

---

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin / Testakte | Direkt-Download |
| --- | --- |
| **forderungsmanagement-klagewerkstatt** (dieses Plugin) | [forderungsmanagement-klagewerkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| **Testakte ModeFuchs** (Referenzfall Inkasso-Zahlungsklage) | [testakte-inkasso-zahlungsklage-modefuchs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |
| prozessrecht (sinnvolle Ergänzung) | [prozessrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |
| Liquiditätsplanung (`liquiditaetsplanung`, Folgeprüfung) | [liquiditaetsplanung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |

Die URLs sind **stabil** und zeigen immer auf die neueste Version. Alle weiteren Plugins (Vertragsrecht, Arbeitsrecht, Datenschutz, …) liegen unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

---

## Was ist drin

Drei Skills, gedacht als Lernlauf-+-Laufzeit-Paar plus direkter Inkasso-Klageassistent:

| Skill | Zweck |
| --- | --- |
| `klagevorlage-aus-eigenen-mustern` | **Lernlauf**: frisst eigene Klagemuster, Urteile, Kommentare, Aufsätze, Formatvorlagen; destilliert die hauseigene Standardklage-Vorlage; sammelt den Sachverhalt; **prüft online die Zuständigkeit** (justizadressen.nrw.de, justiz.de); liefert die Klage und erzeugt zusätzlich ein eigenes installierbares **Mini-Plugin als ZIP**. |
| `klage-aus-eigenem-skill` | **Laufzeit**: setzt voraus, dass das im Lernlauf erzeugte Mini-Plugin installiert ist. Nimmt nur noch Sachverhalt und Beklagtenadresse, prüft erneut online die Zuständigkeit, befüllt die Hausvorlage. Keine erneute Extraktion. |
| `inkasso-zahlungsklage-ersteller` | **Direktlauf**: liest Forderungsakte, Mahnungen, Abtretung, Inkassoschreiben, Teilzahlungen, Mahnbescheid/Widerspruch und vorhandene Klagen; erstellt Mahnchronologie, Anspruchsmatrix und Gerichtsortprüfung; nimmt nur grüne Positionen in den Klageentwurf. Bezahlte Hauptforderungen werden rot geblockt. |

Alle Klage-Skills führen **bei jedem Lauf** die Online-Zuständigkeitsprüfung über [justizadressen.nrw.de](https://www.justizadressen.nrw.de/de/justiz/suche) und das [bundesweite Justizportal](https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php) durch.

## Inkasso-Zahlungsklage-Ersteller

Der neue Direktlauf ist für Fälle gedacht, in denen eine Forderungsakte schon einen Mahn- oder Inkassoverlauf enthält. Er prüft vor der Klage:

- Rechnung, Fälligkeit, Lieferung/Leistung und Abtretung.
- Mahnvorlauf mit Zugang, Fristen und Beträgen.
- Zahlungseingänge, Teilzahlungen, Erfüllung und interne Kenntnis.
- Mahnkosten, Verzugszinsen, Inkassokosten und Mahnverfahrenskosten einzeln.
- Gerichtsort mit aktueller ladungsfähiger Anschrift.

Die ModeFuchs-Testakte unter [`testakten/inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/) ist der Referenzfall: Hauptforderung 698,00 EUR bezahlt vor Klageeinreichung, Nebenforderungen 99,84 EUR streitig. Erwartung: Hauptforderung rot, Nebenforderungen gelb, keine automatische Klage über 797,84 EUR.

[testakte-inkasso-zahlungsklage-modefuchs.zip herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip)

## Plugin-Generator

Aus den extrahierten Hausregeln und der Standardvorlage packt der Skill ein eigenes, in Claude Code direkt installierbares ZIP:

```bash
python scripts/plugin_aus_hausregeln.py \
  --kanzlei "Kanzlei Mustermann" \
  --vorlage assets/vorlagen-leer/standardklage.md \
  --regeln  /pfad/hausregeln.json \
  --ziel    /pfad/klagewerkstatt-mustermann.zip
```

Layout des erzeugten Plugins:

```
klagewerkstatt-<slug>/
  .claude-plugin/plugin.json
  skills/klage-erstellen/SKILL.md
  assets/vorlage/standardklage.md
  references/hausregeln.json
  references/belegmuster.md
  references/anlagenliste.md
  references/zustaendigkeit-quellen.md
  README.md
```

Der erzeugte Skill enthält die Hausregeln fest verdrahtet und führt weiterhin die **Online-Zuständigkeitsprüfung** als Pflichtschritt aus.

## Ergebnisformate

- **DOCX** über `office/docx` (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und **Markdown-Spiegel**.
- **Anlage Zuständigkeitsprüfung** mit Online-Quelle und Abrufdatum.
- **HTML-Padlet** (`assets/padlet/klage-padlet.html`) — single-file, autark, Live-Vorschau, speichert in `localStorage`, exportiert/importiert JSON.
- **Memo** im Gutachtenstil — nur auf ausdrückliche Anfrage.

## Online-Zuständigkeit (Pflicht in jedem Lauf)

1. **Sachlich** rechnerisch: ≤ 10.000 EUR → AG (§ 23 Nr. 1 GVG i. d. F. seit 1.1.2026); > 10.000 EUR → LG (§ 71 GVG); Sondertatbestände beachten (insbes. Wohnraummietsachen AG ohne Streitwertgrenze, § 23 Nr. 2a GVG).
2. **Örtlich** rechtlich: §§ 12, 13 ZPO Allgemeiner Gerichtsstand, § 29 ZPO Erfüllungsort, § 29c ZPO Verbraucherverträge, § 38 ZPO Gerichtsstandsvereinbarung; grenzüberschreitend Brüssel Ia VO 1215/2012.
3. **Online-Adressrecherche**: `justizadressen.nrw.de` (PLZ/Ort) und bundesweit `justiz.de`; Quelle und Abrufdatum dokumentieren.
4. BeA-SAFE-ID: aus dem beA-Adressbuch zu ergänzen.

## Leitentscheidungen (Auswahl, siehe `references/rechtsprechung/INDEX.md`)

- BGH, Urt. v. 25.06.2020 – VII ZR 308/19, NJW 2020, 2884 (§ 288 Abs. 5 BGB)
- BGH, Urt. v. 22.01.2008 – VIII ZR 6/06, NJW 2008, 1888 (RA-Kosten als Verzugsschaden)
- BGH, Urt. v. 04.10.2007 – III ZR 180/06, NJW 2008, 50 (Mahnung)
- BGH, Beschl. v. 23.06.2022 – V ZB 12/22 (§ 130a ZPO)
- BGH, Beschl. v. 31.01.2023 – XI ZB 23/22 (beA-Sorgfalt)
- BGH, Urt. v. 22.04.2009 – VIII ZR 156/07, NJW 2009, 2197 (§ 29 ZPO)
- EuGH, Urt. v. 14.09.2023 – C-393/22 (Brüssel Ia VO)

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Alle Aussagen beruhen auf der zitierten BGH-Rechtsprechung und genannter Kommentarliteratur. Die Skills ersetzen keine eigene anwaltliche Prüfung im Einzelfall.
