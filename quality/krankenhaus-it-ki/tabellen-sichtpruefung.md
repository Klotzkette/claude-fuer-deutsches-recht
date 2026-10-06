# 1. Sichtprüfung der Krankenhaus-Arbeitsmappen

Prüfstand: 6. Oktober 2026, erster Durchgang am Exportstand 21:05 Uhr. Unabhängige Sichtprüfung sämtlicher 14 PDF-Seiten aus vier nativen Arbeitsmappen. Die 14 vorhandenen PNGs wurden einzeln betrachtet, nicht lediglich als Kontaktbogen. Die Originale wurden nicht verändert. Verwendet wurde der PDF-Skill für eine reine Leseprüfung.

## 1.1. Ergebnis des ersten Durchgangs

Alle Inhalte waren sichtbar; keine abgeschnittenen Zeilen, fehlenden Blätter, defekten Glyphen oder Warnungsseiten gefunden. Wiederholte Tabellenköpfe, Eingabefarben, Quellenhinweise und die Abgrenzung zwischen Planung und tatsächlicher Freigabe sind vorhanden. Die leeren Messfelder werden nicht als Nullfehler dargestellt.

Vor finaler Abnahme wurden folgende Layoutkorrekturen an den Ersteller gemeldet:

1. In Mappe 37 berühren Texte benachbarter Spalten einander, insbesondere „Health Europe“ und „Cloud Frankfurt“ im Datenflussblatt sowie Ziel und nächste Entscheidung im Vorhabenblatt. Spalten brauchen sichtbare Abgrenzung und ausreichenden Abstand.
2. In Mappe 38 erscheinen Datum und Prüfstatus ohne optischen Zwischenraum, beispielsweise „09.10.2026Nein“. Datumszellen und angrenzende Statuszellen benötigen eine klar erkennbare Trennung.
3. In Mappe 39 berühren im Transferinventar der Nachweistext und die Zusatzmaßnahme einander. Die Spaltentrennung ist anzupassen.
4. In Mappe 40 stoßen Menge und Einheit sowie Betrag und Quelle optisch zusammen. Zusätzlich erscheinen Geldbeträge noch in US-Schreibweise, etwa „5,340.00“. Für die deutsche Akte ist das deutsche Zahlenformat einzustellen.

Der Ersteller führt die Nacharbeit aus. Bis zur erneuten Sichtprüfung besteht keine endgültige Layoutabnahme.

## 1.2. Inhaltliche Feststellungen

Die vier Mappen trennen Vorhaben, Datenflüsse, Nachweise, Aufgaben und geplante Messungen. Ein beantworteter Lieferantenpunkt wird nicht mehr als Freigabe bezeichnet. Eine erledigte Maßnahmenliste erzeugt ausdrücklich keine Betriebsfreigabe. C5-Typ1 wird nicht pauschal zurückgewiesen; tatsächliches Erstinverkehrbringen, Systemumfang und Kundenkriterien bleiben zu prüfen. Drittlandzugriff wird von EU-Speicherung sowie einer bloßen Anbieterbehauptung unterschieden. Die Hochschulübermittlung wird auch unabhängig vom Drittlandrecht betrachtet.

Das Budget ergibt im Ausgangsstand 5.340,00 EUR Lizenzkosten, 4.800,00 EUR Einrichtung, 10.140,00 EUR externe Nettokosten, 1.926,60 EUR Umsatzsteuer, 12.066,60 EUR externes Zahlungsbudget und 3.120,00 EUR interne Vollkosten; Gesamtressourcenbedarf 15.186,60 EUR. Vorsteuerabzug wird nicht unterstellt. Acht Wochen zu je 20 geplanten Briefen ergeben 160 geplante Briefe; echte Messwerte fehlen am Aktenstichtag.

Der Ersteller meldet sieben bestandene native Ausgangsprüfungen und elf Mutationstests. Diese Sichtprüfung ersetzt jene Formelprüfung nicht. Der unabhängige Abgleich mit den 36 weiteren Aktenoriginalen steht noch aus, weil diese zum ersten Prüfdurchgang noch nicht vollständig im Fallordner lagen.

## 1.3. Hashes des zuerst geprüften Stands

