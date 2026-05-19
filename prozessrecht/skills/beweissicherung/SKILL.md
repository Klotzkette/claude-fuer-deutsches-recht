---
name: beweissicherung
description: "Anordnung, Aktualisierung, Aufhebung oder Statusbericht zu Aufbewahrungspflichten und Beweissicherungsmaßnahmen nach deutschem Recht – § 257 HGB, § 147 AO, §§ 286, 444 ZPO (Beweisvereitelung), §§ 485 ff. ZPO (Selbständiges Beweisverfahren). Verwenden, wenn der Nutzer sagt „Aufbewahrungspflicht prüfen\", „Beweissicherung anordnen\", „Legal Hold einrichten\" oder Statusbericht über Sicherungsmaßnahmen anfordert."
---

# Aufbewahrungspflicht und Beweissicherung

## Zweck

Erstellung, Aktualisierung oder Aufhebung von Beweissicherungs- und Aufbewahrungsanordnungen für Mandate im deutschen Zivil- und Wirtschaftsrecht. Ziel ist die Vermeidung der Beweisvereitelung (§§ 286, 444 ZPO) und die Sicherung von Beweismitteln für ein bevorstehendes oder laufendes Gerichtsverfahren – ggf. im Wege des Selbständigen Beweisverfahrens (§§ 485 ff. ZPO).

> **Kein US-Legal-Hold-System.** Das deutsche Recht kennt keine umfassende parteiengetriebene Discovery-Hold-Pflicht. Aufbewahrungspflichten entstehen aus gesetzlichen Vorschriften und aus dem Grundsatz der Prozessförderungs­pflicht; eine Vernichtung beweis­erheblicher Dokumente kann Beweisvereitelung darstellen.

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--anordnen`, `--aktualisieren`, `--aufheben`, `--status`
- Betroffene Dokumentenkategorien und Custodians (Personen/Abteilungen, die Dokumente halten)
- Aufbewahrungsanlass: laufendes Verfahren / angekündigtes Verfahren / Behördenanfrage

## Ablauf

### 1. Aufbewahrungspflichten prüfen

**Handels- und steuerrechtliche Pflichtfristen:**
| Kategorie | Frist | Rechtsgrundlage |
|---|---|---|
| Handelsbücher, Inventare, Jahresabschlüsse | 10 Jahre | § 257 Abs. 4 HGB |
| Buchungsbelege | 10 Jahre | § 257 Abs. 4 HGB, § 147 Abs. 3 AO |
| Handels- und Geschäftsbriefe | 6 Jahre | § 257 Abs. 4 HGB |
| Sonstige steuerlich relevante Unterlagen | 6 Jahre | § 147 Abs. 1 Nr. 5 AO |
| Lohnunterlagen (SV-relevant) | 10 Jahre | § 28f Abs. 2 SGB IV |

**Prozessuale Aufbewahrungspflicht:**
Ab Kenntnis eines konkreten Rechtsstreits oder einer ernsthaften Drohung entsteht eine Pflicht zur Beweissicherung (vgl. BGH, Urt. v. 23.10.2008 – III ZR 57/07, NJW 2009, 366 Rn. 19 – Beweisvereitelung). Eine schuldhafte Vernichtung von Beweismitteln kann nach § 444 ZPO zur Umkehr der Beweislast führen oder nach § 286 ZPO als beweiswürdigungserhebliches Indiz gewertet werden.

**Konsequenzen der Beweisvereitelung:**
- § 444 ZPO: Unwiderlegliche Vermutung, dass das vernichtete Dokument den gegnerischen Vortrag bestätigt hätte (BGH, Urt. v. 14.12.2016 – IV ZR 527/15, NJW 2017, 869 Rn. 17).
- § 286 ZPO: Freie Beweiswürdigung kann vernichtungsbedingte Nachteile zulasten der vernichtenden Partei ziehen.
- §§ 339 ff. StGB: Strafbarkeit wegen Beweisvereitelung / Urkundenunterdrückung (§ 274 StGB) bei vorsätzlicher Vernichtung.

### 2. Beweissicherungs-Anordnung erstellen (`--anordnen`)

Inhalt der Anordnung:
- Adressaten (Custodians): Namen, Funktion, Abteilung
- Betroffene Dokumentenarten: E-Mails, Verträge, Buchungsbelege, CAD-Dateien, Systemlogs
- Zeitraum der zu sichernden Unterlagen
- Löschverbot: Ausdrückliches Verbot, betreffende Daten zu löschen, zu überschreiben oder zu ändern
- Aufbewahrungsort und -format
- Überprüfungsintervall
- Kontaktperson für Rückfragen
- Geltungsdauer / Aufhebungsvorbehalt

### 3. Selbständiges Beweisverfahren (§§ 485 ff. ZPO)

Wenn Beweismittel außerhalb des Prozesses gesichert werden müssen (z. B. drohende Veränderung von Sachzustand, Mängel, Bauschäden):

- Antrag nach § 485 ZPO: Beantragung der Beweissicherung durch das Prozessgericht (oder nach § 486 ZPO beim Amtsgericht des Ortes)
- Inhalt: Beweisthema, Beweismittel (Sachverständiger, Augenschein), Benennung des Antragsgegners
- Wirkung: Gutachten bindet das spätere Prozessgericht grundsätzlich (§ 493 ZPO)
- Fristen: §§ 486 Abs. 2, 487 ZPO

### 4. Statusbericht (`--status`)

Tabelle aller aktiven Sicherungsanordnungen im Portfolio mit:
- Mandat-Slug
- Datum der Anordnung
- Betroffene Custodians
- Überprüfungsdatum
- Aufhebungsvoraussetzungen

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BGH, Urt. v. 14.12.2016 – IV ZR 527/15, NJW 2017, 869 Rn. 17 (Beweisvereitelung § 444 ZPO: Vermutungswirkung).
- BGH, Urt. v. 23.10.2008 – III ZR 57/07, NJW 2009, 366 Rn. 19 (Beweisvereitelung und Pflicht zur Beweismittelsicherung).
- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 444 Rn. 1 ff. (Beweisvereitelung: Voraussetzungen, Rechtsfolgen).
- Huber, in: Musielak/Voit, ZPO, 21. Aufl. 2024, § 485 Rn. 3 ff. (Selbständiges Beweisverfahren: Voraussetzungen, Antrag).
- BGH, Urt. v. 09.04.2014 – VIII ZR 404/12, NJW 2014, 2102 Rn. 15 (§ 493 ZPO: Bindungswirkung des Sachverständigengutachtens aus dem selbständigen Beweisverfahren).
- § 257 HGB; § 147 AO (Aufbewahrungsfristen).
- § 274 StGB (Urkundenunterdrückung), § 339 StGB (Rechtsbeugung, nur für Richter und Beamte).

## Ausgabeformat

### Beweissicherungs-Anordnung

```
BEWEISSICHERUNGS-ANORDNUNG
Mandat: [Slug]
Datum: TT.MM.JJJJ
Erstellt von: [Anwalt]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO / § 203 StGB

