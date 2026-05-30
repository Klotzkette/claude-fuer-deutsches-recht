# 05 beA-Übertragung und XJustiz-Hash-Probleme

Datum: 21.–24. Januar 2026
Bearbeiter: Wiss. Mitarbeiterin Lea Stang; IT-Beauftragter Kanzlei: Dominik Fleischer
Az.: 11 O 188/26 (LG Aachen)

---

## Hintergrund: Elektronischer Rechtsverkehr und beA

Seit dem 01.01.2022 sind Rechtsanwälte nach § 130a ZPO (https://dejure.org/gesetze/ZPO/130a.html) i.V.m. der ERVV (Elektronischer-Rechtsverkehr-Verordnung) verpflichtet, Schriftsätze und Anlagen elektronisch beim Gericht einzureichen. Das besondere elektronische Anwaltspostfach (beA) der Bundesrechtsanwaltskammer ist das Pflichtpostfach.

Die Werkmann-Klage wurde am 21.01.2026 um 17:42 Uhr über das beA eingereicht. Das beA-System vergibt für jede Übertragung ein Transferprotokoll mit Zeitstempel und einer XJustiz-konformen Metadatenstruktur.

---

## Das Hash-Problem

### XJustiz-Standard Version 3.3.1

Das LG Aachen hat seit dem 01.10.2025 den XJustiz-Standard Version 3.3.1 im Einsatz. Dieser Standard schreibt für die Anlageübertragung unter anderem vor:
- Hashalgorithmus: SHA-256 (verpflichtend)
- Metadatenbeschriftung: Anlagenbezeichnung nach dem Schema `KL_[Anlage-ID]_[Datum-YYYYMMDD]_[Seitenzahl]`
- Dateiformat: PDF/A-2b (bevorzugt) oder PDF/A-1b

Die Kanzlei-Software (RA-Micro, Version 2025.3) erzeugte die XJustiz-Metadaten automatisch. Bei der Nachprüfung stellte Stang fest, dass für 13 der 247 Anlagen die erzeugten SHA-256-Hashes **nicht mit den Prüfsummen übereinstimmten**, die die Kanzlei intern beim Erstellen der PDF-Dateien protokolliert hatte.

### Detailanalyse der Hash-Abweichungen

Stang konnte nach Analyse drei Ursachenkategorien identifizieren:

**Kategorie 1 (8 Anlagen): PDF/A-Konvertierung**
RA-Micro konvertierte die ursprünglich als DOCX- oder DWG-Dateien erstellten Anlagen automatisch in PDF/A-2b. Bei dieser Konvertierung werden Metadaten (Erstellungsdatum, Autorname) in die PDF eingebettet, was den Hash verändert. Das ist technisch korrekt — aber die Kanzlei hatte die Hash-Prüfsummen *vor* der Konvertierung berechnet. Lösung: Hash-Protokollierung erst nach Konvertierung.

**Kategorie 2 (3 Anlagen): Parallelzugriff**
Drei Anlagen wurden von zwei Rechnern gleichzeitig geöffnet und gespeichert (Serverkonflikt im Kanzlei-LAN). Das DMS-System hatte zwei konkurrierende Versionen erstellt; beA übermittelte die ältere Version. Lösung: DMS-Sperrmechanismus aktivieren.

**Kategorie 3 (2 Anlagen): Anlage K17 und K44**
Diese Anlagen hatten Hash-Konflikte, weil Stang nach dem K17-Vorfall (Aktenstück 04) Korrekturdateien unter denselben Dateinamen abgelegt hatte. Die Versionierung war unzureichend. Lösung: Versionshistorie im DMS vollständig aktivieren.

---

## Konsequenzen und Sofortmaßnahmen

### Berichtigungsübertragung

Am 24.01.2026 wurde eine korrigierte Einreichung für die 13 betroffenen Anlagen über beA vorgenommen. Das LG Aachen (Frau Knoops) bestätigte den Eingang. Das neue Übertragungsprotokoll (SHA-256-Prüfsummen korrekt) ist als redaktiertes Dokument in der Akte abgelegt (vgl. PDF `bea_uebertragungsprotokoll_xjustiz_redacted.pdf`).

### XJustiz-Helpdesk-Kontakt

Die Kanzlei nahm Kontakt mit dem XJustiz-Helpdesk auf (E-Mail vom 18.04.2026, vgl. `2026-04-18_xjustiz_helpdesk_hash_problem.eml`). Der Helpdesk bestätigte, dass das beschriebene Konvertierungsproblem ein bekannter Fehler in RA-Micro 2025.3 ist und ein Patch (Version 2025.3.1) verfügbar ist. Patch wurde eingespielt.

---

## Verfahrensrechtliche Relevanz

### Zustellung und Wirksamkeit

Nach § 130a Abs. 5 ZPO (https://dejure.org/gesetze/ZPO/130a.html) ist ein elektronisches Dokument eingegangen, wenn es auf dem Empfängersystem gespeichert ist. Die Wirksamkeit der Klageeinreichung wird durch Hash-Abweichungen grundsätzlich nicht berührt — Hash-Prüfung ist eine Integritätsprüfung, kein Wirksamkeitsmerkmal. Gleichwohl kann die Gegenseite im Streitfall behaupten, die übermittelte Anlage entspreche nicht dem Original.

### Gegnerische Rügemöglichkeit

Der Anwalt der Gegenseite (Dr. Kessling) hat in einem telefonischen Gespräch angedeutet, die Authentizität einzelner Anlagen im Verfahren zu rügen (dazu Aktenstück 06). Ein sauberes Hash-Protokoll ist daher nicht nur technische Sorgfalt, sondern prozessrechtlich relevant.

### Checkliste für künftige Einreichungen

| Schritt | Zeitpunkt | Verantwortlich |
|---|---|---|
| PDF/A-Konvertierung aller Anlagen | Vor Hash-Berechnung | Stang |
| SHA-256-Hash-Berechnung | Nach Konvertierung | IT Fleischer |
| Hash-Protokoll speichern | Vor beA-Upload | Stang |
| DMS-Sperrung aktivieren | Vor Bearbeitung | Fleischer |
| Versionierung prüfen | Bei jeder Änderung | Stang |
| Transferprotokoll archivieren | Nach beA-Eingang | Fleischer |

---

## Technische Dokumentation

Das vollständige Übertragungsprotokoll (XJustiz-Metadaten, SHA-256-Hashes aller 247 Anlagen) ist als redaktiertes PDF in der Akte hinterlegt. Redaktiert wurden: Kanzlei-interne Netzwerkpfade, Mitarbeiter-IDs und der API-Key des DMS-Systems. Das Original liegt im Kanzlei-Tresor.

Kontakt XJustiz-Koordinierungsstelle: xjustiz@bundesjustizamt.de (https://www.xjustiz.de/)