Die folgenden SHA-256-Werte dokumentieren den ersten Durchgang und werden durch den späteren finalen Stand nicht rückwirkend als abgenommen erklärt.

| Datei | SHA-256 |
| --- | --- |
| 37_Vorhaben_Datenfluesse.xlsx | `c15b8b35b66de9333971a45a55c75600d415828e07d917e72855232f5ad9d23e` |
| 38_Massnahmen_Freigaben.xlsx | `34bcaf688cbe333d199f374c4dc62a8f29efc36836b07b1af282e08a5d31d8b4` |
| 39_Lieferanten_Transfernachweise.xlsx | `43ca122ee1dda33df9153fb5857b2a8ca2e1117b745e70cfe7598ed9af6b1306` |
| 40_Pilotmessung_Kosten.xlsx | `cb7a977ad33be51ab203eb1c36fd1c6d6b405d4cb462005469b2caf737a298fa` |
| 37_Vorhaben_Datenfluesse.pdf | `4eb137ff36a770543e3b6579eb847be2b3889b91a9031e08ccbf3245c653a359` |
| 38_Massnahmen_Freigaben.pdf | `e915999361409ec44daa63ac29e67179ed78b6459c5911f370b003db90c5bcee` |
| 39_Lieferanten_Transfernachweise.pdf | `945f3558434a21b19b7bc42eb7603026058a1d29ac73a8a7febdd7117568c507` |
| 40_Pilotmessung_Kosten.pdf | `32a37e5a4337884a698a834bc378ba594ae5d21e2951c761c56ee37d0fd4493b` |

## 2. Finale Nachprüfung nach Layoutkorrektur

Die vier Arbeitsmappen wurden erneut über `testakte_office_pdf.render_office_batch` mit dem gebündelten LibreOffice als native PDFs exportiert. Anschließend wurden sämtliche PDF-Seiten mit pypdfium2 erneut als PNG gerendert und alle 14 Seiten einzeln vollständig angesehen. Die SHA-256-Werte der vier XLSX vor und nach dem Export stimmen überein; der Export hat keine Originale verändert.

**Ergebnis: Sichtprüfung bestanden.** Die hellgrauen Zellgrenzen trennen die zuvor optisch zusammenlaufenden Inhalte. Datums- und Prüfstatusfelder in Mappe 38 sind nun mittig ausgerichtet und eindeutig getrennt. Zahlen in Mappe 40 erscheinen im deutschen Format, insbesondere 5.340,00 EUR, 12.066,60 EUR und 15.186,60 EUR. Die ergänzenden Quell- und Verwendungshinweise bleiben vollständig sichtbar. Keine offenen Befunde zu Textverlust, Überlagerung, Tabellenumbrüchen, defekten Zeichen oder fehlerhafter Zahlendarstellung.

| PDF | Geprüfte Seiten, einsbasiert | PDF SHA-256 | XLSX SHA-256 |
| --- | --- | --- | --- |
| 37_Vorhaben_Datenfluesse.pdf | 1–4 | `5267f5a2ab7e921d89f608491127fdcac0357f7ea734f11a57fde4678642fad4` | `c15b8b35b66de9333971a45a55c75600d415828e07d917e72855232f5ad9d23e` |
| 38_Massnahmen_Freigaben.pdf | 1–2 | `e62be5f6ca828f1f5171d67f6ffdcecf0d4102be952c2f60fc2d89a47874fd09` | `34bcaf688cbe333d199f374c4dc62a8f29efc36836b07b1af282e08a5d31d8b4` |
| 39_Lieferanten_Transfernachweise.pdf | 1–4 | `0288635ed170bf94ee986955213bdc8e8bdbe54b1417ab63a8d52f952fd2b0f9` | `43ca122ee1dda33df9153fb5857b2a8ca2e1117b745e70cfe7598ed9af6b1306` |
| 40_Pilotmessung_Kosten.pdf | 1–4 | `a6ee43397cb41d9a9b1b90886b574e426d665ddc83e9f21c8fe839782404a723` | `cb7a977ad33be51ab203eb1c36fd1c6d6b405d4cb462005469b2caf737a298fa` |

