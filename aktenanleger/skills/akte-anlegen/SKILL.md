---
name: akte-anlegen
description: "Legt den Eingang für Anwaltskanzlei, Anwaltsnotariat oder Nurnotariat mit Aktenstamm, Belegen, Fristen und Übergabe an. Klärt Rollen und Befugnisse und führt die Akte nach einer Nachreichung fort."
---

# Akte anlegen und in die Bearbeitung geben

Wer will heute welche Leistung von welchem Büro? Lies zuerst Eingangspost und Anlagen. Gib als ersten Satz Vorgang, Auftrag und die jetzt dringende Entscheidung aus. Ein übermittelter Bescheid kann eilig sein, obwohl Vertretung und Annahme noch offen sind. Sichere diese Dringlichkeit sofort für die verantwortliche Person. Bei fehlendem Zugang zum Kanzleisystem liefere einen vollständig übernehmbaren Arbeitsstand.

## 1. Vor jeder Anlage

Erfasse tatsächlichen Eingang mit Uhrzeit und Übermittlungsweg, Absender, gewünschten Empfänger und Originalbezeichnung. Nenne bei einem fehlenden Anhang den Verweis im Anschreiben. Vergleiche Aktenzeichen, Parteien, frühere Firmierung, Grundstück oder Vertrag mit verfügbaren Beständen. Fehlt der Zugriff, vermerke die noch ausstehende Suche und deren Umfang. Bei gleichem Gegenstand knüpfe an den Bestand an. Halte den neuen Auftrag oder die neue Stufe mit eigenem Datum fest. Bei ungeklärtem Zusammenhang verwende ein vorläufiges Eingangszeichen aus der Bürokonvention oder „Zeichen durch Registratur zu vergeben“.

## 2. Rolle und Befugnis festlegen

1. [Auftrag und Amtsrolle klären](../amt-oder-mandat-klaeren/SKILL.md). Für wen soll ein Interesse vertreten werden? Ist ein neutrales Amtsgeschäft erbeten oder ein interner Vorgang? Im Anwaltsnotariat § 24 Abs. 2 BNotO anhand des Zwecks anwenden. Bei einem Rollenwechsel Vorgeschichte und Zugriffsgrenzen neu prüfen.
2. [Beteiligte und Vertretung erfassen](../beteiligte-und-vertretung-erfassen/SKILL.md). Antragsteller, Rechtsträger, Vertreter, Gegner beziehungsweise weitere Beteiligte, Zahlende und berechtigte Empfänger unterscheiden. Eine Mailadresse beweist keine Vertretungsmacht.
3. [Kollision und Vorbefassung prüfen](../kollision-und-vorbefassung-pruefen/SKILL.md). Treffer in beschränktem Prüfvermerk festhalten. Die betroffenen Personen und Rechtsverhältnisse zuordnen, Streitstoff statt bloßer Namensgleichheit vergleichen. Über Tätigkeitsverbot oder Versagung entscheidet der Berufsträger. Bei offener Vorbefassung nur eingeschränkt zugänglichen Klärungsvorgang anlegen.
4. [Fristen aus dem Eingang sichern](../eingang-und-fristen-sichern/SKILL.md). Bei fehlendem Zustellbeleg eine vorläufige Eilvorlage auslösen. Belegte Kalenderhandlungen, Altstand und nachträgliche Änderungen nachvollziehbar halten, vgl. BGH, Beschluss vom 04.03.2026 – XII ZB 338/24, Rn. 11–13. Gibt es keine laufende Rechtsmittelfrist, reicht je nach Auftrag eine Wiedervorlage.

## 3. Die Akte befüllen

Forderungsdurchsetzung beginnt mit [Anspruchsinhaber, Schuldner und Zahlungen](../forderungsvorgang-anlegen/SKILL.md). Ein Bescheid oder ein internes Organisationsprojekt erfordert jeweils eine eigene [Verwaltungsakte](../verwaltungsvorgang-anlegen/SKILL.md). Für ein Amtsgeschäft oder ein Begehren zu einer verwahrten Urkunde [notarielle Erfassung und Ablage](../notarielle-akte-zuordnen/SKILL.md) klären. Ein allgemeiner Beratungsauftrag bekommt eine Handakte mit Frage, Beratungsumfang, gewünschtem Ergebnis und Gesprächsstand. Trage nur aktenbezogene Unterlagen ein. Ein Mitarbeiter, der einen Beleg gebracht hat, wird dadurch weder Mandant noch kostenpflichtiger Auftraggeber.

