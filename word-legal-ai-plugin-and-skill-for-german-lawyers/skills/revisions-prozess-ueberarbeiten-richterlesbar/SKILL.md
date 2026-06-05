---
name: revisions-prozess-ueberarbeiten-richterlesbar
description: "Revisions Prozess Ueberarbeiten Richterlesbar: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Revisions Prozess Ueberarbeiten Richterlesbar

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Revisions Prozess Ueberarbeiten Richterlesbar** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `revisions-prozess-redlines-comparison` | Markup-zwischen Parteien. Compare-Doc-Funktion erzeugt aus zwei Versionen ein Redline-Dokument. Konventionen: Einfügungen in Rot und unterstrichen; Streichungen in Rot und durchgestrichen; Kommentare am Rand. Versionierung v0 eigener Erstentwurf bis v3 eigene Reaktion. Tracked Changes gegen Clean Version für Unterschrift. Mit Pitfalls wie Markup im falschen Modus weitergeleitet; alte Kommentare nicht gelöscht; Metadaten-Leak im Dokumenteigenschaftsfeld. Mit Mustertext zur Begleitkommunikation. |
| `schriftsatz-ueberarbeiten-richterlesbar` | Überarbeitet Schriftsätze so, dass Richterinnen und Richter sie schnell erfassen können. Prüft Antrag, Streitgegenstand, Ergebnisüberschriften, Sachverhaltschronologie, Beweisangebote, Substantiierung, Anlagenverweise, Ton und Länge. Liefert eine richterlesbare Fassung ohne Polemik. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Revisions Prozess Ueberarbeiten Richterlesbar**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `revisions-prozess-redlines-comparison`

**Fokus:** Markup-zwischen Parteien. Compare-Doc-Funktion erzeugt aus zwei Versionen ein Redline-Dokument. Konventionen: Einfügungen in Rot und unterstrichen; Streichungen in Rot und durchgestrichen; Kommentare am Rand. Versionierung v0 eigener Erstentwurf bis v3 eigene Reaktion. Tracked Changes gegen Clean Version für Unterschrift. Mit Pitfalls wie Markup im falschen Modus weitergeleitet; alte Kommentare nicht gelöscht; Metadaten-Leak im Dokumenteigenschaftsfeld. Mit Mustertext zur Begleitkommunikation.

# Revisions-Prozess: Redlines und Compare-Workflow

## Zweck

Jeder Vertrag, jedes Vergleichsangebot, jedes Memo, das mehr als einmal die Hand wechselt, wandert durch einen Revisions-Prozess. Dieser Skill strukturiert den Workflow: Wer schickt welche Version, in welchem Modus, in welcher Farbe, mit welcher Begleitkommunikation? Er erklärt die Compare-Funktion (Vergleichen zwei Versionen, Redline erzeugen), die Konventionen für sichtbares Markup und die Trennung zwischen Arbeitsfassung und Clean Version für die Unterschrift.

Der Skill richtet sich an Drafter, die Verhandlungen führen oder Schriftsätze mit Mandanten und Co-Drafter abstimmen. Er ist die operative Anwendung von sauberer Versionsführung, sichtbarem Markup und dem sicheren Austausch nach `cowork-cloud-kollaboration-drafting`.

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

## Ausgabeformat

- Redline-Dokument (Word-Datei) mit klarer Versionsbezeichnung.
- Clean Version separat für die Unterschrift.
- Begleit-E-Mail oder Schreiben mit Erläuterung der Hauptänderungen.

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

## Querverweise

- `word-dokument-finish-und-layout` für die finale Versandhygiene
- `cowork-cloud-kollaboration-drafting` für sichere Übermittlungswege
- `anwaltsschreiben-aussergerichtlich` für die Begleitkommunikation
- `orientierung-drafting-triage` für die Stadium-Einordnung

## Quellen (Stand 05/2026)

- § 43a BRAO; § 203 StGB; gesetze-im-internet.de.
- §§ 126, 126a, 126b BGB für Form-Anforderungen an die Endfassung.
- § 130a ZPO; § 31a ERVV für den elektronischen Rechtsverkehr ab Einreichung.
- Art. 32 DSGVO für die Sicherheit der Verarbeitung beim Markup-Versand.
- Microsoft-Dokumentation zu Vergleichen und Tracked Changes über support.microsoft.com.
- `references/zitierweise.md` für Belegpflicht in den daraus erzeugten Dokumenten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `schriftsatz-ueberarbeiten-richterlesbar`

**Fokus:** Überarbeitet Schriftsätze so, dass Richterinnen und Richter sie schnell erfassen können. Prüft Antrag, Streitgegenstand, Ergebnisüberschriften, Sachverhaltschronologie, Beweisangebote, Substantiierung, Anlagenverweise, Ton und Länge. Liefert eine richterlesbare Fassung ohne Polemik.

# Schriftsatz Richterlesbar Überarbeiten

## Zweck

Ein Schriftsatz soll entscheiden helfen. Dieser Skill macht aus ungeordnetem Vortrag eine lesbare, beweisbare und prozessual verwertbare Fassung.

## Prüffragen

1. Stehen die Anträge vorne und sind sie bestimmt?
2. Ist der Streitgegenstand klar?
3. Hat jeder Abschnitt eine Ergebnisüberschrift?
4. Ist der Sachverhalt chronologisch und belegbar?
5. Gibt es zu streitigen Tatsachen Beweisangebote?
6. Sind Anlagen exakt bezeichnet?
7. Wird Rechtliches nicht mit Sachverhalt vermischt?
8. Ist der Ton sachlich?
9. Gibt es Wiederholungen?
10. Ist die Hilfsargumentation sauber markiert?

## Ablauf

1. Schriftsatz in Antrag, Sachverhalt, Rechtliches, Beweis und Anlagen zerlegen.
2. Dubletten und Polemik markieren.
3. Ergebnisüberschriften formulieren.
4. Tatsachenvortrag mit Anlagen und Beweisangeboten verbinden.
5. Rechtliche Prüfung im Urteilsstil verdichten.
6. Schlussabschnitt mit konkretem Antrag oder prozessualem nächsten Schritt.

## Mikroregeln

- Ein Absatz = ein Gedanke.
- Tatsachen nicht als Wertung tarnen.
- "Offensichtlich" nur, wenn es wirklich aus Anlage oder Akte folgt.
- Beweisangebot direkt an die Tatsache.
- Keine Norm ohne Funktion.
- Kein Angriff ohne prozessualen Nutzen.

## Output

- Diagnose der drei größten Lesbarkeitsprobleme.
- Überarbeitete Gliederung.
- Neuformulierung kritischer Passagen.
- Anlagen- und Beweisangebot-Checkliste.

## Querverweise

- `klage-drafting-253-zpo`
- `klageerwiderung-substantiiertes-bestreiten`
- `argumentationsarchitektur-schreiben`
- `finaler-writing-quality-gate`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