Die Abnahme gilt für genau diese Hashes. Ein späterer Neubau mit verändertem Inhalt oder Layout verlangt einen entsprechenden Abgleich. Die fachliche Quellenprüfung und die nativen Formeltests sind davon getrennte Prüfungen.

## 3. Abgleich mit allen 36 Aktenoriginalen

Nach Bereitstellung wurden die vollständigen Texte sämtlicher Originale 01 bis 36 gelesen: 17 DOCX, 14 EML und fünf PDF. Der Abgleich ist eine inhaltliche Belegprüfung, keine Aussage über die visuelle Abnahme jener Dokumente.

| Arbeitsmappeninhalt | Belege | Ergebnis |
| --- | --- | --- |
| Drei Vorhaben, Projektrollen, getrennte Gesellschaft MVZ, fehlende Betriebsfreigaben | 01, 02, 03, 34, 35, 36 | Stimmig. Der gewünschte Start 19.10.2026 bleibt Planungsziel, kein automatischer Betriebsbeginn. |
| P01: Frankfurt, mögliche Inhaltsdaten im Support, offenes Modelltraining und fehlender US-Nachweis | 04–12, 14–16 | Stimmig. Die synthetische Supportprobe 10 wird nicht als Echtdatentransfer oder bereits festgestellte Patientendatenpanne verbucht. |
| C5 Typ 1 vom 15.04.2026; behauptetes Erstinverkehrbringen am 04.11.2025; offene Systemabdeckung | 06, 12 | Stimmig. Keine automatische Anerkennung des Testats; die Ausnahme und die noch offenen Nachweise werden getrennt gehalten. |
| Radiologie: geplante Version 5.1, vorliegende Zweckbestimmung 5.0, lokale Verarbeitung und offene Wartungsrechte | 09, 17–21, 33 | Stimmig. Die Produktunterlagen und der lokale klinische Einsatz werden nicht als freigegeben ausgegeben. |
| Forschung: 2022–2025, pseudonymisierter Hochschuldatensatz, eigene MVZ-Gesellschaft, zusätzliche Trainingsidee | 09, 24–29, 34 | Stimmig. Weder die ungefähr 1.800 Suchfälle noch die geplanten Datenflüsse werden als genehmigte Studie oder erfolgter Export dargestellt. |
| Beschäftigtenbeteiligung, Freigabevorbereitung und Rückfallbetrieb | 14, 15, 20, 21, 30–36 | Stimmig. Die einzige beobachtete Rückfallzeit von sechs Minuten aus 32/33 wird nicht als Pilotmesswert übernommen. |
| P01-Angebot und interne Planwerte | 04, 08, 16, 35, 36 | 30 × 89,00 × 2 = 5.340,00 EUR; plus 4.800,00 EUR Einrichtung ergibt 10.140,00 EUR extern netto. 48 × 65,00 = 3.120,00 EUR interne Vollkosten. Keine doppelte Einrichtung oder Übertragung des P01-Preises auf P02/P03. |
| Netto- und Bruttoabgrenzung | 04, 16, 36 und Mappe 40 | Beleg 36 nennt 13.260,00 EUR auf Nettobasis einschließlich interner Vollkosten. Mappe 40 rechnet ausdrücklich externe Bruttokosten plus interne Vollkosten zu 15.186,60 EUR; der Unterschied von 1.926,60 EUR ist die separat ausgewiesene Umsatzsteuer, kein Widerspruch. |
| Acht Wochen und Planmenge | 01, 03, 15, 35, 36 | Acht × zwanzig = 160 geplante Briefe. Keine beobachteten Messwerte am 06.10.2026; daher keine Effizienz- oder Sicherheitsbehauptung. |

Die Arbeitsmappen bleiben bewusst fortzuschreibende Unterlagen. Mappe 40 enthält den Prüfzeitanteil, aber noch keine vollständige Vorher-Nachher-Zeiterhebung; eine Aussage über Nettozeitgewinn ist daraus nicht ableitbar. Die noch offene lokale Zwischenablageprüfung aus 22, 23 und 33 ist eine zusätzliche konkret zu verfolgende Aufgabe; die Maßnahmenmappe enthält sie bislang nicht als eigene Zeile. Diese Grenzen wurden dem Ersteller ausdrücklich gemeldet. Sie widersprechen keinem dargestellten Istwert und werden nicht als erledigt ausgegeben.

