---
name: revisions-prozess-ueberarbeiten-richterlesbar
description: "Markup-zwischen Parteien. Compare-Doc-Funktion erzeugt aus zwei Versionen ein Redline-Dokument. Konventionen: Einfügungen in Rot und unterstrichen; Streichungen in Rot und durchgestrichen; Kommentare am Rand. Versionierung v0 eigener Erstentwurf bis v3 eigene Reaktion. Tracked Changes gegen Clean Version für Unterschrift. Mit Pitfalls wie Markup im falschen Modus weitergeleitet; alte Kommentare nicht gelöscht; Metadaten-Leak im Dokumenteigenschaftsfeld. Mit Mustertext zur Begleitkommunikation im Word Legal Ai Plugin And Skill For German Lawyers."
---

# Revisions-Prozess: Redlines und Compare-Workflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Version 1 und Version 2 zum Vergleich
- Adressat (Gegenseite, Mandant, internes Team)
- Verteilungskanal (E-Mail mit verschlüsseltem Anhang, beA, Cowork, Datenraum)
- Eigene Verhandlungsposition (Klägerseite, Beklagtenseite, Käuferseite, Verkäuferseite)
- Stadium der Verhandlung (Erstentwurf, Zweite Runde, Endfassung)

## Rechtlicher und methodischer Rahmen

- § 43a BRAO und § 203 StGB: Vertraulichkeit. Markup-Dokumente enthalten häufig sensible Anmerkungen.
- §§ 126, 126a, 126b BGB: Schriftform und Textform. Markup-Dokumente sind keine Unterschriftsdokumente.
- § 130a ZPO und § 31a ERVV: elektronischer Rechtsverkehr; im Markup-Stadium nicht eingereichte Dokumente.
- DSGVO Art. 32: Sicherheit der Verarbeitung; Markup-Versand verschlüsselt oder über zertifizierte Kanäle.
- Methodik: Versionsnummern als Anker. Redline-Dokument ist Arbeitsmittel; Clean Version ist Bindungsdokument.

## Ablauf / Checkliste

1. **Versionsnummern vergeben.** Konvention: v0 (eigener Erstentwurf, intern), v1 (an Gegenseite), v2 (Rückkommen mit Markup), v3 (eigene Reaktion). Bei langen Verhandlungen weiter.
2. **Eingehendes Markup prüfen.** Welcher Modus: Tracked Changes oder Compare-Doc-Redline? Wer war Bearbeiter (Autorenfeld lesen)?
3. **Compare-Doc nutzen, wenn die Gegenseite eine Clean Version geschickt hat.** Word, Überprüfen, Vergleichen, Original und überarbeitetes Dokument wählen. Ergebnis: Redline mit allen Änderungen.
4. **Tracked Changes prüfen.** Markup: Alle Markups anzeigen. Änderung für Änderung durchgehen, Annehmen oder Ablehnen.
5. **Eigene Änderungen eintragen.** Tracked Changes aktiv lassen. Eigene Änderungen sind dann farblich kennzeichnet (mit Bearbeiternamen verknüpft).
6. **Kommentare nur, wo erklärungsbedürftig.** Nicht jede Streichung kommentieren; nur die strategisch wichtigen oder die nicht selbsterklärenden.
7. **Alte Kommentare löschen.** Vor Versand prüfen, ob frühere Kommentare aus internen Runden noch sichtbar sind.
8. **Metadaten entfernen.** Datei, Informationen, Dokument prüfen. Autor, Bearbeitungszeit, persönliche Pfade.
9. **Clean Version separat erstellen.** Tracked Changes alle akzeptieren in einer Kopie. Diese Clean Version ist der Unterschriftstext.
10. **Begleit-E-Mail oder Schreiben.** Worauf bezieht sich die Version (v2)? Welche Änderungen sind nicht verhandelbar? Welche sind Vorschlag? Frist für Rückkommen.

### Konvention für Redline-Darstellung

| Element | Darstellung |
|---|---|
| Einfügungen | rot, unterstrichen |
| Streichungen | rot, durchgestrichen |
| Verschiebungen | grün (in moderner Word-Konfiguration) |
| Formatänderungen | optional anzeigen |
| Kommentare | rechter Seitenrand, mit Verfasserkürzel |

### Versionsverlauf-Beispiel

