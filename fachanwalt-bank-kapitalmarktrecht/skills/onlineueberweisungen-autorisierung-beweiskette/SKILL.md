---
name: onlineueberweisungen-autorisierung-beweiskette
description: "Rekonstruiert bestrittene Onlineüberweisungen anhand von Freigabeanzeigen, Gerätewechseln, Transaktionsprotokollen und Sperrmeldungen. Trennt Autorisierung, Authentifizierung, Erstattungsbetrag und Gegenansprüche bei Phishing oder vorgetäuschten Bankanrufen."
---

# 1. Zweck und Anwendungsfall

Prüfe hohe Kontobelastungen, bei denen die Zustimmung zur Zahlung bestritten wird. Die wirtschaftliche Bedeutung liegt im unmittelbaren Liquiditätsverlust; aufwendig ist der Abgleich technischer Aufzeichnungen mit den Angaben der Beteiligten. Anders als bei der allgemeinen Vorbereitung eines Bankprozesses wird jede Überweisung mit ihrer eigenen Freigabe- und Beweiskette geprüft. Nicht für Anlageberatung oder bloß fehlerhafte Ausführung einer unstreitig autorisierten Überweisung.

## 1.1. Eingaben

Zuerst Kontovertrag, Verbraucher- oder Unternehmerstatus, Belastungen, Reklamation, Bankantwort, Nachrichten und vorhandene Protokolle lesen. Je Vorgang Betrag, Währung, Empfänger, Zeit mit Zeitzone, Gerätebindung, Freigabetext, handelnde Person, tatsächliche Wahrnehmung, Sperrmeldung und Rückfluss erfassen. Niemals PIN, TAN oder Zugang zur Bank verlangen; keine Anmeldung und kein Nachspielen des Angriffs.

## 1.2. Ablauf und Checkliste

1. Erstelle eine unveränderte Ereignischronologie. Trenne Anmeldung, Registrierung eines neuen Geräts, Empfängeranlage und einzelne Zahlungsfreigabe. Angaben des Kunden, technische Aufzeichnung und Schlussfolgerung bleiben unterschiedliche Spalten. Eine Gerätefreigabe ist nicht automatisch Zustimmung zu jeder Folgeüberweisung.
2. Prüfe für jede Zahlung zuerst die Zustimmung nach Paragraf 675j BGB. Hat der Kunde bewusst genau Betrag und Empfänger freigegeben, obwohl er über den Zweck getäuscht wurde, darf der Vorgang nicht allein wegen Betrugs als unautorisiert gelten. Bei streitigem Anzeigetext beide Tatsachenvarianten bewerten, ohne aus der TAN-Nutzung Zustimmung abzuleiten.
3. Bestimme den Erstattungsweg nach Paragraf 675u BGB und den Zeitpunkt der Kenntnis der Bank. Unverzügliche Anzeige und Ausschlussfrist nach Paragraf 676b BGB gesondert prüfen, einschließlich ordnungsgemäßer Unterrichtung und möglicher Unternehmervereinbarungen nach Paragraf 675e BGB. Eine Anzeige bei der Polizei ersetzt die Unterrichtung der Bank nicht.
4. Prüfe den Nachweis nach Paragraf 675w BGB: Authentifizierung, Aufzeichnung, Verbuchung und Störungsfreiheit. Fordere vorgangsbezogen vorhandene Freigabeanzeigen, Geräte-Registrierungsprotokolle, Sitzungszuordnung, starke Kundenauthentifizierung und unterstützende Beweismittel an. IP-Adresse oder erfolgreiches Verfahren allein identifiziert nicht notwendig den zustimmenden Menschen. Kein pauschaler Anspruch auf den gesamten Quellcode des Banksystems.
5. Prüfe den Gegenanspruch nach Paragraf 675v BGB getrennt: konkrete Pflicht, Handlung, subjektiver Vorwurf, Kausalität und Schaden. Warntext, Sichtbarkeit, Täuschungssituation und individuelles Verständnis würdigen. Weder Phishing automatisch als grob fahrlässig noch die erfolgreiche Authentifizierung als Entlastung behandeln. Absätze 2, 4 und 5, insbesondere fehlende starke Kundenauthentifizierung und Nutzung nach Sperranzeige, vor Haftungsbetrag prüfen. 50 EUR sind kein pauschaler Selbstbehalt jeder Reklamation.
6. Rechne je Vorgang Belastung minus endgültiger Rückfluss gleich offener Erstattungsbetrag. Vorläufige Gutschrift, endgültige Erstattung, Rückholung und Bankgegenforderung getrennt buchen. Zinsen und Gebühren nur mit eigenem Grund und Nachweis. Dasselbe Geld nicht zweimal verlangen oder abziehen.
7. Höchstens eine gebündelte Rückfrage zu ausschlaggebenden Lücken. Liefere danach begründete Positionen und gezielte Beleganforderung; nur die unsichere Zahlung bleibt offen. Keine Kontosperre, Überweisung, Strafanzeige, Klage oder Kommunikation eigenmächtig veranlassen.