### 3.1. Hashes der gelesenen Aktenoriginale

| Original | SHA-256 |
| --- | --- |
| 01_Projektauftrag.docx | `68ed876297e312120435cf7712ce8c6f0e200a9f5de10456c8439efb0f7e87f3` |
| 02_Betriebsprofil.docx | `b3a6830bd40d687c5e81a1f3d16ce60b13c6213883a05e5e9e9d321997e8e9cf` |
| 03_Geschaeftsfuehrung_Starttermin.eml | `cc03d96e033d63c235db90093b42764269e993619ebf297fe1d459ad03ae072f` |
| 04_Angebot_Sprechfeder.pdf | `398a4ad22755992c4923e35ddfd38b3a3a358552770e700266ada845799d1a95` |
| 05_AVV_Lieferantenentwurf.docx | `e1d08403472f1d4744884aaa5e27a13d79aeb52a157b4bb0690ffbe85f12f9ac` |
| 06_TOM_und_Pruefbericht.pdf | `9a7f92bf2f0a54cd8c5d2e481ca757aad8b68e2c5e3a4bbdf519e2dddf3aa63a` |
| 07_Unterauftragsverarbeiter.docx | `4de3b21c972495c35475237b6246ad9f74a9d6036a86d9f0f854d822398c899b` |
| 08_Lieferant_Angebot_Anhang.eml | `3f5cd3597db4c86b84a37b3f1ac9b9a0ebea9b22cb89e1251a1f65e6835e10b1` |
| 09_Datenflussaufnahme.docx | `f3857d787e593e77dc065c8ec8efd0551f04e82e714f4cef72f14d649daee149` |
| 10_Supportprobe.pdf | `b261ce8881711906074ee47f9c79eba56b9823484b6b8ec45d117e737c670c54` |
| 11_TIA_Fragenstand.docx | `7b9ecc2884eac80bdfcd09092c604bf89c0adec736ab1dccd81c1b3ecb4cf204` |
| 12_DSB_Nachweise.eml | `172a5c36f73a1e291d5b0c8911932426c5f86a1ba5362ed47d756c64e8b6ca4a` |
| 13_Patienteninformation_Entwurf.docx | `5e831aca2d90e31539e4c8d88485e1d3ff8fafceed9bf83df812b5001023dd15` |
| 14_DSFA_Erhebung.docx | `ceb132c6d3103262076d4a013a0e53aba0f2277d57027f1001fd791617fe85cf` |
| 15_Station_Rueckfragen.eml | `fd1799732f99c90f35dea0c9cb23cc964ea3708c99a0196008837ed222b10e7b` |
| 16_Einkauf_Vertrag.eml | `85ba5ad86cf0132f040570af5c8686e3a912422fab277fbe19eea1808cef61ea` |
| 17_Zweckbestimmung_Radiaviso.pdf | `c1dc9f5657d3ae1ecc9e90d0fc9061b73301936999412221de4a8246b3048601` |
| 18_Konformitaet_Lieferstand.docx | `99121c9969b0b0b25eaada57b7baa9993be09095d624c45e6b69235ed4d78103` |
| 19_Radiaviso_Anhang.eml | `e0fc2e670bb7f6cc05878270e655028433a6a2ac030095c9dd650482b7fad9d0` |
| 20_Medizintechnik_Abgleich.docx | `ec8c6efcd7d597a87368487605919bc8b5192c797296ffbb9042331a949af361` |
| 21_Radiologie_Wunsch.eml | `123408debc064cab4accf41e5261146997080c4196e6fb651b92202ced1ac255` |
| 22_Beinahevorfall.docx | `feba77d8f27e251c556b633e393654ec80bf3e1be293751fb397c44a015a3cab` |
| 23_Ticket_Beinahevorfall.eml | `3116ba35d9eb7e5fa6c31851e9a4ce567789671eab5b995a1a21f89665010737` |
| 24_Forschungsprotokoll.docx | `55089f2789842723477b13f252e1710b53923d55a840a59f16fa8bb979df9ef9` |
| 25_Datenkatalog_Forschung.docx | `777dbf5b3061003a30f5a9c1d7af5d0d5a7edeec63c1a87b00f4d36cdcc83bcd` |
| 26_Ethikanfrage.docx | `814d51d3f07696d3096513e09f1e0819f5c7897d2275aa423ad6ffa49ea29e0e` |
| 27_Forschung_Modelltraining.eml | `9a08ec2c74ce157833022d46d09c545e312fc03023045c9a7945378505f067e4` |
| 28_MVZ_Datenanfrage.eml | `413b945d4889f9addbad4a4048d0ea12f27c8e86e732f96895f82b93b4a5c3d6` |
| 29_Kooperationsentwurf.docx | `3b028ddde7e252da483724a92dff9ca2088bac5f5a970f8f155cd781ee06e26c` |
| 30_Betriebsrat_Anfrage.pdf | `3a4ca1e97c3dcb72d4241a1e78aab652aa0511b7c3c6ae2ddb04e211e4e835e6` |
| 31_Betriebsrat_Termin.eml | `1cb84e969018c0261d92497605b0783e33557b7d248da8c7ca77f793853dbc5f` |
| 32_Notfallprobe.docx | `416d9e741ff4ec6fb4a7c596ae59b06a05a6189957a5e5885ce01379469704b0` |
| 33_ISB_Rueckmeldung.eml | `82d9f65c50d068cb8d0a1a13f0cc3647362d2033d8bb6feb1636cef2fd5f7073` |
| 34_Rechtsabteilung_Rollen.eml | `8c6abc76b000c485b4d42bfd342c1151a008687da5d0854ccafb765d7d036893` |
| 35_IT_Aktenuebergabe.eml | `8286e54988d42a0c3f82389946892ef88fe25cfc30fe9a377ed752ba4f936bd6` |
| 36_Lenkungsrunde_Stand.docx | `dcbd16ed865a357ec35452341b19051d80f3cb85fd599fc7bfbf74a3af322f9a` |