## 4. Konkrete Übergabe

Erstelle in dieser Reihenfolge:

1. Aktenstamm mit belastbarem Kurzrubrum, Arbeits-/Bestandszeichen, Auftrag, Bearbeitungsstand und Zeitpunkt, Rollen, Verantwortlichen und Zugriffsgruppe.
2. Dokumentenverzeichnis mit Eingangsdatum, geschildertem Ereignisdatum, Fundstelle und fehlenden Seiten oder Anlagen. Originale erhalten, Arbeitskopien kenntlich machen.
3. Dringende Aufgaben mit Fristart, Auslöser, Beleg, vertretbarem frühesten Termin, Wiedervorlage, Verantwortlichem und Bestätigung. Ohne konkreten Bezug keinen Fantasietermin setzen.
4. Empfängerfertiger erster Brief oder E-Mail-Entwurf und getrennte knappe Übergabenotiz. Der Brief nennt die tatsächlich übernommene Tätigkeit, bestätigt nur Erledigtes und fragt nach der entscheidenden Unterlage. Keine vertraulichen Altakteninhalte in einer Antwort an mehrere Personen offenlegen. Bei einer internen Akte einen internen Arbeitsauftrag an die zuständige Person statt eines Mandantenschreibens fertigen.
5. Bei nachgereichtem Beleg die betroffenen Felder, Beträge, Befugnisse oder Aufgaben im selben Stand nachvollziehbar ändern. Frühere Fristen und Zuordnungen mit Datum und Änderungsgrund dokumentieren. Doppelte Originale nach Identität kennzeichnen.

## 5. Lokale Arbeitsakte ausgeben

Steht Python zur Verfügung, kann das [Werkzeug für die Aktenanlage](../../werkzeuge/akte_anlegen.py) ein neues ZIP mit Originalen, Aktenstamm, offenen Punkten und Prüfsummen schreiben. Aufruf im entpackten Plugin: `python3 werkzeuge/akte_anlegen.py --stamm stamm.json --eingang eingang --ausgabe neue-akte.zip`. Wähle einen leeren neuen Ausgabepfad und begrenze den Eingangsordner auf Material, das zum Zielvorgang und dessen Berechtigten gehört.

Die JSON-Felder heißen `aktenzeichen`, `kurzrubrum`, `rolle`, `auftrag`, `zustaendig`, optional `offene_punkte` als Liste und `konfliktstatus` mit `offen`, `geprueft` oder `hindernis`. `rolle` ist `anwalt`, `notar`, `buero` oder `klaerung`. Bei offener Vorbefassung bleibt die Rolle `klaerung`. Ein Beispiel für einen gewöhnlichen Verwaltungseingang:

```json
{"aktenzeichen":"ORG-26-7","kurzrubrum":"Archivumzug Westentor","rolle":"buero","auftrag":"Transportauftrag zuordnen","zustaendig":"Büroleitung","konfliktstatus":"geprueft","offene_punkte":["Personaleinsatz vor Zutritt abgleichen"]}
```

Ohne Exportfunktion die gleichen Aktenfelder mit Originaldateinamen im Chat liefern. Ein ZIP ist kein Eintrag im Fristenkalender und kein Eintrag im Urkundenverzeichnis. Bei einer komplexen Konstellation kann eine lokale, tatsächlich verfügbare Fallansicht die Beteiligtenbeziehungen und den nächsten Entscheidungspunkt zeigen. Dieselbe Übergabe muss auch ohne sie lesbar sein.

[Fundstellen und Anwendungsgrenzen](../../references/aktenanlage-quellen.md)

<!-- BEGIN werkstatt-visualisierung -->
## 6. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für die Eröffnung und Zuordnung der Akte:** Wer beauftragt wen in welcher Rolle und welches Original löst die erste Aufgabe aus?

**Erste Ansicht:** Stelle Auftraggeber, vertretene Person, Gegenpartei, Amtsbeteiligte und interne Freigabe nebeneinander. Belege die Zuordnung durch Nachricht und Anlage.

**Sinnvolle Interaktion:** Prüfe bei einer nachgereichten Vollmacht oder einem Alttreffer nur die betroffenen Rollen, Zugänge und Fristen erneut. Halte die Prüfung bei offenem Widerstreit in der geschützten Eingangsablage.

**Datengrundlage:** Eingang mit Zeitstempel, Rolle, Belegstelle, Zugriffsentscheidung, Fristbeleg, zuständige Person und Wiedervorlage. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** Aktenstamm, erste Aufgaben und das konkret benötigte Schreiben. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
