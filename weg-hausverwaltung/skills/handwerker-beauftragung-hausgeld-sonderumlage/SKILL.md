---
name: handwerker-beauftragung-hausgeld-sonderumlage
description: "Handwerker Beauftragung Hausgeld Sonderumlage im Plugin Weg Hausverwaltung: prüft konkret Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026), Prüft Hausgeld, Vorschüsse, Rückstände. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Handwerker Beauftragung Hausgeld Sonderumlage

## Arbeitsbereich

**Handwerker Beauftragung Hausgeld Sonderumlage** ordnet den Fall über die tragenden Prüfungslinien: Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026), Prüft Hausgeld, Vorschüsse. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `handwerker-beauftragung-vergabe` | Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026): Leistungsbeschreibung, Vergleichsangebote, Beschlussbedarf, Budget, Nachträge, Abnahme, Rechnungskontrolle, Gewährleistung, Dokumentation; berücksichtigt § 27 WEG (Verwalterkompetenz), § 21 WEG (Kostenfolge), GEG-Pflichten beim Heizungstausch und Sondervergütungspraxis. |
| `hausgeld-sonderumlage-liquiditaet` | Prüft Hausgeld, Vorschüsse, Rückstände, Sonderumlagen, Liquidität, Mahnungen, Ratenzahlung, Beschlussgrundlage und Klagepfad der GdWE (Stand 05/2026). Berücksichtigt BGH V ZR 190/24 zum Zurückbehaltungsrecht und V ZR 139/23 zur Verteilung von Prozesskosten. |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Ordnet Alltagskonflikte in WEG-Anlagen: Tauben auf Balkonen, Fahrradkeller, Diebstahl, Kinderlärm, Spielhof, Weihnachtsbaum, Brandschutz, Hausordnung und Kommunikation. Output: Maßnahmenmatrix und deeskalierende Schreiben. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `handwerker-beauftragung-vergabe`

**Fokus:** Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026): Leistungsbeschreibung, Vergleichsangebote, Beschlussbedarf, Budget, Nachträge, Abnahme, Rechnungskontrolle, Gewährleistung, Dokumentation; berücksichtigt § 27 WEG (Verwalterkompetenz), § 21 WEG (Kostenfolge), GEG-Pflichten beim Heizungstausch und Sondervergütungspraxis.