## 4. Abschließende Schreibweisenkorrektur und finaler XLSX-Stand – 6. Oktober 2026

Nach der formalen Ersetzung der Paragrafzeichen in den Hinweisen der Mappe 39 wurde deren PDF erneut mit der nativen Office-Engine erstellt. Die vier Seiten wurden erneut gerendert. Die betroffenen Hinweise auf Seite 2 (Tabellenzeilen 21 und 27) wurden gezielt visuell geprüft: „Paragraf 393 Absatz 4 SGB V“ und „Paragraf 393 SGB V“ sind vollständig lesbar, ohne Abschneiden oder Überlagerung. Die Aussage zur begrenzten 18-Monatsregel und die Abgrenzung des TIA bleiben erhalten. Kein neuer Layoutbefund.

Der abschließende native Prüfbericht enthält 7 bestandene Basisprüfungen und 11 bestandene Mutationsprüfungen. Die dort protokollierten Hashes wurden mit allen vier aktuellen Originalmappen abgeglichen; sie stimmen überein. Maßgeblich für den finalen XLSX-Stand sind die folgenden Hashes (frühere Tabellen dokumentieren die vorherigen Prüfstände).

| Finale Arbeitsmappe | SHA-256 |
|---|---|
| 37_Vorhaben_Datenfluesse.xlsx | `5e8f18f0bfc25e80026269b0c0baffaca95c1098d8e86b2f30e456d6d3703c18` |
| 38_Massnahmen_Freigaben.xlsx | `bc62e1ce4ecc08b9f800f6f30b206b899b87cccdf29a9adc664f34ca35258f16` |
| 39_Lieferanten_Transfernachweise.xlsx | `e49a34f3c0600a2011d767b6ddc015a0d20ceb64108182ecf16bb461053a8ec3` |
| 40_Pilotmessung_Kosten.xlsx | `0fe9d9e5330e474dbed0cee8d134fb77717381c7a05223b6b40870893c3887df` |

Neu erzeugtes PDF 39, 4 Seiten: `a0f9630243a379c11ca4a1a3f16542903632af8da76f5bcd09bd4415b6ead414`.
