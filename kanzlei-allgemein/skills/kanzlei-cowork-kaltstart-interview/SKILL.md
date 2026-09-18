---
name: kanzlei-cowork-kaltstart-interview
description: "Für /kanzlei-allgemein:kanzlei-cowork-kaltstart-interview: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# 1. Kanzleikonfiguration einrichten

Erstelle oder ergänze das beauftragte Kanzleiprofil anhand bestehender Konventionen. Bei einem einzelnen Mandatsauftrag verwende vorhandene Vorgaben, statt ein vollständiges Einrichtungsinterview voranzustellen.

## 1.1. Vorhandene Konfiguration lesen

Prüfe bei entsprechendem Auftrag die vorhandene Datei `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/CLAUDE.md`. Vollständig bestätigte Angaben weiterverwenden; offene Platzhalter und widersprüchliche Einstellungen gezielt klären. Eine vorhandene Datei nicht allein wegen fehlender Platzhalter als sachlich richtig bestätigen.

Nur die freigegebene Konfiguration ändern. Kein Profil löschen, keine Integration verbinden und keine Mandantenakte anlegen, wenn dies nicht beauftragt ist.

## 1.2. Offene Einstellungen fachlich klären

### 1.2.1. Kanzlei und Akten

Rechtsform, Standort, Kammerbezirk, Anwälte, Mitarbeiterrollen und Sekretariat nur soweit erforderlich erheben. Rechtsgebiete, Mandantenstruktur und Fachzuständigkeiten den konkreten Abläufen zuordnen. Paragrafen 43, 43a und 51 BRAO sowie Paragraf 8 PartGG nach der jeweiligen Organisationsfrage prüfen.

Bestehendes Aktennummernsystem und Verzeichniskonvention verwenden. Der technische Aktenpfad bleibt `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandate/<az>/`; mögliche vorhandene Unterordner sind `01_stammdaten 02_korrespondenz 03_schriftsaetze 04_anlagen 05_fristen 06_honorar`. Abweichungen nicht ohne Auftrag vereinheitlichen.

### 1.2.2. Postfach, Versand und Fristen

Tatsächliche beA-Verfügbarkeit, Berechtigungen, Signaturmittel und weitere Kanäle wie EGVP, Post oder sicherer Mandantenzugang klären. Paragraf 31a BRAO und konkrete elektronische Einreichungspflicht auseinanderhalten; kein pauschales Einrichtungsdatum für sämtliche Pflichten übernehmen.

Verbindlichen Fristenkalender, Kontrolle, Vertretung und Vorfristen aus der Kanzleivorgabe bestimmen. Eine typische Fünf-Tage-Vorfrist nicht als verbindliche Einstellung erfinden. Fehlt die verantwortliche Person, gezielt fragen; nach Antwort Kalender- und Versandablauf gemeinsam aktualisieren.

### 1.2.3. Honorar, Buchhaltung und Mahnung

RVG-Abrechnung, Honorarvereinbarung, Stundensätze, Zeitnachweise, Zwischenrechnungen und Freigabe unterscheiden. Vorhandene Software und Übergabe an die Steuerkanzlei berücksichtigen. RVG, insbesondere Vergütungsverzeichnis und Gebührentabelle, sowie erforderliche Rechnungsregeln nach ihrer tatsächlichen Funktion prüfen.

Mahnpraxis, Zahlungsabgleich und Entscheidung über gerichtliche Schritte klären, ohne automatisch feste Mahnstufen oder Gebühren anzunehmen. Für UStVA Zeitraum, zuständiges Fachsystem und Verantwortliche festhalten; keine Meldung aus einer bloßen Profilbestellung ableiten.

### 1.2.4. Mandantenpflege und Datenschutz

Geburtstags-, Weihnachts- und Newsletterverteiler nur auf Wunsch einbeziehen. Freigegebene Empfänger, Kanal und Datenschutz prüfen; keine Nachricht automatisch versenden. Artikel 5, 6 und 9 DSGVO für die jeweiligen Daten sowie Artikel 28 bei Auftragsverarbeitung unterscheiden.

## 1.3. Rückfragen und fertiges Profil

Stelle kurze zusammenhängende Fragen nur zu offenen Entscheidungen des beauftragten Bereichs. Nach Antwort betroffene Einstellungen und Folgeabläufe aktualisieren, etwa Rechnungsfreigabe nach Wechsel der Buchhaltung. Zeigt die Antwort eine weitere entscheidende Lücke, gezielt nachfragen; bestätigte Angaben nicht erneut abfragen.

Liefere das vereinbarte Profil in vollständigen verständlichen Sätzen unter dem gewünschten Dateinamen oder im beauftragten bestehenden Pfad. Noch offene Teile als vorläufig kennzeichnen; nach Ergänzung fertigstellen. Formatierte Dokumente möglichst in Times New Roman 11 pt und dezimaler Gliederung, sonst mit getrenntem Exporthinweis.

## 1.4. Quellen, Beispiel und Grenzen

Tragende Normen und aktuelle technische Vorgaben prüfen; Entscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage. Optional ergänzt `references/zitierweise.md` die Zitierweise. Quellenstatus nicht in Mandantenkorrespondenz übernehmen.

Bei Wechsel des verbindlichen Fristenkalenders die Zuständigkeit für Übertragung und Kontrolle klären. Danach die betroffenen Profilabschnitte ausarbeiten, ohne vorhandene Fristen ungefragt zu verschieben oder zu löschen.

Optional unterstützen `/kanzlei-allgemein:fristenbuch-fuehren`, `/kanzlei-allgemein:sekretariats-tagesbrief` und `/kanzlei-allgemein:versand-vor-check` passende Folgeaufgaben. Vor Versand Identität, Freigabe, Empfänger, Signatur und Anlagen selbst prüfen; kein Skillverweis ersetzt die Kontrolle. Außenhandlungen verbleiben in anwaltlicher Verantwortung und benötigen ausdrückliche Freigabe.

Ohne diese Ressourcen anhand des vorliegenden Ablaufs weiterarbeiten. Fehlenden Zugriff konkret benennen; ohne Export vollständigen Text liefern.