### Handwerkerbeauftragung und Vergabe

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handwerkerbeauftragung und Vergabe` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Handwerkerbeauftragung und Vergabe
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Aus einem technischen Problem wird ein sauber dokumentierter Verwaltungs- und Beschlussvorgang.

## Workflow

1. **Schaden/Maßnahme beschreiben**: Fotos, Ort, Dringlichkeit, Fachgewerk, betroffene Eigentumsteile, Sicherungsmaßnahmen.
2. **Leistungsbeschreibung** erstellen: gewünschtes Ergebnis, vorhandene Bausubstanz, Ausführungszeitfenster, einzuhaltende Normen.
3. **Angebote vergleichbar machen**:
 - **Mindestens 2–3 Vergleichsangebote** bei substantiellen Maßnahmen (Schwellwerte im Verwaltervertrag/GO oder Beschluss verankert).
 - Vergleichstabelle: Preis (Netto/Brutto), Leistungsumfang, Material, Ausführungszeit, Gewährleistungsfrist (abhängig von Werkart und VOB/B-Vereinbarung — siehe Mustertabelle), Pauschal-/Stundenanteil, Nebenkosten, Ausschlüsse, Referenzen, Versicherung, Bonität.
4. **Beschlussbedarf prüfen** (siehe Tabelle).
5. **Beauftragung** mit klarer Vollmacht, Auftragsbestätigung, ggf. VOB/B-Vereinbarung, Versicherungsnachweis.
6. **Nachträge** schriftlich vereinbaren (Mehrkostenrisiko sichtbar machen), Beirat ggf. einbinden.
7. **Abnahme** dokumentieren (Protokoll, Mängelliste, Beginn Gewährleistung).
8. **Rechnungsprüfung** gegen Angebot, Aufmaß und Abnahme; ggf. Sicherheitseinbehalt.

## Beschlussbedarf (Faustregel)

| Maßnahme | Verwalter allein | Beschluss |
| --- | --- | --- |
| Bagatell-/Routine (kleine Reparaturen) | ja (untergeordnete Bedeutung, § 27 Abs. 1 Nr. 1 WEG) | nein |
| Eilmaßnahme (Schadensabwehr) | ja (§ 27 Abs. 1 Nr. 2 WEG), Bericht | nein |
| Erhaltung über Schwellwert | nur wenn Verwaltervertrag/Beschluss ermächtigt | Mehrheitsbeschluss |
| Modernisierende Erhaltung | nein | Mehrheitsbeschluss, Kostenrahmen |
| Bauliche Veränderung § 20 WEG | nein | Beschluss mit Auflagen, Kostenfolge nach § 21 WEG |
| Heizungstausch (GEG § 71) | nein | Beschluss mit GEG-konformem Konzept |

## Vergleichstabelle Angebote (Schema)

| Punkt | Angebot A | Angebot B | Angebot C |
| --- | --- | --- | --- |
| Brutto Festpreis | ... | ... | ... |
| Ausführungszeit | ... | ... | ... |
| Gewährleistungsfrist (BGB: Bauwerk 5 J, sonstige Werkleistungen/Wartung 2 J — § 634a Abs. 1 BGB; VOB/B § 13 Abs. 4: Bauwerk 4 J, andere Arbeiten und Wartungsarbeiten 2 J, soweit VOB/B wirksam vereinbart) | ... | ... | ... |
| Materialqualität / Typ | ... | ... | ... |
| Ausgeschlossene Leistungen | ... | ... | ... |
| Versicherung / Sachkunde | ... | ... | ... |
| Bonität / Referenzen | ... | ... | ... |
| Nachweise (BAFA, GEG) | ... | ... | ... |

## Mustertext Auftragsbestätigung

> Sehr geehrte Damen und Herren,
> auf Grundlage Ihres Angebots vom [Datum] und des Beschlusses der WEG [Adresse] vom [Datum, TOP X] beauftragen wir Sie verbindlich mit der Ausführung der Maßnahme [Bezeichnung] zu folgenden Konditionen:
> 1. Leistungsumfang gemäß Angebot Anlage 1.
> 2. Pauschalpreis brutto [Betrag] EUR (inkl. USt.).
> 3. Ausführungszeitraum: [Beginn]–[Ende].
> 4. Abnahme: gemeinsam vor Ort am [Datum].
> 5. Gewährleistungsfrist: [Bauwerk-Arbeit BGB 5 Jahre / Bauwerk-Arbeit mit wirksam vereinbarter VOB/B 4 Jahre / sonstige Werkleistung oder Wartung 2 Jahre — passend zur Auftragsart streichen] ab Abnahme.
> 6. Versicherungsnachweis bitte bis [Datum] vorlegen.
> 7. Nachträge nur schriftlich nach vorheriger Freigabe der Verwaltung.

## Output

- Leistungsbeschreibung
- Angebotsvergleich (Tabelle)
- Beauftragungsentwurf
- Nachtragsprüfung (Anlass, Erforderlichkeit, Mehrkosten, Freigabe)
- Abnahme- und Mängelprotokoll
- Rechnungsprüfung mit Differenzliste

## Cross-Refs

- Erhaltung / Modernisierung / GEG → `erhaltung-modernisierung-baumaengel`
- Bauliche Veränderung → `bauliche-veraenderungen-20-weg`
- Beschluss / Sonderumlage → `beschlussvorlagen-erstellen`, `hausgeld-sonderumlage-liquiditaet`
- Beiratskontrolle → `beirat-controlling-verwalter`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. § 27 WEG: https://www.gesetze-im-internet.de/woeigg/__27.html . Bei Heizungstausch GEG § 71 (https://www.gesetze-im-internet.de/geg/__71.html) prüfen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `hausgeld-sonderumlage-liquiditaet`

**Fokus:** Prüft Hausgeld, Vorschüsse, Rückstände, Sonderumlagen, Liquidität, Mahnungen, Ratenzahlung, Beschlussgrundlage und Klagepfad der GdWE (Stand 05/2026). Berücksichtigt BGH V ZR 190/24 zum Zurückbehaltungsrecht und V ZR 139/23 zur Verteilung von Prozesskosten.

### Hausgeld, Sonderumlage und Liquidität

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Hausgeld, Sonderumlage und Liquidität` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Hausgeld, Sonderumlage und Liquidität
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Die Zahlungsfähigkeit der GdWE sichern, ohne Forderungen unsauber zu verfolgen. Hausgeldforderungen leben von der laufenden Liquidität — Zurückbehaltungsrechte sind eng begrenzt.

## Prüfung

