---
name: anlagenkonvolut-konsolidieren
description: "Konsolidiert mehrere zusammengehörige Belegdateien zu einer gerichtstauglichen Anlage: liest den Bestand zuerst, trennt Dubletten und Fassungen, bestimmt Eltern- und Unteranlagen, erzeugt Deckblatt, Inhaltsliste, Seitenstempel und Lesezeichen, gleicht jeden Teil mit dem Beweisthema im Schriftsatz ab und liefert Einzelanlage, Prüfkonvolut, Hashprotokoll und."
---

# Anlagenkonvolut konsolidieren

## 1. Direktstart

Lies zuerst den Schriftsatz, das bisherige Anlagenverzeichnis und sämtliche Kandidatendateien. Liefere ohne vorgeschalteten Fragenkatalog eine Bestandsmatrix mit Dateiname, Datum, Absender, Dokumentart, Seitenzahl, Hashwert, Fassung, Beweisthema und vorgesehener Unteranlage. Frage nur nach einer Zuordnung, die weder aus Datei noch Schriftsatz hervorgeht und die Konsolidierung sperrt.

## 2. Konsolidierungsentscheidung

Mehrere Dokumente dürfen nur dann eine gemeinsame Anlage bilden, wenn sie ein einheitliches Beweisthema nachvollziehbar dokumentieren, etwa eine vollständige E-Mail-Kette mit Anhängen oder einen Vertrag mit Nachträgen. Bloße gemeinsame Herkunft, Dateiformat oder Ordnerlage genügt nicht.

| Entscheidung | Voraussetzung | Ergebnis |
| --- | --- | --- |
| getrennte Anlagen | eigenständige Beweisthemen oder getrennte Schriftsatzbezüge | fortlaufende K- oder B-Nummern |
| Elternanlage mit Unteranlagen | ein Beweisthema, mehrere klar trennbare Dokumente | Deckblatt und K 5/1, K 5/2 fortlaufend |
| eine mehrseitige Anlage | ein Dokument oder untrennbare Dokumentfolge | eine Nummer, jede Seite bezeichnet |
| nur interne Prüffassung | Gesamtüberblick wird gebraucht, Gericht soll Einzeldateien erhalten | Lesezeichen-Konvolut im Ordner `intern/` |

Ein zusammengeführtes Prüfkonvolut ist nicht automatisch die Versandfassung. Gerichtliche Hinweise zur getrennten Einreichung haben Vorrang.

## 3. Produktionslauf

1. Originale unverändert sichern und Hashwerte bilden.
2. Dubletten, Entwürfe, OCR-Fassungen und spätere Endfassungen kennzeichnen; nur eine gerichtliche Fassung je Dokument bestimmen.
3. Beweisthema und genaue Fundstelle im Schriftsatz jeder Datei zuordnen.
4. Elternnummer und Unterfolge ohne Lücken oder Doppelbelegung festlegen.
5. Dateigrenzen, chronologische Reihenfolge und Seitenausrichtung kontrollieren.
6. In PDF konvertieren, Ergebnis visuell gegen das Original prüfen und fehlende OCR kenntlich machen.
7. Deckblatt und kurze Inhaltsliste mit Dokumentdatum, Absender, Empfänger und Seitenbereich erzeugen.
8. Jede Seite oben rechts mit Eltern- und erforderlichenfalls Unteranlagenbezeichnung versehen.
9. Lesezeichen an jeder Dokumentgrenze und eine fortlaufende interne Seitenzählung anlegen.
10. Anlagenzitate, Verzeichnis, Dateinamen und finale PDFs gegeneinander prüfen.

## 4. Normen- und Quellenanker

- ZPO Paragraf 130 Nummer 6: Bezeichnung der beigefügten Urkunden.
- ZPO Paragraf 130a und ERVV Paragraf 2: elektronisches Dokument und technisch geeignete Dateiformate.
- ZPO Paragraf 131: Beifügung von Urkunden, auf die im Schriftsatz Bezug genommen wird.
- ZPO Paragraf 138: konkreter und wahrheitsgemäßer Tatsachenvortrag; ein Anlagenkonvolut ersetzt keinen verständlichen Vortrag im Schriftsatz.
- ZPO Paragraf 253 Absatz 2: bestimmter Antrag und hinreichend bestimmter Klagegrund bleiben im Hauptdokument erforderlich.

Für Format-, Dateinamen- und Versandfragen gelten `references/ANLAGEN-STANDARDS.md` und `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und geprüfter amtlicher Quelle verwendet.

## 5. Stop-Kriterien

Stoppe die Versandfreigabe bei fehlender oder doppelter Nummer, nicht erklärter Fassung, unterbrochener E-Mail-Kette, unlesbarer Seite, fehlendem Anhang, unstimmigem Schriftsatzbezug, aktivem PDF-Inhalt, Kennwortschutz oder nicht kontrollierter Konvertierung. Beschreibe den Befund datei- und seitengenau und nenne den nächsten Reparaturschritt.

## 6. Output

Liefere eine gerichtliche Einzelanlage oder getrennte Einzelanlagen, ein Anlagenverzeichnis, eine Zuordnungsmatrix Schriftsatzstelle zu Beleg, ein Hash- und Fassungsprotokoll, einen visuellen Prüfvermerk und nur bei Bedarf ein internes Lesezeichen-Konvolut. Übergib die fertigen Dateien anschließend an `bea-versandmappe-endfertigung`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
