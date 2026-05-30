# 18 QR-Codes, Querverweise und interner Anlage-Index

Datum: 8. März 2026
Bearbeiter: Wiss. Mitarbeiterin Lea Stang (IT-technische Umsetzung: Fleischer)
Az.: DIS-SV-2026/088; 11 O 188/26

---

## Konzept des QR-Code-Index

Für den physischen Anlagen-Sammelband des Schiedsgerichts (Aktenstück 17) wurde ein QR-Code-System entwickelt, das die Navigation im 1.847-seitigen Dokument erleichtert:

Jede Anlage trägt auf ihrem Deckblatt:
1. **Anlage-Nummer** (z.B. S-W-038) in großer Schrift
2. **Kurzbezeichnung** (z.B. „Aufmaßprotokoll DN200, Strang A1, 22.05.2024")
3. **Seitenposition im Sammelband** (z.B. „Seiten 412–421 von 1.847")
4. **QR-Code** — verlinkt auf die digitale Version auf dem kanzleieigenen SharePoint (passwortgeschützt; Zugangsdaten werden dem Schiedsgericht separat mitgeteilt)
5. **SHA-256-Prüfsumme** der digitalen Version (8-stelliger Kurzcode, menschenlesbar)

---

## Technische Umsetzung (QR-Code-Generierung)

Fleischer hat ein Python-Skript entwickelt, das für alle 247 Anlagen automatisch Deckblätter erzeugt:

- Bibliotheken: `qrcode`, `reportlab`, `hashlib`
- Input: CSV-Datei mit Anlage-Nummer, Bezeichnung, URL, SHA-256-Hash
- Output: 247 PDF-Deckblätter (je 1 Seite, A4)
- Gesamtlaufzeit: ca. 4 Minuten

Die Deckblätter werden vor dem Druckauftrag in die Mastersequenz eingefügt (vgl. Aktenstück 17, Schritt 2).

---

## Querverweissystem im Schriftsatz

Neben den QR-Codes auf den Deckblättern enthält der Schriftsatz selbst ein strukturiertes Querverweissystem. Jeder Verweis auf eine Anlage im Schriftsatztext folgt dem Schema:

> *„... ergibt sich aus dem Aufmaßprotokoll vom 22.05.2024 **(S-W-038, Seite 412 des Sammelbands)**..."*

Die Seitenangabe bezieht sich auf die Gesamtseitenzählung des gebundenen Sammelbands — nicht auf die Seite innerhalb der Einzelanlage. Dies ermöglicht dem Schiedsrichter, direkt zur richtigen Stelle zu blättern, ohne das Inhaltsverzeichnis zu bemühen.

### Querverweistabelle (Auszug)

| Schriftsatz-Satz | Anlage | Sammelband-Seite | Verweis-Typ |
|---|---|---|---|
| Schriftsatz S. 12, Abs. 3 | S-W-038 | 412 | Mengenbeleg |
| Schriftsatz S. 15, Abs. 1 | S-W-014 | 189 | Vertragsbeleg |
| Schriftsatz S. 22, Abs. 2 | S-W-079 | 833 | FAT-Report |
| Schriftsatz S. 28, Abs. 4 | S-W-112 | 1.124 | Lieferschein |
| Schriftsatz S. 35, Abs. 1 | S-W-195 | 1.512 | Mehrkostenbeleg |

Die vollständige Querverweistabelle (alle 288 Einzelverweise im 48-seitigen Schriftsatz) liegt als Anhang zu `schiedsgerichtsschriftsatz_dis_anlagenkonvolut.docx` bei.

---

## Interner Kanzlei-Index (SharePoint)

Parallel zum physischen Sammelband wird ein digitaler Kanzlei-Index auf dem SharePoint der Kanzlei gepflegt. Der Index ist für alle Kanzleimitglieder zugänglich (nicht öffentlich) und enthält:

- Volltext-Suchfunktion über alle 3.847 Dokumente
- Filterung nach Dokumenttyp, Datum, Verfahren, Anspruchsposition
- Verlinkung zur Anlagenmatrix (Aktenstück 12)
- Automatische Benachrichtigung bei Änderungen (E-Mail an Dr. Söhnchen und Stang)

Der SharePoint-Index hat sich im Mandatsverlauf als unverzichtbar erwiesen: Bei der Beantwortung der richterlichen Hinweise (Aktenstück 15) konnte Stang innerhalb von 30 Minuten alle relevanten Dokumente identifizieren und aufbereiten — ein Vorgang, der ohne Index Stunden gedauert hätte.

---

## Visualisierung (Anlagenindex-Diagramm)

Das Diagramm `anlagenindex_diagramm.jpg` zeigt schematisch die Struktur des Anlagenkonvoluts:

- Kreis-Ebene 1 (innen): 3 Verfahren (LG, OLG, DIS)
- Kreis-Ebene 2 (mitte): Anlagengruppen (A: Vertragsgrundlagen, B: Baunachweise, C: Liefernachweise, D: Konformität, E: Mehrkosten)
- Kreis-Ebene 3 (außen): Einzelanlagen (K-Nummern / S-W-Nummern)

Dieses Diagramm wird dem Schiedsgericht als zusätzliche Orientierungshilfe auf dem Deckblatt des Sammelbands beigefügt (1 Seite, farbig, Anlage S-W-000 / Frontispiz).

---

## Bewertung und Ausblick

Das QR-Code-System hat mehrere Vorteile:

1. Das Schiedsgericht kann jederzeit auf die aktuelle, passwortgeschützte Digitalversion zugreifen — z.B. wenn der Vorsitzende im Büro ist und das Exemplar nicht zur Hand hat.

2. Bei Nachträgen (nachgereichte Anlagen S-W-248 ff.) werden neue Deckblätter generiert und per Post an das Schiedsgericht gesandt — die digitale Version wird sofort aktualisiert.

3. Die Prüfsummen auf den Deckblättern ermöglichen die Integritätsprüfung: Das Schiedsgericht kann jederzeit prüfen, ob die physische Anlage mit der Digitalversion übereinstimmt.

Der zeitliche Mehraufwand für das QR-Code-System (ca. 8 Arbeitsstunden Fleischer, 4 Arbeitsstunden Stang) ist angesichts der Komplexität des Verfahrens gut investiert.
