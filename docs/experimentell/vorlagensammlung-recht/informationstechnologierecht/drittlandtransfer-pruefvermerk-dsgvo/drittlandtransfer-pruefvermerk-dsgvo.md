# Prüfvermerk Drittlandtransfer nach DSGVO

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Aktenbestandteil für externe Herausgabe]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Datenflüsse, die Dienstleisterauskünfte und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den Transfer technisch und rechtlich nachzuvollziehen, hat noch kein verwendbares Dokument, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Rubrum, interne Prüfstelle und Dokument

### PRÜFVERMERK DRITTLANDTRANSFER NACH DSGVO

Bearbeitungsstand: [Entwurf / Datenschutzfreigabe / Geschäftsleitungsfreigabe / Nachprüfung].

Aktenzeichen Datenschutz: [internes Datenschutz-Aktenzeichen].

Verantwortliche Stelle: [Name, Rechtsform, Anschrift].

Datenschutzkontakt: [Datenschutzbeauftragter oder Datenschutzkoordination, E-Mail, Telefon].

Geprüfter Transfer: [System, Dienstleister, Schnittstelle, Datenempfänger, Zielland].

#### 1. Prüfgegenstand und Datenfluss

1.1 Geprüft wird der Transfer personenbezogener Daten aus [EU-Mitgliedstaat / EWR-Staat] an [Empfängername, Rechtsform, Anschrift, Zielland] im Zusammenhang mit [konkreter Verarbeitungszweck, etwa Cloud-Hosting, Supportzugriff, konzerninterne HR-Auswertung, Zahlungsabwicklung, Kollaborationstool].

1.2 Der Transfer besteht aus [Variante A: aktiver Übermittlung durch Export, API, Dateiablage oder Schnittstelle; Variante B: Zugriffsmöglichkeit aus dem Drittland durch Support, Administration oder Fernwartung; Variante C: Speicherung oder Backup in Rechenzentren außerhalb des EWR; Variante D: Weiterübermittlung durch Unterauftragsverarbeiter].

1.3 Betroffen sind [Kategorien betroffener Personen, etwa Beschäftigte, Kunden, Interessenten, Nutzer, Lieferantenkontakte] und folgende Datenkategorien: [Stammdaten; Kontaktdaten; Vertragsdaten; Nutzungsdaten; Inhaltsdaten; Kommunikationsdaten; besondere Kategorien nach Art. 9 DSGVO; Strafdaten nach Art. 10 DSGVO].

1.4 Die Verarbeitung im Ausgangspunkt stützt sich auf [Art. 6 Abs. 1 lit. b DSGVO Vertragserfüllung / Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse / Art. 6 Abs. 1 lit. c DSGVO rechtliche Pflicht / Art. 6 Abs. 1 lit. a DSGVO Einwilligung]. Besondere Kategorien personenbezogener Daten werden nur verarbeitet, soweit [Ausnahme nach Art. 9 Abs. 2 DSGVO] greift.

#### 2. Rollen, Empfänger und Unterauftragskette

2.1 [Empfängername] handelt für diesen Transfer als [Auftragsverarbeiter / weiterer Auftragsverarbeiter / eigenständig Verantwortlicher / gemeinsam Verantwortlicher].

2.2 Die Rollenbewertung folgt aus [Vertrag, Leistungsbeschreibung, Weisungsrechten, tatsächlicher Entscheidung über Zwecke und wesentliche Mittel]. Abweichende Bezeichnungen im Vertrag sind für diesen Vermerk nicht maßgeblich, soweit die tatsächliche Rollenverteilung anders liegt.

2.3 Unterauftragsverarbeiter oder weitere Empfänger mit Drittlandbezug sind [Name, Rolle, Land, Leistung, Zugriffstyp, DPF-Status oder SCC-Modul]. Nicht freigegeben sind Weiterübermittlungen an [ausgeschlossene Länder, Dienste oder Unterauftragnehmer].

#### 3. Kapitel-V-Instrument

3.1 Für den Transfer wird folgendes Instrument nach Kapitel V DSGVO gewählt: [Angemessenheitsbeschluss nach Art. 45 DSGVO / EU-Standardvertragsklauseln nach Art. 46 Abs. 2 lit. c DSGVO / Binding Corporate Rules nach Art. 47 DSGVO / genehmigte Vertragsklauseln / Art.-49-Ausnahme].

