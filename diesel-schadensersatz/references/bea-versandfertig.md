# beA-versandfertige Schriftsatz- und Anlagenpakete

Stand: 09.08.2026. Diese Referenz beschreibt die Vorbereitung eines Versandpakets. Die tatsächliche Signatur, Adressierung, Übermittlung und Eingangskontrolle bleiben anwaltliche Handlungen im beA-/Kanzleisystem.

## 1. Normebenen strikt trennen

| Ebene | Inhalt | Verbindlichkeit |
| --- | --- | --- |
| § 130a ZPO | Form elektronischer Dokumente, qualifizierte elektronische Signatur oder einfache Signatur plus sicherer Übermittlungsweg | gesetzlich |
| § 130d ZPO | aktive elektronische Nutzungspflicht; Ersatzeinreichung nur bei vorübergehender technischer Unmöglichkeit mit Glaubhaftmachung | gesetzlich |
| §§ 2, 5 ERVV und ERVB 2025 | PDF/TIFF, technische Standards, XJustiz, Anzahl/Volumen, Datenträger und Signaturformate | Verordnung/Bekanntmachung |
| NRW-Namenskonvention | sprechende Namen, Rollenpräfixe und logische Anlagenfolge | amtliche Empfehlung, keine bundesweite Namensnorm |
| ASCII-/Unterstrich-Hausstandard dieses Plugins | kurze, portable Dateinamen ohne Leerzeichen und Umlaute | interner strengerer Standard |

Der interne ASCII-Standard darf nicht als Gesetz ausgegeben werden. Die ERVB erlaubt auch Buchstaben des deutschen Alphabets einschließlich Umlaute und `ß`; Punkte sind grundsätzlich nur zur Trennung der Dateiendung vorgesehen.

## 2. Aktuelle technische Leitplanken

Nach der ERVB 2025 gilt für die hier vorbereiteten Zivilsachen insbesondere:

- Schriftsatz und Anlagen grundsätzlich als einzelne PDF-Dateien; TIFF darf bei nicht verlustfrei in PDF darstellbaren Abbildungen zusätzlich übermittelt werden.
- PDF einschließlich PDF 2.0, PDF/A-1, PDF/A-2 und PDF/UA ist vorgesehen.
- Keine eingebetteten Objekte und keine ausführbaren Anweisungen, insbesondere kein JavaScript. Formularfelder ohne JavaScript und Hyperlinks sind zulässig.
- Höchstens 1.000 Dateien und höchstens 200 MB je Nachricht.
- Dateiname höchstens 90 Zeichen einschließlich Endung.
- Bei außergewöhnlich umfangreichen Einreichungen sind nach der ERVB 2025 auch DVD, CD oder USB-Speicher mit USB 2.0 oder höher und exFAT/NTFS vorgesehen; Verfahren und Glaubhaftmachung sind vor Fristablauf anwaltlich live zu prüfen.

Quellen:

- [§ 130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html)
- [§ 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html)
- [§ 2 ERVV](https://www.gesetze-im-internet.de/ervv/__2.html)
- [§ 5 ERVV](https://www.gesetze-im-internet.de/ervv/__5.html)
- [ERVB 2025, BAnz AT 29.07.2025 B2](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf)
- [Leitfaden zum elektronischen Rechtsverkehr](https://justiz.de/ervvoe/leitfaden_erv_pdf.pdf)
- [XJustiz-Downloads und jeweils gültige Version](https://xjustiz.justiz.de/downloads/index.php)
- [BRAK zur Einreichung großvolumiger Dokumente](https://www.brak.de/newsroom/news/grossvolumige-dokumente-jetzt-auch-auf-usb-stick-einreichbar/)

## 3. Signatur und verantwortende Person

Es gibt zwei Grundwege:

1. qualifizierte elektronische Signatur der verantwortenden Person; oder
2. einfache elektronische Signatur im Dokument und persönliche Übermittlung durch dieselbe verantwortende Person auf einem sicheren Übermittlungsweg.

Die einfache Signatur ist regelmäßig die Wiedergabe des Namens am Ende des Schriftsatzes. Briefkopf, Dateiname oder beA-Absender ersetzen sie nicht. Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Absender des persönlichen beA übereinstimmen. Abweichende Verfasser-, Signatur- und Versandkonstellationen benötigen eine bewusste Prüfung; eine qualifizierte Signatur kann andere Verantwortungszuordnungen ermöglichen.

Amtliche BGH-Anker:

- [BGH, Beschl. v. 07.09.2022 - XII ZB 215/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2022/XII_ZB_215-22.pdf?__blob=publicationFile&v=1): Name am Textende als einfache Signatur.
- [BGH, Beschl. v. 28.02.2024 - IX ZB 30/23](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2023/IX_ZB__30-23.pdf?__blob=publicationFile&v=1): Verantwortung bei qualifizierter Signatur eines anderen Sozietätsmitglieds.
- [BGH, Beschl. v. 07.05.2024 - VI ZB 22/23](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VI_ZS/2023/VI_ZB__22-23.pdf?__blob=publicationFile&v=1): einfache Signatur und beA-Absender dürfen nicht auseinanderfallen.
- [BGH, Urt. v. 14.07.2026 - VIa ZR 946/22, Rn. 3 f.](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIa_ZS/2022/VIa_ZR_946-22.pdf?__blob=publicationFile&v=1): Der regelmäßig erscheinende Prüfberichtshinweis, dass keine Sperrabfrage beim Trustcenter durchgeführt wurde, verlangte ohne konkretes Sperrindiz keine weitere Aufklärung. Die Entscheidung ist keine pauschale Entwarnung für andere Warnungen oder fehlgeschlagene Prüfungen; Signaturdatei, Prüfbericht und Eingangsbestätigung bleiben vollständig zu sichern.
- [BGH, Beschl. v. 09.04.2025 - XII ZB 599/23](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2023/XII_ZB_599-23.pdf?__blob=publicationFile&v=1): einfacher Signaturbedarf auch bei sicherem Übermittlungsweg.

## 4. Eingangskontrolle

Ein lokaler Export, ein beA-Prüfprotokoll oder ein Signaturprüfbericht beweist nicht für sich den Eingang des beabsichtigten Schriftsatzes beim Gericht. Nach dem Versand sind die automatisierte gerichtliche Eingangsbestätigung, Status, Zeitpunkt, Empfänger und die dort aufgeführten Dateinamen zu kontrollieren und zur Akte zu speichern.

Amtliche BGH-Anker:

- [BGH, Beschl. v. 20.09.2022 - XI ZB 14/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XI_ZS/2022/XI_ZB__14-22.pdf?__blob=publicationFile&v=1): Eingangsbestätigung muss sich auf das beabsichtigte Dokument beziehen.
- [BGH, Beschl. v. 30.03.2023 - III ZB 13/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2022/III_ZB__13-22.pdf?__blob=publicationFile&v=1): automatisierte Eingangsbestätigung kontrollieren und sichern.
- [BGH, Beschl. v. 21.03.2023 - VIII ZB 80/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2022/VIII_ZB__80-22.pdf?__blob=publicationFile&v=1): anhand des Dateinamens prüfen, ob die richtige Datei bestätigt wurde.
- [BGH, Beschl. v. 19.12.2024 - IX ZB 41/23](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2023/IX_ZB__41-23.pdf?__blob=publicationFile&v=1): amtliche Störungsinformation kann Teil der Glaubhaftmachung einer technischen Störung sein.

## 5. Dateinamen für Gericht und Kanzlei

Die [NRW-Namensempfehlung](https://www.justiz.nrw.de/sites/default/files/imported/files/2022-11/Namenskonvention-fuer-Externe-Nutzer.pdf) schlägt sprechende Dateinamen, Rollenpräfixe am Hauptdokument und eine logische Anlagenfolge vor. Die [NRW-ERV-Hinweise](https://www.justiz.nrw.de/Gerichte_Behoerden/anschriften/elektronischer_rechtsverkehr/ERV_Hinweise) warnen vor nichtssagenden Namen wie `Dok1.pdf` und verlangen ein bekanntes Aktenzeichen in den Metadaten; bei Neueingängen wird der Vorgang als solcher gekennzeichnet.

Plugin-Hausstandard:

```text
00_K_2026-07-10_Replik_16_O_123_24.pdf
01_Anlage_K12_Kaufvertrag_2020-05-14.pdf
02_Anlage_K13_Zulassungsbescheinigung_Teil_I.pdf
03_Anlage_K14_KBA_Rueckrufschreiben_2021-08-03.pdf
```

Regeln:

- Nur ASCII, Ziffern, Unterstrich und Minus; genau ein Punkt vor `.pdf`.
- Zielwert höchstens 80 Zeichen, absolute ERVB-Grenze 90 Zeichen einschließlich `.pdf`.
- Sortiernummer mindestens zweistellig auffüllen (`01` bis `99`); ab `100` ohne Abschneiden entsprechend breiter fortführen.
- Hauptdokument genau einmal mit Rollenpräfix, Dokumentart, Datum und bereinigtem Aktenzeichen.
- Anlagenbezeichnung im Dateinamen muss dem Stempel und der Bezugnahme im Schriftsatz entsprechen.
- Bei Replik oder weiterem Schriftsatz bestehende Nummerierung fortsetzen; bereits eingereichte Anlagen nie still umnummerieren.
- `K` regelmäßig für Klägerseite, `B` regelmäßig für Beklagtenseite. Abweichende Gerichts- oder Kanzleikonventionen vor Produktion abfragen.

## 6. Anlagenstempel und Beweisintegrität

Der Stempel `Anlage K1`, `Anlage K2` usw. wird rechts oben auf einer **Versandkopie** angebracht. Das Original bleibt unverändert und erhält einen SHA-256-Wert. Vor und nach Konvertierung werden Seitenzahl, Lesbarkeit, Orientierung und Vollständigkeit verglichen.

Stopps:

- Der Stempel verdeckt Text, Stempel, Unterschrift, QR-Code oder Bildinhalt.
- Die Quelldatei ist digital signiert oder ihr Beweiswert hängt von einer Signatur ab.
- Konvertierung ändert Seiten, Farben, Maßstab oder lesbaren Inhalt.
- OCR erzeugt sichtbare Textfehler oder ersetzt statt ergänzt das Seitenbild.

Bei Platzkonflikt wird nach anwaltlicher Freigabe ein Anlagen-Deckblatt mit Bezeichnung rechts oben verwendet. Digital signierte Originale werden nicht überschrieben oder unbemerkt neu serialisiert.

Produktionsdatei und Auditprotokoll müssen verschiedene Pfade haben. Stempelwerkzeug, Paketbauer und Paketprüfer folgen keinen symbolischen Links; sie sperren PDFs mit mehr als 5.000 Seiten oder Seitenachsen über 14.400 Punkten als internen Ressourcen- und Renderingschutz. Der Stempelpfad liest und hasht bis zur 200-MB-Grenze race-sicher, parst Ein- und Ausgabe strikt und veröffentlicht die Ausgabe erst danach atomar. Vorhandene Ausgabe- oder Auditdateien bleiben ohne bewusst gesetztes `--force` unverändert. Ändert sich das Original während der Verarbeitung, wird die Ausgabe verworfen.

## 7. Paketstruktur und Freigabegates

```text
bea-paket/
├── original/      unveränderte Eingänge, nicht versenden
├── arbeit/        OCR-, Konvertierungs- und Stempelkopien
├── versand/       nur die tatsächlich auszuwählenden PDF-Dateien
└── kontrolle/     Anlagenverzeichnis, Hashes, Prüfbericht, Freigabe
```

Der maschinenlesbare Paketauftrag bindet bereits vor der Produktion Gericht/Aktenzeichen, Rolle, Dokumentart, Frist, verantwortende Person, Signaturweg, Anlagenfolge, jede Schriftsatzfundstelle sowie den erwarteten SHA-256-Wert von Hauptdokument und Anlagen. Der Paketbauer erzeugt daraus ein Manifest mit Produktionszeitpunkt, tatsächlichen Versanddateinamen, Größen, Seitenzahlen und Hashes. Der daraus kanonisch berechnete Paket-Fingerprint bindet auch `created_at` und ändert sich, sobald Produktionszeit, Auftrag, Bezugnahme, Dateiinhalt, Dateiname oder Reihenfolge geändert werden. Produktions- und Freigabezeitpunkt müssen sekunden-genaue ISO-Zeitpunkte mit Zeitzone sein; ein Zeitpunkt mehr als fünf Minuten in der Zukunft sperrt das Paket.

Stabile Hashprüfung folgt keinen symbolischen Links und liest reine Originalspuren ohne unnötige Vollkopie in den Arbeitsspeicher. Gleiches Dateiobjekt unter mehreren Namen (Hardlink), normalisierte/portable Namenskollisionen, Unicode-Steuer- oder Formatzeichen, widersprüchliche Seitenzahlen und interne Manifestabweichungen sind harte Fehler. Hauptdokument plus Anlagen dürfen zusammen bereits als Quellen die 200-MB-Nachrichtengrenze nicht überschreiten.

Nach erfolgreicher technischer Produktion gilt der Zwischenstatus `FREIGABE_AUSSTEHEND`. Eine strukturierte `freigabe.json` muss genau diesen Paket-Fingerprint nennen und die tatsächlich erfolgte anwaltliche Inhalts-, Zuordnungs- und visuelle PDF-Prüfung bestätigen. Dieser Datensatz ist ein interner Kontrollnachweis; er ersetzt weder die einfache/qES-Signatur noch den persönlichen Versand oder die gerichtliche Eingangsbestätigung.

`VERSANDFERTIG` darf nur ausgegeben werden, wenn:

1. Gericht, Aktenzeichen/Neueingang, Parteirolle, Schriftsatzart, Frist und verantwortende Person bestätigt sind;
2. genau ein Hauptdokument vorliegt und dessen Endfassung anwaltlich freigegeben ist;
3. jede Anlagenbezugnahme im Schriftsatz genau einer Datei entspricht und umgekehrt;
4. Nummerierung, Stempel, Dateiname und Anlagenverzeichnis deckungsgleich sind;
5. PDF-Lesbarkeit, Seitenfolge, Orientierung, Dateigrenzen und technische Ausschlussmerkmale geprüft sind;
6. Signatur-/Versandweg festgelegt, aber noch nicht fälschlich als ausgeführt dokumentiert ist;
7. der Prüfer null Fehler und null Warnungen meldet.

Der technische Prüfer unterscheidet deshalb:

- `NICHT_VERSANDFERTIG` bei Fehlern, Warnungen, fehlendem/abweichendem Manifest oder ungültiger Freigabe;
- `FREIGABE_AUSSTEHEND` bei technisch und semantisch fehlerfreiem Paket ohne gebundene Freigabe;
- `VERSANDFERTIG` ausschließlich bei fehlerfreiem Paket und gültiger Freigabe zum aktuellen Fingerprint.

Nach der Paketfreigabe übernimmt Skill 16 die tatsächliche Adressierung, Signatur, Übermittlung, gerichtliche Eingangsbestätigung, Vorschuss- und Zustellungskontrolle.
