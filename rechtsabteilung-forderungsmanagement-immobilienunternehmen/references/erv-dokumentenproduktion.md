# ERV-, eBO- und beA-Dokumentenproduktion

Stand: 09.08.2026. Diese Referenz ist die technische und rechtliche Kontrollspur für gerichtsfertige Schriftsatzpakete. Sie beschreibt die Paketvorbereitung; ein Modell versendet weder aus beA noch eBO und ersetzt keine reale Signatur-, Freigabe- oder Fristentscheidung. Der ERVV-Normtext ist bis zur Änderung durch Art. 2 des Gesetzes vom 22.06.2026 (BGBl. 2026 I Nr. 192) abgeglichen. Der amtliche Technikabgleich erfasst zusätzlich beA 4.5 und die beA-Umstellung auf XJustiz 3.6.2; maßgeblich bleibt beim Versand der tatsächlich aktive Clientstand.

## 1. Zielbild

Ein fertiges Gerichtspaket besteht aus:

1. genau einer freigegebenen Fassung des Hauptschriftsatzes,
2. jeder Anlage als eigener lesbarer PDF-Arbeitskopie,
3. stabilen Anlagenbezeichnungen im Schriftsatz und auf der Anlage,
4. logisch nummerierten, kurzen Dateinamen,
5. Anlagenverzeichnis und technischem Manifest,
6. dokumentiertem Signatur- und Übermittlungsweg,
7. Versandauftrag für die verantwortende Person sowie
8. Eingangsbestätigung und unveränderbarem Einreichungsvermerk.

Originale bleiben unverändert. Kennzeichnung, OCR, Drehung oder Formatkonvertierung erfolgen nur auf abgeleiteten Arbeitskopien; Original und Arbeitskopie erhalten getrennte Hashwerte.

## 2. Verbindliche Normen und amtliche Standards

