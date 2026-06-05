---
name: aktenzeichen
description: "Kanzlei Allgemein Akte, Kanzlei Allgemein Aktenzeichen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Kanzlei Allgemein Akte, Kanzlei Allgemein Aktenzeichen

## Arbeitsbereich

Dieser Skill bündelt **Kanzlei Allgemein Akte, Kanzlei Allgemein Aktenzeichen** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `kanzlei-allgemein-akte` | Anlage oder Zuordnung einer Kanzleiakte bei neuer Mandatsanfrage oder eingehendem Schriftstueck. Anwendungsfall Mandant erteilt neuen Auftrag oder Eingang ist keiner Akte zugeordnet. Normen § 43a Abs. 4 BRAO Konfliktcheck § 3 BORA Art. 13 DSGVO Datenschutzhinweis §§ 10 11 GwG Identifizierung. Prüfraster Mandatsart Beteiligte Konfliktcheck Mandatsumfang GwG-Anwendbarkeit Honorar Vollmacht. Output Mandatsblatt Konfliktcheck-Vermerk GwG-Vermerk Aktenstruktur Übergabeliste Fristen. Abgrenzung zu mandatsannahme-gwg (ausführliche GwG-Ausführung) und kanzlei-allgemein-aktenzeichen. |
| `kanzlei-allgemein-aktenzeichen` | Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO § 130a ZPO. Prüfraster Typen (eigenes gerichtliches behoerdliches gegnerisches) Normalisierung Varianten Kollisionen Kontext. Output Verknuepfungstabelle mit Sicherheitsgrad Kollisionswarnungen Rückfragen bei Unsicherheit. Abgrenzung zu kanzlei-allgemein-akte und kanzlei-allgemein-intake. |

## Arbeitsweg

Für **Kanzlei Allgemein Akte, Kanzlei Allgemein Aktenzeichen** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `kanzlei-allgemein` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `kanzlei-allgemein-akte`

**Fokus:** Anlage oder Zuordnung einer Kanzleiakte bei neuer Mandatsanfrage oder eingehendem Schriftstueck. Anwendungsfall Mandant erteilt neuen Auftrag oder Eingang ist keiner Akte zugeordnet. Normen § 43a Abs. 4 BRAO Konfliktcheck § 3 BORA Art. 13 DSGVO Datenschutzhinweis §§ 10 11 GwG Identifizierung. Prüfraster Mandatsart Beteiligte Konfliktcheck Mandatsumfang GwG-Anwendbarkeit Honorar Vollmacht. Output Mandatsblatt Konfliktcheck-Vermerk GwG-Vermerk Aktenstruktur Übergabeliste Fristen. Abgrenzung zu mandatsannahme-gwg (ausführliche GwG-Ausführung) und kanzlei-allgemein-aktenzeichen.

# Akte, Konfliktcheck und Mandatsanlage

## Zweck

Dieser Skill führt von der Anfrage zur belastbaren Mandatsakte. Er legt keine produktive Kanzleiakte heimlich an, sondern erzeugt eine Aktenanlage mit Prüfvermerken und Rückfragen.

## Ablauf

1. **Mandatsart klären**: Beratung, Vertretung, Prozess, Verteidigung, Dauerberatung, Eilsache.
2. **Beteiligte erfassen**: Mandant, Gegner, Dritte, Versicherer, Gericht, Behörde.
3. **Konfliktcheck vorbereiten**: Namen, verbundene Unternehmen, wirtschaftlich Berechtigte, frühere Mandate.
4. **Mandatsumfang abgrenzen**: was ist beauftragt, was ausdrücklich nicht.
5. **Mandatsannahme/GwG starten**: `kanzlei-allgemein-mandatsannahme-gwg` ausführen, wenn neue Mandatsanfrage, Unternehmensmandant, Transaktionsbezug, Immobilienbezug, Gesellschaftsbezug, Fremdgeld, abweichender Zahler oder Identifizierungsbedarf vorliegt.
6. **Pflichtdokumente anlegen**: Vollmacht, Datenschutzhinweis, Mandatsvereinbarung, Honorar, Vorschuss, KI-Hinweis, GwG-Dokumentation.
7. **Kontoblatt anlegen**: Debitor, Rechnungsempfänger, Stundensatz, Vorschuss, Rechtsschutz, Fremdgeldhinweis, E-Rechnung, GoBD-Ablage.
8. **Aktenstruktur vorschlagen**: Eingänge, Schriftsätze, Anlagen, Fristen, Honorar, GwG, Korrespondenz, Notizen.
9. **Übergabe an Fristen und Zeit**: erste Fristen und erste Tätigkeiten vormerken.