──────────────────────────────────────────────
ANORDNUNG ZUR AUFBEWAHRUNG VON UNTERLAGEN
──────────────────────────────────────────────

An: [Name, Funktion, Abteilung]

Betreff: Aufbewahrungspflicht im Zusammenhang mit [Sachverhaltskurzbezeichnung]

Aufgrund eines bevorstehenden / laufenden Rechtsstreits [Aktenzeichen oder Sachverhalt] 
ordnen wir an, folgende Unterlagen bis auf Weiteres aufzubewahren:

Betroffene Dokumente:
1. Alle E-Mails und sonstigen Korrespondenzen betreffend [Thema] ab [Datum]
2. Verträge und Anlagen zu [Projekt]
3. [weitere Kategorien]

LÖSCHVERBOT: Es ist untersagt, die oben bezeichneten Unterlagen zu löschen, zu 
vernichten, zu überschreiben oder anderweitig unzugänglich zu machen.

Nächste Überprüfung: TT.MM.JJJJ
Kontakt: [Anwalt, Kanzlei, Telefon]
```

## Risiken / typische Fehler

- **Verzögerter Hold:** Die Anordnung muss bei Kenntnis des Rechtsstreits sofort erfolgen; spätere Vernichtung begründet Beweisvereitelung auch ohne Hold (BGH – IV ZR 527/15).
- **Zu enger Anwendungsbereich:** Custodians und Dokumentenkategorien zu eng gewählt; alle betroffenen Abteilungen und IT-Systeme (E-Mail-Archiv, Cloud-Speicher) einschließen.
- **Datenschutzkollision:** Aufbewahrungspflicht und DSGVO-Löschpflicht können kollidieren; bei Widerspruch gilt prozessuale Sicherungspflicht im Zweifel (vgl. Art. 17 Abs. 3 lit. e DSGVO: Aufbewahrung für Rechtsstreitigkeiten).
- **Selbständiges Beweisverfahren zu spät:** Nach Sachzustandsveränderung ist keine Beweissicherung mehr möglich; § 485 ZPO-Antrag frühzeitig stellen.