| Thema | Quelle | Arbeitsregel |
|---|---|---|
| Inhalt vorbereitender Schriftsätze | [§ 130 ZPO](https://www.gesetze-im-internet.de/zpo/__130.html) | Parteien, Gericht, Streitgegenstand, Anträge, Tatsachen, Einlassung, Beweismittel und Anlagenzahl kontrollieren. |
| Klageschrift | [§ 253 ZPO](https://www.gesetze-im-internet.de/zpo/__253.html) | Gericht und Parteien bestimmt bezeichnen; Gegenstand, Grund und bestimmter Antrag müssen tragfähig sein. |
| Elektronisches Dokument | [§ 130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Zur gerichtlichen Bearbeitung geeignetes elektronisches Dokument; qualifizierte elektronische Signatur oder einfache Signatur plus sicherer Übermittlungsweg. Anlagen benötigen keine eigene Signatur. Eingang ist die Speicherung auf der Empfangseinrichtung des Gerichts. |
| Aktive Nutzungspflicht | [§ 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html) | Rechtsanwälte, Behörden und juristische Personen des öffentlichen Rechts reichen elektronisch ein; eine technische Ersatzeinreichung und ihre vorübergehende Unmöglichkeit sind unverzüglich glaubhaft zu machen. |
| Eigenübermittlung der privaten Konzerngesellschaft | [§ 130a Abs. 4 S. 1 Nr. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) und [§ 10 ERVV](https://www.gesetze-im-internet.de/ervv/__10.html) | Eine private juristische Person kann ein identifiziertes eBO als sicheren Übermittlungsweg verwenden. Postfachinhaber, authentisierter Versand, verantwortende Person, Signatur und Vertretungsbefugnis müssen zum konkreten Vorgang passen. |
| Aktueller ERVV-Normstand | [ERVV-Gesamttext](https://www.gesetze-im-internet.de/ervv/BJNR380300017.html) | Vor jeder Release- oder Einreichungsprüfung den aktuellen Änderungsstand öffnen. Prüfstand hier: zuletzt geändert durch Art. 2 des Gesetzes vom 22.06.2026 (BGBl. 2026 I Nr. 192). |
| Dateiformat und Strukturdaten | [§ 2 ERVV](https://www.gesetze-im-internet.de/ervv/__2.html) | PDF ist Standard; TIFF nur zusätzlich, wenn eine bildliche Darstellung in PDF nicht verlustfrei möglich ist. XJustiz-Datensatz soll Gericht, Aktenzeichen, Parteien und Gegenstand enthalten. |
| Aktueller Technikstandard | [ERVB 2025 vom 29.07.2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf) | Druckbar; höchstens 90 Zeichen einschließlich Endung; zulässige Zeichen und logische Nummerierung; höchstens 1.000 Dateien und 200 MB je Nachricht. |
| Aktueller beA-/XJustiz-Stand | [BRAK beA-Newsletter 2026](https://www.brak.de/newsroom/newsletter/bea-newsletter/2026/) | beA 4.5 wurde am 01.07.2026 bereitgestellt; die Umstellung auf XJustiz 3.6.2 wurde am 13.04.2026 dokumentiert. Vor Übergabe den real aktiven beA-/Kanzleisoftwarestand, das verwendete XJustiz-Profil und sämtliche clientseitigen Dateinamens- oder Anhangswarnungen protokollieren. Keine Struktur- oder Empfängerdaten erfinden. |
| Bundeseinheitlicher Leitfaden | [Leitfaden zum elektronischen Rechtsverkehr](https://justiz.de/ervvoe/leitfaden_erv_pdf.pdf) | Ein Verfahren je Nachricht; einzelne PDFs statt ZIP; keine Zusatzverschlüsselung oder Lesesperre; Empfangsbestätigung prüfen. |
| NRW-E-Akten-Namen | [Hinweise NRW](https://www.justiz.nrw.de/Gerichte_Behoerden/anschriften/elektronischer_rechtsverkehr/ERV_Hinweise) und [Namenskonvention](https://www.justiz.nrw.de/sites/default/files/imported/files/2022-11/Namenskonvention-fuer-Externe-Nutzer.pdf) | Bekanntes Aktenzeichen verwenden, sonst `Neueingang`; Hauptdokument mit Parteirolle kennzeichnen; bedeutungslose Namen vermeiden; Anlagen logisch als `Anlage_01` usw. benennen. |

Die ERVB erlaubt Umlaute und ß. Der Konzernstandard transliteriert trotzdem zu `ae`, `oe`, `ue`, `ss` und begrenzt Dateinamen auf 80 Zeichen einschließlich `.pdf`. Das ist eine konservative Kompatibilitätsregel für beA, DMS und gerichtliche E-Akten, keine Behauptung über den gesetzlichen Mindeststandard.

## 3. Rollen und Signatur

### 3.1 Fachangestellte

Fachangestellte dürfen Entwurf, PDF-Paket, Anlagenmanifest, XJustiz-Daten, Versandauftrag und Preflight vollständig vorbereiten. Im zulässigen Parteiprozess können sie die private Konzerngesellschaft nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO vertreten, wenn Beschäftigtenstatus, Konzernverbund, Vollmacht und interne Freigabe belegt sind. Sie dürfen weder eine anwaltliche Prüfung noch eine verantwortende Signatur oder Postfachberechtigung simulieren. Der interne Status bleibt bis zur realen Freigabe `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

### 3.2 Verantwortender Rechtsanwalt

Bei einfacher Signatur muss die im Schriftsatz namentlich ausgewiesene verantwortende Person den Schriftsatz grundsätzlich selbst über ihr beA versenden. Soll ein anderer Anwalt senden, reicht die bloße einfache Signatur des ersten Anwalts nicht. Dann muss die konkrete qualifizierte Signatur- oder Verantwortungsvariante vor Fristablauf geklärt werden.

### 3.3 Eigenvertretung der privaten Konzerngesellschaft

Eine private GmbH wird nicht allein wegen ihrer Rechtsform von Paragraf 130d ZPO erfasst. Handelt die Konzerngesellschaft ohne Rechtsanwalt im zulässigen Parteiprozess, wird der Einreichungsweg deshalb eigenständig bestimmt:

1. Für die elektronische Eigenübermittlung darf nur ein tatsächlich eingerichtetes und identifiziertes eBO der richtigen Gesellschaft oder eindeutig bezeichneten Untergliederung verwendet werden. Paragraf 130a Abs. 4 S. 1 Nr. 3 ZPO und Paragraf 10 ERVV sind die Normanker.
2. Der Schriftsatz benötigt eine qualifizierte elektronische Signatur der verantwortenden Person oder deren einfache Signatur in Verbindung mit dem sicheren Übermittlungsweg. Postfachinhaber, verantwortende natürliche Person, Versandberechtigung und Vertretungsbefugnis werden im Versandauftrag dokumentiert.
3. Fehlt ein nutzbares eBO, wird nicht aus einem fremden beA oder einem bloßen EGVP-Zugang versendet. Dann ist vor Fristablauf zu bestimmen, ob eine eigenhändig unterzeichnete schriftliche Einreichung nach den allgemeinen Vorschriften im konkreten Verfahren zulässig ist.
4. Bei freiwilliger eBO-Nutzung einer privaten Gesellschaft wird eine technische Störung nicht automatisch zu einer Ersatzeinreichung nach Paragraf 130d ZPO. Der rechtzeitig verfügbare, formwirksame Alternativweg ist stattdessen konkret festzulegen.

### 3.4 Kein Mischweg

Ein beA gehört zur verantwortenden anwaltlichen Person; ein eBO gehört zur identifizierten Gesellschaft oder Vereinigung. Beschäftigte einer GmbH erhalten durch Paragraf 79 ZPO kein Recht, ein anwaltliches Postfach zu verwenden. Ebenso darf eine Kanzlei ihre Pflicht nach Paragraf 130d ZPO nicht dadurch umgehen, dass die Fachabteilung denselben anwaltlich verantworteten Schriftsatz ohne geklärte Rollenänderung auf einem anderen Weg einreicht.

## 4. Quellfassung sperren

Vor Konvertierung werden festgehalten:

| Feld | Mindestinhalt |
|---|---|
| Aktenstand | Akten-ID, Datenstichtag, letzte Zahlung, Fremd-Aktenzeichen |
| Hauptdokument | Quelldatei, Version, Änderungsdatum, Hash |
| Freigabe | Person, Zeitpunkt, freigegebene Version, Auflagen |
| Anlagenstand | höchste K-/B-Nummer, bereits eingereicht, neu, zurückgezogen |
| Frist | Ablauf, Vorfrist, verantwortliche Person, Notfallweg |

Ändern sich Betrag, Antrag, Partei, Frist, Beweis, Anlage, Zustellweg oder Datenstichtag, erlischt die Freigabe. Keine stille Korrektur nach Freigabe.

## 5. Dokumentgestaltung

Vor der Finalisierung wird einmal gefragt, welches Profil gelten soll:

| Profil | Gestaltung |
|---|---|
| Konzernbriefkopf | freigegebener Briefkopf, definierte Schrift, Aktenzeichen, Seitenzahlen, Unterschriftsblock |
| Kanzleibriefkopf | nur durch beauftragte Kanzlei oder auf deren freigegebener Vorlage |
| Gericht-neutral | klare Ränder, lesbare Standardschrift, Aktenzeichen in Kopfzeile, Seitenzahlen, keine Dekoration |

Interne Freigabestatus, Kommentare, Änderungsverfolgung, Metadaten-Notizen und Prüfvermerke gehören nicht in das außenwirksame Dokument. Rubrum, Anträge, Gliederung, Beweisangebote und Anlagenverzeichnis müssen vollständig ausformuliert und visuell ruhig sein.

## 6. Anlagenproduktion

### 6.1 Nummerierung

- Klägerseite: `Anlage K 1`, `Anlage K 2` usw.
- Beklagtenseite: `Anlage B 1`, `Anlage B 2` usw.
- Nach einem weiteren Schriftsatz wird die letzte Nummer fortgesetzt.
- Eine bereits eingereichte Nummer wird nie still einem anderen Dokument zugewiesen.
- Ein zurückgezogenes Dokument bleibt in der Historie erkennbar; die Nummer wird nicht recycelt.

### 6.2 Sichtbare Kennzeichnung

Die abgeleitete Einreichungs-PDF trägt auf der ersten Seite rechts oben die Bezeichnung `Anlage K 1` oder `Anlage B 1`. Die Kennzeichnung darf Inhalt, Unterschrift, Stempel, Barcode oder Seitenzahl nicht verdecken. Fehlt freier Rand, wird zusätzlicher Rand erzeugt oder ein Anlagen-Deckblatt vorgeschaltet. Das Original bleibt unverändert.

### 6.3 PDF-Qualität

Jede Datei wird geöffnet und geprüft auf:

1. richtige Seitenfolge und Seitenzahl,
2. Leserichtung und Beschnitt,
3. lesbare Tabellen, Fotos, Handschrift und Kleindruck,
4. Suchtext oder nachvollziehbaren OCR-Status,
5. Druckbarkeit und darstellbare Schriften,
6. fehlende oder leere Seiten,
7. Kommentare, Formulare, Skripte, eingebettete Objekte und Dateischutz,
8. erforderliche Schwärzungen und Datenminimierung.

Bei Excel- oder SAP-Ausgaben werden Druckbereiche, wiederholte Tabellenköpfe, Spaltenbreite und Seitenumbrüche kontrolliert. Eine unlesbare Verkleinerung ist keine fertige Anlage.

## 7. Dateinamenschema

### 7.1 Konzernstandard

- logische zweistellige Reihenfolge am Anfang,
- Hauptdokument zuerst,
- nur ASCII, Ziffern, Unterstrich und Minus,
- höchstens 80 Zeichen einschließlich `.pdf`,
- sprechend, aber ohne interne Pfade, Passwörter oder unnötige Personendaten,
- nur der Punkt vor der Dateiendung.

### 7.2 Muster

```text
01_K_Klage_Mietrueckstand.pdf
01_K_Replik_Mietrueckstand.pdf
01_B_Klageerwiderung_Mietrueckstand.pdf
02_Anlage_K01_Mietvertrag_2022-05-01.pdf
03_Anlage_K02_Mietkonto_2026-07-10.pdf
04_Anlage_K03_Mahnung_2026-05-14.pdf
05_Anlagenverzeichnis_K01-K03.pdf
```

NRW empfiehlt die Parteirolle nur am Hauptdokument. Der Konzernstandard folgt dem. Die K-/B-Zuordnung der Anlage bleibt im sichtbaren Anlagenstempel und in der sprechenden Dateibezeichnung erhalten, damit Geschäftsstelle, Kanzlei und DMS dasselbe Dokument sicher zuordnen können.

Das Anlagenverzeichnis steht regelmäßig im Hauptschriftsatz. Eine zusätzliche Verzeichnis-PDF wird nur erzeugt, wenn Kanzlei-, Gerichts- oder interner Paketstandard sie verlangt; sie darf nicht als weitere Beweisanlage missverstanden werden.

## 8. Technisches Manifest

Das lesbare Übergaberegister bleibt kompakt:

| Nr. | Schriftsatzbezug | Zieldatei | Seiten | Größe | Status |
|---:|---|---|---:|---:|---|
| 1 | Hauptdokument | `01_K_Klage_Mietrueckstand.pdf` | 8 | [Bytes] | bereit |
| 2 | Anlage K 1 | `02_Anlage_K01_Mietvertrag_2022-05-01.pdf` | 12 | [Bytes] | bereit |

Die technische Nachweisspur wird getrennt geführt:

| Nr. | Quelldatei | Original-Hash | PDF-Hash | OCR | Kennzeichnung | Datenschutz |
|---:|---|---|---|---|---|---|
| 1 | [Quelle] | [Hash] | [Hash] | ja | entfällt | geprüft |
| 2 | [Quelle] | [Hash] | [Hash] | ja | erste Seite | geprüft |

Das Manifest ist intern. Es wird nicht automatisch als weitere Anlage eingereicht.

## 9. Versand-Preflight

Vor Übergabe an den tatsächlichen Versender müssen alle Fragen beantwortet sein:

1. Sind Datum, aktiver beA-/eBO-/Kanzleisoftwarestand, verwendetes XJustiz-Profil und Ergebnis der clientseitigen Dateinamens- und Anhangsprüfung protokolliert? Eine Warnung bleibt gelb oder rot, bis eine reale Person sie nachvollziehbar geklärt hat.
2. Ist das richtige Gericht ausgewählt und betrifft die Nachricht genau ein Verfahren?
3. Stimmen Aktenzeichen oder `Neueingang`, Parteirollen und Betreff?
4. Stimmen Antrag, Betrag, Zins, Streitwert und Anlagenzitate mit der letzten Freigabe überein?
5. Öffnen sich Hauptdokument und jede Anlage, und ist jede Seite lesbar?
6. Stimmen Reihenfolge, sichtbare K-/B-Nummer, Dateiname und Anlagenverzeichnis?
7. Bleiben Dateizahl und Gesamtvolumen unter 1.000 Dateien und 200 MB?
8. Ist der Einreichungsweg eindeutig als beA, eBO oder zulässige schriftliche Eigenübermittlung festgelegt? Beim beA müssen verantwortende Person und beA-Versender bei einfacher Signatur identisch sein; beim eBO müssen Postfachinhaber, verantwortende Person, Signatur, Versandberechtigung und Vertretungsbefugnis belegt sein.
9. Ist eine reale Freigabeperson benannt, und ist genau diese Paketversion freigegeben?
10. Sind Zustellungs-/Einreichungsfrist, Vorfrist und Störungsweg dokumentiert?
11. Für den Störungsfall: Sind Beginn, konkretes Fehlerbild, betroffene Komponenten, angezeigte Meldung, technische Ursache soweit feststellbar, Abhilfemaßnahmen, letzter erfolgreicher Versand und Belege so vorbereitet, dass eine geschlossene Glaubhaftmachung grundsätzlich zusammen mit der Ersatzeinreichung möglich ist?

## 10. Eingangsnachweis

Nach der Übermittlung werden gespeichert:

- gesendete Nachricht mit Empfänger, Aktenzeichen und Zeitstempel,
- vollständige Dateiliste und Gesamtgröße,
- Prüf- und Signaturprotokoll,
- automatisierte Eingangsbestätigung,
- Hashmanifest der tatsächlich gesendeten Dateien,
- Aktenvermerk zu Fristwahrung, Gerichtskostenvorschuss, Zustellung und Wiedervorlage.

Die bloße Anzeige „gesendet“ ersetzt die Prüfung der gerichtlichen Eingangsbestätigung nicht.

## 11. Rechtsprechungsanker zum ERV

| Entscheidung | Arbeitsregel | Amtliche Quelle |
|---|---|---|
| BGH, Beschluss vom 02.12.2025 - VIII ZB 17/25 | Die technische Unmöglichkeit und ihre nur vorübergehende Natur sind in einer aus sich heraus verständlichen, geschlossenen Tatsachenschilderung glaubhaft zu machen. Eine pauschale Angabe wie `Störung wohl am Router` genügt nicht. Fehlerbild, Beginn und laienverständlich beschriebene Abhilfemaßnahmen müssen Bedienungs- oder Personenfehler unwahrscheinlich machen. Die Glaubhaftmachung erfolgt grundsätzlich mit der Ersatzeinreichung; eine Nachholung ist nur in der eng begrenzten Ausnahme unverzüglich zulässig. | [BGH-Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2025/VIII_ZB__17-25.pdf?__blob=publicationFile&v=1) |
| BGH, Urteil vom 11.10.2024 - V ZR 261/23 | Ein nicht qualifiziert signierter Schriftsatz ist über beA nur formgerecht, wenn die verantwortende Person einfach signiert und selbst versendet; fehlende einfache Signatur kann die Fristwahrung zerstören. | [BGH-Volltext](https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024-10&Gericht=bgh&Seite=1&Sort=12&anz=221&pos=33) |
| BGH, Beschluss vom 07.05.2024 - VI ZB 22/23 | Bei einfacher Signatur müssen Verantwortungsübernahme und tatsächlicher beA-Versand personell zusammenpassen. | [BGH-Volltext](https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024&Gericht=bgh&Seite=17&Sort=2062&anz=2887&pos=528) |
| BGH, Beschluss vom 28.02.2024 - IX ZB 30/23 | Eine qualifizierte elektronische Signatur kann eine andere Verantwortungs- und Versandkonstellation tragen; die gewählte Variante muss eindeutig dokumentiert sein. | [BGH-Volltext](https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024-2&Gericht=bgh&anz=275&nr=86164&pos=21) |
| BVerfG, Beschluss vom 16.02.2023 - 1 BvR 1881/21 | Ein technisch eingegangener Schriftsatz durfte im damaligen Fall nicht wegen eines von der Gerichtssoftware nicht verarbeiteten überlangen Anlagennamens ignoriert werden. Die Entscheidung betraf ältere Technikvorgaben und ist kein Freibrief, die aktuelle 90-Zeichen-Regel zu missachten. | [BVerfG-Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2023/02/rk20230216_1bvr188121.html) |

## 12. Rote Stopps

- Freigabe fehlt oder bezieht sich auf eine andere Version.
- Frist oder Gericht ist ungeklärt.
- Antrag, Betrag oder Partei widerspricht der Anlagen-/Aktenlage.
- Anlage fehlt, ist leer, unlesbar oder anders nummeriert als im Schriftsatz.
- Original wurde überschrieben oder Herkunft/Version ist nicht mehr nachvollziehbar.
- beA-Fall: Einfache Signatur und tatsächlicher beA-Versender sind nicht dieselbe verantwortende Person.
- eBO-Fall: Postfachinhaber, verantwortende Person, Versandberechtigung, Vertretungsbefugnis oder Signaturmodell sind ungeklärt.
- Die private Gesellschaft wird ohne Normprüfung fälschlich als nach Paragraf 130d ZPO aktiv nutzungspflichtig behandelt oder ein anwaltlicher Pflichtfall wird als freiwillige Eigenübermittlung ausgegeben.
- Paket enthält ZIP, Passwortschutz, ausführbaren Inhalt oder unzulässige Dateinamen.
- Gesamtpaket überschreitet die aktuelle technische Grenze.
- Bei geplanter Ersatzeinreichung fehlen geschlossene Störungsschilderung, Belege oder unverzügliche Glaubhaftmachung.
- Automatisierte Eingangsbestätigung fehlt oder weist eine Abweichung aus.

Bei rotem Stopp: keine Scheinsicherheit, keine improvisierte Übermittlung. Fehlerkarte, Frist, zuständige Person und anwaltlich zu entscheidenden Korrekturweg ausgeben.
