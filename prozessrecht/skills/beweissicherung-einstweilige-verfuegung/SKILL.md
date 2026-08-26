---
name: beweissicherung-einstweilige-verfuegung
description: "Für Aufbewahrungspflicht und Beweissicherung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix."
---

# Aufbewahrungspflicht und Beweissicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
| Handelsbücher, Inventare, Jahresabschlüsse | 10 Jahre | Paragraf 257 Abs. 4 HGB |
| Buchungsbelege | 10 Jahre | Paragraf 257 Abs. 4 HGB, Paragraf 147 Abs. 3 AO |
| Handels- und Geschäftsbriefe | 6 Jahre | Paragraf 257 Abs. 4 HGB |
| Sonstige steuerlich relevante Unterlagen | 6 Jahre | Paragraf 147 Abs. 1 Nr. 5 AO |
| Lohnunterlagen (SV-relevant) | 10 Jahre | Paragraf 28f Abs. 2 SGB IV |

**Prozessuale Aufbewahrungspflicht:**

**Konsequenzen der Beweisvereitelung:**
- Paragraf 286 ZPO: Freie Beweiswürdigung kann vernichtungsbedingte Nachteile zulasten der vernichtenden Partei ziehen.
- Paragrafen 339 ff. StGB: Strafbarkeit wegen Beweisvereitelung / Urkundenunterdrückung (Paragraf 274 StGB) bei vorsätzlicher Vernichtung.

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

### 3. Selbständiges Beweisverfahren (Paragrafen 485 ff. ZPO)

Wenn Beweismittel außerhalb des Prozesses gesichert werden müssen (z. B. drohende Veränderung von Sachzustand, Mängel, Bauschäden):

- Antrag nach Paragraf 485 ZPO: Beantragung der Beweissicherung durch das Prozessgericht (oder nach Paragraf 486 ZPO beim Amtsgericht des Ortes)
- Inhalt: Beweisthema, Beweismittel (Sachverständiger, Augenschein), Benennung des Antragsgegners
- Wirkung: Gutachten bindet das spätere Prozessgericht grundsätzlich (Paragraf 493 ZPO)
- Fristen: Paragrafen 486 Abs. 2, 487 ZPO

### 4. Statusbericht (`--status`)

Tabelle aller aktiven Sicherungsanordnungen im Portfolio mit:
- Mandat-Slug
- Datum der Anordnung
- Betroffene Custodians
- Überprüfungsdatum
- Aufhebungsvoraussetzungen

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Paragraf 257 HGB; Paragraf 147 AO (Aufbewahrungsfristen).
- Paragraf 274 StGB (Urkundenunterdrückung), Paragraf 339 StGB (Rechtsbeugung, nur für Richter und Beamte).

## Ausgabeformat

### Beweissicherungs-Anordnung

```
BEWEISSICHERUNGS-ANORDNUNG
Mandat: [Slug]
Datum: TT.MM.JJJJ
Erstellt von: [Anwalt]
MANDATSGEHEIMNIS – Paragraf 43a Abs. 2 BRAO / Paragraf 203 StGB

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Risiken / typische Fehler

- **Zu enger Anwendungsbereich:** Custodians und Dokumentenkategorien zu eng gewählt; alle betroffenen Abteilungen und IT-Systeme (E-Mail-Archiv, Cloud-Speicher) einschließen.
- **Datenschutzkollision:** Aufbewahrungspflicht und DSGVO-Löschpflicht können kollidieren; bei Widerspruch gilt prozessuale Sicherungspflicht im Zweifel (vgl. Art. 17 Abs. 3 lit. e DSGVO: Aufbewahrung für Rechtsstreitigkeiten).
- **Selbständiges Beweisverfahren zu spät:** Nach Sachzustandsveränderung ist keine Beweissicherung mehr möglich; Paragraf 485 ZPO-Antrag frühzeitig stellen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