3.2 Bei Transfer in die USA lautet das Ergebnis: [Variante A: Empfänger ist aktiv im EU-US Data Privacy Framework gelistet und die konkrete Datenverarbeitung fällt unter den Zertifizierungsumfang; Variante B: Empfänger ist nicht oder nicht passend gelistet, deshalb wird der Transfer nicht auf DPF gestützt; Variante C: DPF wird nur für einen Teil der Empfängerkette genutzt, für den übrigen Teil gelten SCC und TIA].

3.3 Bei Transfer in ein anderes Drittland lautet das Ergebnis: [Angemessenheitsbeschluss vorhanden und einschlägig / kein Angemessenheitsbeschluss, SCC und TIA erforderlich / Ausnahme nach Art. 49 DSGVO nur für den dokumentierten Einzelfall].

#### 4. Wirksamkeitsprüfung und ergänzende Maßnahmen

4.1 Soweit der Transfer nicht vollständig von einem einschlägigen Angemessenheitsbeschluss gedeckt ist, wird ein Transfer Impact Assessment nach der gesonderten Vorlage [Aktenzeichen oder Dokumentenname] geführt.

4.2 Technische Maßnahmen sind [Ende-zu-Ende-Verschlüsselung mit Schlüsselhoheit im EWR / Pseudonymisierung vor Transfer / Mandantentrennung / Zugriff nur über privilegierte Bastion-Hosts / Protokollierung und Vier-Augen-Freigabe / keine wirksame technische Zusatzmaßnahme möglich].

4.3 Vertragliche Maßnahmen sind [SCC-Modul Nummer / Transparenzpflicht bei Behördenzugriffen / Warrant Canary, soweit rechtlich zulässig / Pflicht zur Anfechtung unverhältnismäßiger Herausgabeverlangen / Weiterübermittlungsverbot ohne Freigabe / Audit- und Nachweispflichten].

4.4 Organisatorische Maßnahmen sind [Drittlandtransfer-Register / jährliche DPF-Listenprüfung / halbjährliche Unterauftragsprüfung / Lösch- und Exit-Test / Schulung von Administratoren / Notfallprozess bei Verlust des Transferinstruments].

#### 5. Betroffeneninformation und Verzeichnis

5.1 Die Information nach Art. 13 Abs. 1 lit. f oder Art. 14 Abs. 1 lit. f DSGVO wird angepasst in [Datenschutzhinweis, Vertragsanlage, Bewerberinformation, Beschäftigteninformation, Website-Datenschutzerklärung].

5.2 Das Verzeichnis der Verarbeitungstätigkeiten wird ergänzt um [Transferzweck, Empfänger, Drittland, Transferinstrument, Löschfrist, Schutzmaßnahmen, Verantwortlicher für Nachprüfung].

5.3 Eine Datenschutz-Folgenabschätzung ist [nicht erforderlich, Begründung / erforderlich und wird unter Aktenzeichen geführt / bereits vorhanden und wird um den Drittlandtransfer ergänzt].

#### 6. Freigabeentscheidung

6.1 Der Transfer wird freigegeben unter folgenden Auflagen: [DPF-Listung vor Produktivstart erneut prüfen; SCC-Anlagen vor Unterzeichnung vervollständigen; TIA final freigeben; Schlüsselverwaltung im EWR nachweisen; Betroffeneninformation veröffentlichen; Unterauftragsliste sperren; Export vorläufig deaktivieren].

6.2 Ohne Erfüllung der Auflagen nach 6.1 darf [System, Dienst, Schnittstelle] keine personenbezogenen Daten an [Empfänger oder Zielland] übertragen oder zugänglich machen.

6.3 Nachprüfung: [Datum, Verantwortlicher, Ereignis, etwa jährliche Kontrolle, Zertifizierungsablauf, Änderung des Ziellandrechts, neuer Unterauftragnehmer, Produktänderung].

#### 7. Anlagen

7.1 Anlage 1: Datenflussdiagramm und Systembeschreibung.

7.2 Anlage 2: Vertrag, AVV oder Joint-Controller-Vereinbarung.