- **Beschlussgrundlage**: Wirtschaftsplan (§ 28 Abs. 1 WEG), Sonderumlage (Mehrheitsbeschluss), Nachschüsse aus Abrechnung (§ 28 Abs. 2 WEG).
- **Fälligkeit**: Beschlusswortlaut präzise (Datum oder X Werktage nach Beschluss), Schuldnerbestimmung (Eigentümer bei Beschlussfassung, nicht bei Fälligkeit, soweit nicht abweichend geregelt), Eigentümerwechsel berücksichtigen.
- **Mahnlauf**: erste Erinnerung, Mahnung mit Frist, Verzugszinsen (§ 288 BGB).
- **Rückstände** nach Einheit und Kostenart aufschlüsseln (Vorschuss, Sonderumlage, Nachschuss, Zinsen, Kosten).
- **Ratenzahlung**: Gleichbehandlung der Eigentümer beachten — Beschluss der GdWE oder klare Ermessensleitlinien.
- **Liquiditätslücke**: dringende Maßnahmen, Anwalt, Mahnbescheid, Klage beim Amtsgericht der belegenen Sache (§ 43 WEG, § 23 Nr. 2c GVG).

## Kein Zurückbehaltungsrecht gegen Vorschüsse

- BGH, Urteil vom 14.11.2025, V ZR 190/24: Ein Wohnungseigentümer kann beschlossene Hausgeldvorschüsse **nicht** unter Berufung auf ein Zurückbehaltungsrecht verweigern — auch nicht dann, wenn er einen rechtskräftigen Titel auf Erstellung der Jahresabrechnung besitzt.
- Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.11.2025&Aktenzeichen=V+ZR+190/24
- Begründung: Das laufende Finanzierungssystem der GdWE (§ 28 Abs. 1 Satz 1 WEG) darf nicht durch Druckmittel unterbrochen werden. Aufrechnung mit unstreitigen oder titulierten Gegenforderungen bleibt nach allgemeinen Grundsätzen denkbar (Erfüllungssurrogat), Zurückbehaltung dagegen nicht.

## Prozesskosten der Beschlussklage als Verwaltungskosten

- Prozesskosten der unterliegenden GdWE = Verwaltungskosten i.S.d. § 16 Abs. 2 Satz 1 WEG; sie werden grundsätzlich nach allgemeinem Schlüssel verteilt — auch der obsiegende Anfechtungskläger trägt seinen Anteil mit.
- BGH, Urteil vom 19.07.2024, V ZR 139/23 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.07.2024&Aktenzeichen=V+ZR+139/23).
- Praxisfolge: In der Sonderumlage- oder Wirtschaftsplan-Kalkulation Prozesskostenrisiko realistisch ausweisen.

## Mustertext Sonderumlage-Beschluss

> Die Wohnungseigentümer beschließen eine Sonderumlage in Höhe von [Betrag] EUR zur Finanzierung von [Zweck, z. B. Dachsanierung gemäß TOP X, Beschluss Nr. Y]. Die Umlage wird nach dem allgemeinen Kostenschlüssel auf die Eigentümer verteilt (Anlage [Z]). Fälligkeit: [Datum oder X Werktage nach Zugang der Einzelabrechnung]. Die Verwaltung wird beauftragt, die Sonderumlage einzufordern und auf einem zweckgebundenen Konto zu verbuchen.

## Mustertext Mahnung

> Sehr geehrte/r [Name],
> auf der Grundlage des Wirtschaftsplans/Beschlusses Nr. [...] vom [Datum] sind folgende Hausgeldvorschüsse / Sonderumlagebeträge bis [Fälligkeit] zur Zahlung fällig gewesen:
> [Tabelle]
> Wir bitten Sie, den offenen Betrag in Höhe von [Summe] EUR bis spätestens [Datum] auf das Konto [IBAN] zu überweisen. Bei weiterem Verzug behält sich die GdWE die gerichtliche Geltendmachung einschließlich Verzugszinsen (§ 288 BGB) und Kosten vor.

## Eskalation Hausgeldklage

- Prüfen: Aktivlegitimation GdWE (§ 9a Abs. 2 WEG), Beschlussgrundlage, Bezifferung pro Eigentümer, Fälligkeit, Mahnung, Zinsen.
- Vorbereitendes Anwaltspaket: Sachverhaltschronologie, Beschlüsse (vollständig), Einzelabrechnung, Mahnverlauf, Zahlungsverkehr, Eigentümerwechselbeleg (§ 894 BGB).
- Amtsgericht der belegenen Sache (§ 43 Abs. 1 WEG, § 23 Nr. 2c GVG).

