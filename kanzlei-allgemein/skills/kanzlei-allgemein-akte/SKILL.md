---
name: kanzlei-allgemein-akte
description: "Anlage oder Zuordnung einer Kanzleiakte bei neuer Mandatsanfrage oder eingehendem Schriftstueck. Anwendungsfall Mandant erteilt neuen Auftrag oder Eingang ist keiner Akte zugeordnet. Normen § 43a Abs. 4 BRAO Konfliktcheck § 3 BORA Art. 13 DSGVO Datenschutzhinweis §§ 10 11 GwG Identifizierung. Pruefraster Mandatsart Beteiligte Konfliktcheck Mandatsumfang GwG-Anwendbarkeit Honorar Vollmacht. Output Mandatsblatt Konfliktcheck-Vermerk GwG-Vermerk Aktenstruktur Uebergabeliste Fristen. Abgrenzung zu mandatsannahme-gwg (ausfuehrliche GwG-Ausfuehrung) und kanzlei-allgemein-aktenzeichen."
---

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