Bei zusätzlich geltend gemachtem Schadensersatz nach Artikel 82 Absatz 1 der Datenschutz-Grundverordnung prüfe den behaupteten Datenschutzverstoß, den konkreten Schaden und deren ursächlichen Zusammenhang anhand gesonderter Belege. Leite die Kausalität nicht allein aus dem Ergebnis der Erstattungsprüfung nach Paragraf 675u BGB ab.

## 1.3. Quellenpflicht

Optional ergänzt die [Zitierweise](../../references/zitierweise.md) die Quellenarbeit. Entscheidungen mit Gericht, Datum, Aktenzeichen und überprüfter Fundstelle zitieren; Tatsachen und Schlussfolgerungen trennen. Prüfstand 15.09.2026, vor Einsatz Normfassung und technische Übertragbarkeit prüfen.

- BGB [Paragraf 675u](https://www.gesetze-im-internet.de/bgb/__675u.html), [Paragraf 675v](https://www.gesetze-im-internet.de/bgb/__675v.html), [Paragraf 675w](https://www.gesetze-im-internet.de/bgb/__675w.html) und [Paragraf 676b](https://www.gesetze-im-internet.de/bgb/__676b.html).
- BGH, Beschluss vom 07.07.2026, Az. XI ZR 71/25, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XI_ZS/2025/XI_ZR__71-25.pdf?__blob=publicationFile&v=1), Seite 2, vollständig geprüft am 15.09.2026: Ein zusätzlicher Anspruch aus Artikel 82 Absatz 1 der Datenschutz-Grundverordnung neben Paragraf 675u Satz 2 BGB blieb offen; im konkreten Fall fehlte der Kausalzusammenhang zwischen behaupteten Verstößen und Schaden. Den Beschluss weder als allgemeinen Anspruchsausschluss noch als eigenständige Aussage zu Autorisierung oder grober Fahrlässigkeit verwenden.
- BGH, Urteil vom 26.01.2016, Az. XI ZR 91/14, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XI_ZS/2014/XI_ZR__91-14.pdf?__blob=publicationFile&v=1), Randnummern 18 und 19, 75 sowie 79 bis 81: Grenzen des Authentifizierungsnachweises, kein Erfahrungssatz grober Fahrlässigkeit und technische Beweissicherung. Entscheidung zur damaligen Rechtslage; heutige starke Kundenauthentifizierung und Paragraf 675v nicht aus alten Absatznummern ableiten.

## 1.4. Ausgabeformat

`ergebnis.md` enthält Sachverhalt, Überweisungstabelle, Beweisketten mit konkreten Lücken, Erstattungsrechnung, Gegenanspruchsprüfung und ausformulierten Reklamations- oder Verteidigungsentwurf. Jede Tatsachenvariante nennt den entscheidenden Beleg und ihre finanzielle Auswirkung. Internes Risiko nicht ungeprüft in das Außenschreiben übernehmen.

Ausformulierungspflicht: vollständige Sätze, keine Skelette. Formatstandard: Times New Roman 11 pt, dezimale Gliederung mit Leerzeilen und Exporthinweis bei Markdown. Nur tatsächlich erzeugte Dateien verlinken.

## 1.5. Beispiele

Ein Anruf führt zur Freigabe einer angeblichen Geräteerneuerung; danach folgen zwei Überweisungen. Rekonstruiere zwei Zahlungsfreigaben gesondert. Ein fehlender technischer Nachweis darf nicht durch die Behauptung ersetzt werden, wer sein Gerät freigebe, genehmige damit alle späteren Zahlungen.