```
v0 2026-05-15 intern Erstentwurf Kanzlei Stern
v1 2026-05-20 Versand an Gegenseite (Clean)
v2 2026-05-27 Eingang von Gegenseite (mit Tracked Changes)
v3 2026-05-30 intern Bewertung und Gegenvorschlag in Tracked Changes
v3a 2026-06-02 Versand an Gegenseite (Tracked Changes sichtbar)
v4 2026-06-10 Eingang von Gegenseite (Reaktion)
v5 2026-06-14 final Clean Version für Unterschrift
```

## Typische Drafting-Fehler

- **Markup im falschen Modus weitergeleitet.** Tracked Changes aus, aber die Änderungen sind nicht akzeptiert. Folge: Empfänger sieht nicht, was geändert wurde.
- **Alte Kommentare nicht gelöscht.** Interne Anmerkungen ("Mandant will hier hart bleiben") werden mit nach außen geschickt.
- **Metadaten-Leak.** Dokumenteigenschaften zeigen Autor, Kanzleipfad oder vorherigen Mandantennamen.
- **Versionsverwirrung.** Empfänger weiß nicht, welche Version die aktuelle ist. Ohne Versionsstempel im Dateinamen wird sofort chaotisch.
- **Tracked Changes mit verschiedenen Bearbeiterprofilen.** Mehrere Drafter haben unterschiedlichen Markup-Farben; im finalen Schritt verwirrend.
- **Compare-Doc verglichen mit falscher Version.** v3 mit v1 verglichen, dabei v2-Schritt übersprungen.
- **Clean Version vergessen vor Unterzeichnung.** Vertrag wird mit eingeschalteten Tracked Changes unterschrieben. Bei späteren Streitigkeiten unklar, was Vertragstext ist.
- **PDF-Konvertierung mit Markup.** PDF eingefrieren mit sichtbaren Tracked Changes; nicht aufhebbar.

## Beispiele

### Mustertext Begleitkommunikation Redline

```
Betreff: Liefervertrag XY-100 – v3 mit unserem Markup

Sehr geehrte Frau Schmidt,

anbei in Tracked Changes unsere Reaktion auf Ihre Version vom 20. Mai 2026
(v2). Wir senden zwei Dateien:

1. Liefervertrag_XY100_v3_2026-05-30_redline.docx mit unseren Änderungen
 in roter Farbe; Tracked Changes sind eingeschaltet.

2. Liefervertrag_XY100_v3_2026-05-30_clean.docx als Lesefassung.

Die wichtigsten Punkte unserer Version v3:

- § 7 Mängelhaftung: Die Verjährungsfrist von zwölf Monaten haben wir auf
 24 Monate erweitert (Verhandlungspriorität A).
- § 11 Haftungsbegrenzung: Den Ausschluss für mittlere Fahrlässigkeit
 haben wir gestrichen. Mit § 309 Nr. 7 BGB nicht vereinbar.
- § 15 Gerichtsstand: Hamburg statt München. Verhandelbar.
- § 20 Salvatorische Klausel: redaktionelle Anpassung.

Wir erwarten Ihre Rückäußerung bis zum 13. Juni 2026.

Mit freundlichen Grüßen
Marta Stern
Rechtsanwältin
```

### Beispiel-Checkliste vor Versand

```
[ ] Tracked Changes-Modus geprüft (an oder aus, je nach Empfänger)
[ ] Alte Kommentare gelöscht
[ ] Metadaten entfernt (Datei, Informationen, Dokument prüfen)
[ ] Dateiname enthält Versionsnummer und Datum
[ ] Clean Version als zweite Datei beigefügt (falls Vertrag)
[ ] Begleit-E-Mail mit den drei bis fünf wichtigsten Änderungen
[ ] Versand über sicheren Kanal (beA, Datenraum, verschlüsselte E-Mail)
```

## Quellen (Stand 05/2026)

- § 43a BRAO; § 203 StGB; gesetze-im-internet.de.
- §§ 126, 126a, 126b BGB für Form-Anforderungen an die Endfassung.
- § 130a ZPO; § 31a ERVV für den elektronischen Rechtsverkehr ab Einreichung.
- Art. 32 DSGVO für die Sicherheit der Verarbeitung beim Markup-Versand.
- Microsoft-Dokumentation zu Vergleichen und Tracked Changes über support.microsoft.com.
- `references/zitierweise.md` für Belegpflicht in den daraus erzeugten Dokumenten.