## Output

- Rückstandstabelle (Eigentümer, Beschluss, Betrag, Fälligkeit, Mahnstand, Zinsen)
- Mahnung/Erinnerung
- Ratenzahlungs-Check (Gleichbehandlung, Beschlussbedarf, Sicherheiten)
- Beschlussvorschlag Sonderumlage
- Übergabepaket Hausgeldklage

## Cross-Refs

- Beschlussvorschlag Sonderumlage → `beschlussvorlagen-erstellen`
- Anfechtungsrisiko bei Sonderumlage → `beschlussanfechtung-risiko`
- Eskalation Gericht → `eskalation-anwalt-amtsgericht`
- Abrechnungsspitzen → `wirtschaftsplan-jahresabrechnung-28-weg`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. Keine Beck-RS, juris ohne offene Veröffentlichung, Kommentare/Aufsätze aus Modellwissen. Aktenzeichen nur mit offen prüfbarer URL.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum`

**Fokus:** Ordnet Alltagskonflikte in WEG-Anlagen: Tauben auf Balkonen, Fahrradkeller, Diebstahl, Kinderlärm, Spielhof, Weihnachtsbaum, Brandschutz, Hausordnung und Kommunikation. Output: Maßnahmenmatrix und deeskalierende Schreiben.

### Hausordnung: Tauben, Fahrrad, Kinder, Weihnachtsbaum

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Hausordnung: Tauben, Fahrrad, Kinder, Weihnachtsbaum` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Hausordnung: Tauben, Fahrrad, Kinder, Weihnachtsbaum
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Dieses Fachmodul prüft die kleinen Dinge, die eine WEG zuverlässig groß machen: Tauben auf Balkonen, Fahrradchaos, Fahrraddiebstahl, kinderfeindliche Beschwerden, Hofnutzung, unsicherer Weihnachtsbaum, Fluchtwege und Gemeinschaftsflächen.

## Leitlinie

Alltagskonflikte brauchen zuerst Ordnung und Kommunikation, nicht sofort Anwalt. Gleichzeitig dürfen Brandschutz, Verkehrssicherung, Hygiene und Eigentümerrechte nicht kleingeredet werden.

## Prüfraster

| Thema | Sofort prüfen | Typischer Weg |
| --- | --- | --- |
| Tauben | Hygiene, bauliche Abwehr, Fütterung, Balkon/Sondereigentum | Hinweis, Angebot, Beschluss |
| Fahrrad | Abstellordnung, Fluchtwege, Diebstahl, Video/Datenschutz | Markierung, Registrierung, Räumaktion |
| Kinder | sozialadäquater Lärm, Spielzeiten, Sicherheit | moderieren, keine unzulässige Verdrängung |
| Weihnachtsbaum | Standfestigkeit, Brandschutz, Strom, Haftung | Zuständigkeit und Kosten beschließen |
| Hof | Sondernutzung, Müll, Lieferverkehr, Spielbereich | Nutzungsregeln und Beschilderung |

## Deeskalierender Antwortbaustein

```text
Wir nehmen Ihre Beschwerde ernst und ordnen sie in der nächsten Beiratssitzung ein. Zugleich bitten wir um Verständnis, dass die Verwaltung zwischen bloßen Unannehmlichkeiten, sozial üblicher Nutzung und rechtlich relevanten Störungen unterscheiden muss. Bitte senden Sie uns konkrete Daten, Uhrzeiten, Fotos oder Zeugenangaben, damit wir den Vorgang belastbar prüfen können.
```

## Beschlussbaustein Fahrrad

```text
Die Gemeinschaft beschließt eine Neuordnung der Fahrradabstellflächen. Die Verwaltung wird beauftragt, nicht gekennzeichnete oder offensichtlich aufgegebene Fahrräder nach vorheriger Ankündigung und Dokumentation aus den Gemeinschaftsflächen zu entfernen bzw. gesichert einzulagern. Flucht- und Rettungswege sind dauerhaft freizuhalten.
```

## Red Flags

- Kinderlärm wird pauschal als Störung behandelt.
- Taubenabwehr greift in Fassade oder Balkon ein, ohne Beschluss.
- Fahrräder werden ohne Dokumentation entfernt.
- Weihnachtsbaum/Beleuchtung blockiert Rettungswege oder erzeugt Brandlast.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
