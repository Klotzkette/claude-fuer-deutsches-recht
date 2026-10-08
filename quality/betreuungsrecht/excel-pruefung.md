# 1. Excel-Prüfung der Unterlagenauswertung

Stand: 08.10.2026.

Die drei Arbeitsmappen wurden mit `@oai/artifact-tool` im gebündelten Node-Laufzeitsystem erzeugt. Der reproduzierbare Builder ist `scripts/build-betreuung-unterlagen-workbooks.mjs`. Er liest die kanonischen Falldaten aus `scripts/data/betreuung-pimpernell.json`; die generische Vorlage enthält keine Falllösung und keine beibehaltenen Testeingaben.

## 1.1. Gelieferte Arbeitsmappen

| Arbeitsmappe | Inhalt | Abgrenzung |
|---|---|---|
| `betreuungsrecht/templates/unterlagen-abrechnung.xlsx` | Sechs Blätter: Abrechnung, Konten, Buchungen, Belege, Rückfragen und Anleitung. | Fallneutrale Arbeitsvorlage mit 1.500 Buchungszeilen, 20 Konten, 300 Belegen und 100 Rückfragen. |
| `testakten/betreuung-adelheid-pimpernell-dreijahresabrechnung/06_Tabellen/Bankexport_2023-10_bis_2026-09.xlsx` | 584 Bankbuchungen sowie 72 Monatskontenabgleiche für Giro- und Sparkonto. | Bankseitige Zahlungsdaten mit Originaltext, Datum, Betrag und Quellenzuordnung; keine rechtliche Verdachtslösung. |
| `testakten/betreuung-adelheid-pimpernell-dreijahresabrechnung/06_Tabellen/Haushaltsnotizen_Adelheid_2026-10-02.xlsx` | 14 Haushaltspositionen aus Gespräch und erster Sichtung. | Bewusst offene Erinnerungen und fehlender Bargeldbestand; kein vollständiger Haushaltsabschluss. Der Dateiname verweist auf das Gespräch, die Zusammenstellung trägt den Stand 08.10.2026. |

## 1.2. Fachliche Rechenlogik

Der Kontenabgleich enthält jede erfasste Bewegung innerhalb des eingestellten Zeitraums. Die Einnahmen- und Ausgabenauswertung berücksichtigt die manuelle Bestätigung der Zuordnung. Erstattungen, Umbuchungen, Bargeldbewegungen und ungeklärte Positionen werden getrennt ausgewiesen. Eine Bargeldabhebung wird nicht automatisch zum nachgewiesenen Verbrauch. Eigene Kontenüberträge werden nicht doppelt als Einnahme und Ausgabe gezählt.

Anfangssaldo, Endsaldo laut Beleg, Bewegungen, rechnerischer Endsaldo und Differenz sind getrennt sichtbar. Ein nicht ausgefüllter Saldo unterscheidet sich von der Zahl Null. Offene Rückfragen bleiben auch nach einer Freigabe offen. Der Status „erledigt“ vermindert die Anzahl offener Rückfragen erst zusammen mit einem dokumentierten Erledigungsnachweis.

Die Vorlage bietet keine automatische rechtliche Auswahl zwischen Kündigung, Widerruf, Rücktritt, Anfechtung und Rückforderung. Die hierfür erforderliche Sachverhalts- und Rechtsprüfung gehört in den Skill. Empfänger, Adressquelle, Frage, Entwurfspfad, persönliche Freigabe und Versand- oder Antwortbeleg haben getrennte Eingabefelder.

## 1.3. Ausgeführte Prüfungen

1. Alle 584 Buchungsbeträge und ihre Datums-, Konto- und Quellenfelder stammen aus der kanonischen JSON-Datei. Geldbeträge sind numerisch; Datumsfelder sind echte Excel-Datumswerte mit Zahlenformat.
2. Sämtliche 72 Monatsrechnungen stimmen centgenau. Eine Erhöhung der ersten Bankbuchung um einen Cent erzeugt eine Differenz von einem Cent. Anschließend wurde die Originalbuchung wiederhergestellt.
3. In einer getrennten Prüfbelegung der Vorlage wurden Ausgaben von 20,00 EUR auf 21,37 EUR geändert. Die Ausgabensumme reagierte mit 21,37 EUR, die Kontendifferenz mit minus 1,37 EUR.
4. Weitere Prüfungen unterscheiden fehlenden Anfangssaldo und echten Nullsaldo, unbestätigte und bestätigte Zuordnungen, Bargeldverwendung, fehlende und passende Umbuchungsgegenbuchung sowie doppelte Buchungs-IDs.
5. Eine offene Rückfrage blieb nach persönlicher Freigabe offen. Auch „erledigt“ ohne Antwort- oder Erledigungsbeleg genügte nicht. Erst der zusätzliche Nachweis änderte den errechneten Offenstand.
6. Alle temporären Werte wurden vor der Auslieferung der Vorlage entfernt. Die leere Vorlage meldet den fehlenden Zeitraum, null erfasste Prüfpositionen und null angelegte Rückfragen.
7. Formel-Fehlersuche mit Artifact Tool ergab keine Fehler. In einer zusätzlichen LibreOffice-Neuberechnung der exportierten Arbeitsmappen blieben alle 72 Kontendifferenzen null. Eine separat exportierte Eingabeänderungs-Prüfkopie errechnete auch dort 21,37 EUR Ausgaben und minus 1,37 EUR Kontendifferenz.
8. Jedes der zehn Blätter wurde gerendert und visuell gelesen. Korrigiert wurde die Datumsdarstellung der Bankliste; die endgültige Darstellung verwendet `yyyy-mm-dd`. Überschriften, Geldbeträge, offene Angaben und Quellen bleiben lesbar. Times New Roman 11 pt ist die Grundschrift.

## 1.4. Grenzen und Fortführung

Die Berechnung wurde mit Artifact Tool und dem gebündelten LibreOffice überprüft. Ein interaktiver Test in Microsoft Excel wurde nicht durchgeführt. Die Arbeitsmappen enthalten native Tabellen, Formeln, Datums- und Geldformate sowie Eingabeauswahllisten; sie enthalten keine Makros und keine Bank- oder Versandverbindung.

Bei Erweiterung der Vorlage müssen sowohl die Tabellen als auch die ausdrücklich begrenzten Formelbereiche verlängert werden. Die Anleitung nennt ihre Kapazitäten. Die reinen Teilnehmerunterlagen enthalten keine ausgefüllte Auswertung der Verdachtspositionen. Rechenprüfungen, Vorschauen und Prüfkopien bleiben außerhalb der Testakten-Archive.