## Konfliktcheck

Der Skill trifft keine endgültige berufsrechtliche Entscheidung. Er erzeugt:

- Trefferliste.
- Risikoklasse.
- Rückfragen.
- Vorschlag: annehmen, nur nach Klärung, ablehnen.

## Mandatsannahme und GwG

Bei Neuanlagen nie nur ein leeres Mandatsblatt erzeugen. Immer mindestens festhalten:

- Akquisequelle und Erstkontakt.
- Mandatsumfang und ausgeschlossene Tätigkeiten.
- Konfliktcheck-Status.
- GwG-Anwendbarkeit oder Grund, warum kein Kataloggeschäft vorliegt.
- Identifizierungsstatus.
- wirtschaftlich Berechtigte, soweit relevant.
- Mandatskontoblatt mit Honorar, Vorschuss und Rechnungsempfänger.
- Annahmeentscheidung mit Verantwortlichem.

## Vorlage

Für das Mandatsblatt `assets/templates/mandatsblatt-vorlage.md` verwenden.
Für Mandatsannahme und GwG zusätzlich `assets/templates/mandatsannahme-gwg-start.md`, `assets/templates/mandatskontoblatt.md` und die GwG-Templates verwenden.

## Ausgabe

- Mandatsblatt.
- Konfliktcheck-Vermerk.
- GwG- und Mandatsannahmevermerk.
- Mandatskontoblatt.
- Liste fehlender Pflichtdaten.
- Aktenstruktur.
- Übergabeliste an Fristen, Zeit und Honorar.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kanzlei-allgemein-aktenzeichen`

**Fokus:** Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO § 130a ZPO. Prüfraster Typen (eigenes gerichtliches behoerdliches gegnerisches) Normalisierung Varianten Kollisionen Kontext. Output Verknuepfungstabelle mit Sicherheitsgrad Kollisionswarnungen Rückfragen bei Unsicherheit. Abgrenzung zu kanzlei-allgemein-akte und kanzlei-allgemein-intake.

# Aktenzeichen und Verknüpfungen


## Triage zu Beginn
1. Liegt ein eigenes Kanzlei-Aktenzeichen, ein gerichtliches Aktenzeichen oder ein behördliches Zeichen vor?
2. Gibt es Kollisionsgefahr bei aehnlichen Aktenzeichen-Varianten in derselben Akte?
3. Soll das Aktenzeichen einem bereits vorhandenen Mandat zugeordnet oder als neues Mandat angelegt werden?
4. Sind fremde Aktenzeichen (Gegner, Versicherung, Rechtsschutz) mit dem eigenen verknuepft?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 51 BRAO — Berufshaftpflicht des Rechtsanwalts; Aktenzeichen-Fehler als Pflichtverletzung
- § 253 Abs. 2 Nr. 1 ZPO — Bezeichnungspflicht der Parteien und Sache in der Klageschrift
- § 319 ZPO — Berichtigung offensichtlicher Unrichtigkeiten in Urteilen (auch Aktenzeichen)
- § 130a ZPO — Pflichtangaben beim elektronischen Dokument, inkl. Aktenzeichen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill verhindert Suchchaos. Er erkennt Aktenzeichen aus Texten, Dateinamen, Betreffzeilen, beA-Nachrichten, PDFs, Screenshots und Notizen und verknüpft sie mit der richtigen Kanzleiakte.

## Typen von Aktenzeichen

- Eigenes Kanzlei-Aktenzeichen.
- Gerichtliches Aktenzeichen.
- Behördenzeichen.
- Gegnerisches Aktenzeichen.
- Versicherungs- oder Schadennummer.
- Rechtsschutz-Schadennummer.
- Mandanteninterne Projektnummer.
- Altaktenzeichen.

## Ablauf

1. Alle Kandidaten extrahieren.
2. Varianten normalisieren: Leerzeichen, Schrägstrich, Bindestrich, führende Nullen.
3. Kontext prüfen: Name, Gericht, Gegner, Datum, Betreff.
4. Kollisionen markieren.
5. Eindeutige Verknüpfung vorschlagen.
6. Unsichere Zuordnung als Rückfrage ausgeben.

## Ausgabe

```markdown
## Aktenzeichen-Verknüpfung

| Typ | Aktenzeichen | Quelle | Akte | Sicherheit | Notiz |
| --- | --- | --- | --- | --- | --- |
```

## Sicherheitsregel

Wenn zwei Akten plausibel sind, nicht automatisch ablegen. Immer nachfragen.
