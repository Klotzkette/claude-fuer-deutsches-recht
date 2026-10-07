# ERV-Versandstandard der Schriftsatzwerkstatt

Stand: 09.08.2026. Die ERVV ist in der zuletzt durch Gesetz vom 22.06.2026 geänderten Fassung geprüft; die ERVB 2025 ist weiterhin die auffindbare aktuelle Bekanntmachung nach § 5 ERVV. Die amtlichen Links wurden am 09.08.2026 erneut kontrolliert. Die BRAK dokumentiert beA 4.5 seit 01.07.2026 und XJustiz 3.6.2 seit April 2026; für den konkreten Versand zählt der tatsächlich aktive Clientstand. Diese Referenz enthält ausschließlich technische und formale Versandregeln. Sie bewertet weder den rechtlichen Inhalt noch die Richtigkeit von Antrag, Vortrag, Beweis oder Frist.

## Amtliche Quellen

| Regel | Amtliche Quelle | Werkstattfolge |
|---|---|---|
| Elektronische Dokumente müssen für das Gericht bearbeitbar sein. | [§ 130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Hauptdokument und Anlagen öffnen, visuell prüfen und Eingang bestätigen lassen. |
| Der Schriftsatz benötigt qeS oder einfache Signatur der verantwortlichen Person plus sicheren Übermittlungsweg. Anlagen benötigen keine eigene Signatur. | [§ 130a Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Verantwortliche Person, Signaturart und tatsächlichen Versender vor Freigabe dokumentieren. |
| Standardformat ist PDF; TIFF ist nur zusätzlich zulässig, wenn eine bildliche Darstellung in PDF nicht verlustfrei möglich ist. | [§ 2 ERVV](https://www.gesetze-im-internet.de/ervv/__2.html) | Upload-Ordner grundsätzlich mit einzelnen PDFs bauen; TIFF-Ausnahme nicht automatisch wählen. |
| Können die bekanntgemachten Höchstgrenzen nicht eingehalten werden, regelt § 3 ERVV einen besonderen Übermittlungsweg mit Glaubhaftmachung und möglichst elektronischen Dokumenten auf zulässigem Datenträger. | [§ 3 ERVV](https://www.gesetze-im-internet.de/ervv/__3.html) | Nicht eigenmächtig aufteilen oder Datenträger bestimmen; rot stoppen und der verantwortlichen Person Dateiliste, Bytes und Lösungsvorschlag übergeben. |
| Mehrere elektronische Dokumente dürfen nicht mit einer gemeinsamen qeS übermittelt werden. | [§ 4 Abs. 2 ERVV](https://www.gesetze-im-internet.de/ervv/__4.html) | Keine Container- oder Sammelsignatur; qeS-Bezug zur konkreten Hauptschrift prüfen. Anlagen benötigen nach § 130a Abs. 3 ZPO keine eigene Signatur. |
| PDF einschließlich PDF 2.0, PDF/A-1, PDF/A-2 und PDF/UA ist vorgesehen; eingebettete Objekte und ausführbare Skripte sollen fehlen. | [ERVB 2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | Kein JavaScript, kein eingebettetes Office-Objekt, keine Zusatzverschlüsselung; Druckbarkeit prüfen. |
| Formularfelder ohne JavaScript und Hyperlinks sind nach der ERVB technisch zulässig. | [ERVB 2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | In der finalen Versandfassung offene Formularwerte und interaktive Funktionen trotzdem sichtbar prüfen und dokumentiert entscheiden. |
| Je Nachricht sind höchstens 1.000 Dateien und 200 MB zulässig. | [ERVB 2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | Vor Freigabe Dateizahl und Gesamtbytes berechnen; ab 900 Dateien oder 180 MB warnen. |
| Dateinamen dürfen amtlich höchstens 90 Zeichen einschließlich Endung haben und müssen logisch nummeriert sein. | [ERVB 2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | Strenger interner Standard: höchstens 80 Zeichen und nur ASCII. |
| Die BRAK hat beA 4.5 am 01.07.2026 bereitgestellt und die Umstellung auf XJustiz 3.6.2 im April 2026 beschrieben. | [BRAK beA-Newsletter 2026](https://www.brak.de/newsroom/newsletter/bea-newsletter/2026/) | Datum, real aktiven beA-/Kanzleisoftwarestand, XJustiz-Profil und clientseitige Warnungen im Preflight erfassen; keine bloß dokumentierte Versionsnummer als lokal aktiv unterstellen. |
| PAdES liegt in der PDF, CAdES in einer gesonderten Signaturdatei; das Format allein belegt noch keine qeS. Externe Signaturdateien können `.p7`, `.p7s`, `.p7m` oder `.pkcs7` verwenden. | [beA-Anwenderhandbuch zum Prüfprotokoll](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/oeffnen-und-anzeigen/pruefen-einer-qualifizierten-elektronischen-signatur-qes/erlaeuterungen-zum-pruefprotokoll), [Anhänge signieren](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/erstellen-und-senden/anhaenge-signieren) | Prüfprotokoll, Signaturniveau, Unterzeichner und Bezug zur konkreten finalen PDF kontrollieren; CAdES im Signaturmanifest erfassen. |
| Eingang liegt vor, wenn das Dokument auf der Empfangseinrichtung des Gerichts gespeichert ist; eine automatisierte Bestätigung ist zu erteilen. | [§ 130a Abs. 5 ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Nicht bei `gesendet` stehen bleiben; Eingangsbestätigung öffnen, prüfen und sichern. |
| Bei ungeeignetem Dokument kann unverzügliche geeignete Nachreichung den früheren Zeitpunkt erhalten, wenn Inhaltsgleichheit glaubhaft gemacht wird. | [§ 130a Abs. 6 ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Fehler nicht still überschreiben; Erstfassung, Meldung, Korrektur und Inhaltsgleichheit dokumentieren. |
| Bei vorübergehender technischer Unmöglichkeit gelten besondere Anforderungen an Ersatzeinreichung und Glaubhaftmachung. | [§ 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html) | Sofort an die verantwortliche anwaltliche Person übergeben; das Plugin entscheidet den Ersatzweg nicht selbst. |

## Signaturmatrix

1. **qeS:** Die verantwortliche Person versieht den Schriftsatz mit einer prüfbaren qualifizierten elektronischen Signatur. Vor Übergabe werden Signaturdatei beziehungsweise eingebettete Signatur, Zertifikatsstatus und Dokumentidentität geprüft. Eine gemeinsame qeS für mehrere elektronische Dokumente wird nicht verwendet.
2. **Einfache Signatur und sicherer Übermittlungsweg:** Unter dem Schriftsatz steht der Name der verantwortlichen Person. Genau diese Person löst den Versand persönlich über ihren sicheren Übermittlungsweg aus.
3. **Abweichende Person:** Soll eine andere Person den Versand auslösen, bleibt das Paket rot, bis eine wirksame qeS der verantwortlichen Person vorliegt oder der Versandweg anwaltlich anders freigegeben ist.
4. **Anlagen:** Anlagen zum formgerechten Schriftsatz benötigen keine eigene Signatur. Vorhandene elektronische Signaturen in Beweisdateien dürfen durch Konvertierung oder Stempelung nicht unbemerkt zerstört werden.
5. **Unterschriftsbild:** Eine eingescannte oder eingefügte Unterschriftsgrafik wird nicht automatisch als einfache Signatur behandelt. Die Werkstatt verlangt eine lesbare Namenswiedergabe am Dokumentende und eine eindeutige Zuordnung zur verantwortlichen Person; eine qeS ersetzt die Grafik nicht.

Der sichere Übermittlungsweg ersetzt nur die qeS-Alternative. Er beseitigt nicht die Pflicht zur einfachen Signatur durch lesbare Namenswiedergabe der verantwortlichen Person.

## Paketgrenzen

- Genau ein Verfahren je Nachricht; Gericht, SAFE-Empfänger, Aktenzeichen oder `Neueingang` und Betreff vor Versand prüfen.
- Hauptschriftsatz und jede Anlage getrennt als PDF. Keine ZIP-Datei als Ersatz für die Einzelunterlagen.
- Im vorbereiteten Upload-Ordner liegen keine Symlinks, Unterordner oder internen Protokolle. Neben Versand-PDFs sind nur zugeordnete CAdES-Dateien mit `.p7`, `.p7s`, `.p7m` oder `.pkcs7` zulässig. Eine vom Signatur-/Versandsystem erzeugte Signaturdatei wird nicht vorab erfunden, umbenannt oder einer anderen PDF zugeordnet.
- Keine passwortgeschützten oder zusätzlich verschlüsselten PDFs.
- Keine Makros, eingebetteten Office-Dateien, Audio-/Videoobjekte oder ausführbaren Skripte.
- Der Upload-Ordner enthält nur tatsächlich zu sendende Dateien. Manifest, Konvertierungsprotokoll und Freigabekarte bleiben intern.
- Erzeugt das eingesetzte Signatur-/Versandsystem bei qeS zusätzlich eine separate Signaturdatei, werden Dateizahl und Gesamtbytes nach deren Erzeugung erneut geprüft. Das interne `signaturmanifest.csv` bindet sie über Zielname und Zielhash an genau eine finale PDF und dokumentiert eigenen Hash/Bytes, CAdES/qeS, grünen Prüfstatus, Unterzeichner und Prüfprotokoll. Die Werkstatt benennt das Systemartefakt nicht um und rechnet es nicht still aus der Nachricht heraus.
- XJustiz-Daten werden im beA-/Kanzleisystem anhand von Gericht, Aktenzeichen, Parteien und Gegenstand gepflegt; die Werkstatt erfindet keine Empfänger- oder Verfahrensdaten.
- Vor der Freigabe wird das fertige Paket im tatsächlich vorgesehenen beA-/Kanzleisystem als Entwurf geladen oder mit dessen aktueller Vorprüfung kontrolliert. Dateinamens-, Anhangs-, Signatur- oder XJustiz-Warnungen werden wörtlich protokolliert und nicht durch eine bloß lokal erfolgreiche PDF-Prüfung überstimmt.

## Rote Stopps

- Hauptschriftsatz oder verantwortliche Person nicht eindeutig.
- einfache Signatur und tatsächlicher Versender stimmen nicht überein.
- qeS fehlt, ist ungültig oder gehört nicht zur gesperrten PDF-Fassung.
- Frist, Gericht, Aktenzeichen oder Empfänger sind ungeklärt.
- Datei lässt sich nicht vollständig öffnen, drucken oder lesen.
- Passwortschutz, Verschlüsselung, ausführbarer Inhalt oder defektes PDF.
- Anlagenzitat, sichtbare Kennzeichnung und Dateiname widersprechen sich.
- Upload überschreitet 1.000 Dateien oder 200 MB.
- automatisierte Eingangsbestätigung fehlt oder weist Fehler aus.

## Operative Kontrollspur

Der [100-Punkte-Fehlerkatalog](./100-punkte-fehlerkatalog.md) übersetzt diese Vorgaben in konkrete Stopps von der Ordnerannahme bis zur Eingangsbestätigung. Der Paketvalidator automatisiert nur objektiv prüfbare Merkmale; er ersetzt keine visuelle Seitenprüfung, Zertifikatsprüfung, Empfängerbestätigung oder reale Freigabe.