7.3 Anlage 3: DPF-Listennachweis oder Angemessenheitsnachweis.

7.4 Anlage 4: SCC-Begleitvereinbarung und Transfer Impact Assessment.

7.5 Anlage 5: Betroffeneninformation, Verzeichnis der Verarbeitungstätigkeiten und Freigabevermerk.

#### 8. Freigabe

[Ort], den [Datum]

| Datenschutz | Fachbereich | Geschäftsleitung |
|---|---|---|
| _____________________________ | _____________________________ | _____________________________ |
| [Name, Funktion] | [Name, Funktion] | [Name, Funktion] |

### Anlage 6 — Prüf- und Bewertungsschema

1. Zweck und Prüfstand

1.1 Dieses Schema führt die Freigabeentscheidung des Vermerks als Stufenprüfung, deren Stufen den Abschnitten 1 bis 6 zugeordnet sind; jede Stufe erhält einen eigenen Befund mit Tatsachengrundlage.

1.2 Transfer: [System, Empfänger, Zielland]; Prüfdatum: [JJJJ-MM-TT]; prüfende Person: [Name, Funktion].

2. Stufe 1 — Datenfluss und Rechtsgrundlage (Abschnitt 1)

2.1 Alle Transferpfade der Varianten A bis D sind erhoben und im Datenflussdiagramm der Anlage 1 abgebildet; nicht erfasste Pfade: [keine / Beschreibung].

2.2 Die Rechtsgrundlage der Ausgangsverarbeitung nach Ziffer 1.4 trägt den konkreten Exportumfang; Befund: [tragfähig / nur nach Reduktion tragfähig / nicht tragfähig — Prüfung endet].

3. Stufe 2 — Rollen und Kette (Abschnitt 2)

3.1 Die Rolle des Empfängers ist anhand der tatsächlichen Zweck- und Mittelentscheidung geprüft, nicht anhand der Vertragsbezeichnung; Befund: [bestätigt / abweichend mit Folgeänderung].

3.2 Die Unterauftragskette ist vollständig erfasst und gegen die veröffentlichte Liste des Dienstleisters abgeglichen am [Datum]; Befund: [vollständig / Lücken mit Nachforderung].

4. Stufe 3 — Transferinstrument (Abschnitt 3)

4.1 Das gewählte Instrument ist mit Nachweis belegt: [Fundstelle des Angemessenheitsbeschlusses mit Abrufdatum / DPF-Listenprüfung mit Datum und Zertifizierungsumfang / unterzeichnete SCC mit Modul und Datum / BCR-Beitrittsnachweis / Art.-49-Einzelfalldokumentation].

4.2 Befund Stufe 3: [Instrument trägt den gesamten Transfer / Instrument trägt nur Teilstrecken — Ersatzinstrument je Teilstrecke benannt / kein tragfähiges Instrument — keine Freigabe].

5. Stufe 4 — Ziellandrecht und ergänzende Maßnahmen (Abschnitt 4)

5.1 Das Transfer Impact Assessment nach Ziffer 4.1 liegt vor mit Stand [Datum]; die dort festgestellten Zugriffsszenarien sind durch die Maßnahmen der Ziffern 4.2 bis 4.4 abgedeckt (Suchanker für die Live-Recherche: EuGH Schrems II ergänzende Maßnahmen).

5.2 Befund Stufe 4: [Schutzniveau hergestellt / hergestellt mit Auflagen / nicht herstellbar — keine Freigabe].

6. Stufe 5 — Dokumentation, Auflagen und Nachprüfung (Abschnitte 5 und 6)

6.1 Betroffeneninformation, Verzeichnis der Verarbeitungstätigkeiten und Transferregister sind angepasst; Ablageorte: [Fundstellen].

6.2 Jede Auflage aus Ziffer 6.1 hat Verantwortlichen, Frist und Nachweisform, und die Sperrfolge der Ziffer 6.2 ist technisch oder organisatorisch umgesetzt: [Beschreibung].

6.3 Gesamtergebnis der Stufenprüfung: [Freigabe / Freigabe unter Auflagen / keine Freigabe]; Wiedervorlage: [Datum]; Vermerk: [Ort, Datum, Name, Funktion].

---

Lizenz: Apache-2.0 OR MIT.
