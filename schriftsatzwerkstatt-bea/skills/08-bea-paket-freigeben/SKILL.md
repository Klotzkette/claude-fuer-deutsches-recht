---
name: 08-bea-paket-freigeben
description: "Unmittelbar vor Übergabe eines konvertierten beA-Pakets an den Versender: gleicht PDFs, Anlagenfolge, Manifest, Hashes, Dateinamen, Gericht, Aktenzeichen, Frist, Signaturweg, Dateizahl und Größe ab. Liefert Freigabekarte und Versandauftrag. Versendet nicht selbst; Freigabe nur durch eine reale benannte Person."
---

# beA-Paket prüfen und zur Übergabe vorbereiten

## Zweck und Anwendungsfall

Dieser Skill ist das letzte Gate vor dem tatsächlichen beA-Versand. Er bündelt ausschließlich bereits geprüfte Dateien und gibt sie nur mit realer Freigabe an die benannte versendende Person weiter.

## Eingaben

- `_bea_ausgabe/upload` mit finalen PDFs.
- `versandmanifest.csv`, Konvertierungs- und Prüfprotokoll.
- Anlagenplan und gesperrter Hauptschriftsatz-Hash.
- Gericht/SAFE-Empfänger, Aktenzeichen oder Neueingang, Betreff und Frist.
- Signatur-/Versandwegmatrix aus Skill 07.
- tatsächlich vorgesehenes beA-/eBO-/Kanzleisystem mit sichtbarem Clientstand und XJustiz-Profil.
- reale Freigabeperson.

## Ablauf / Checkliste

1. Upload-Ordner neu inventarisieren. Er darf nur die für genau diese Nachricht bestimmten PDFs enthalten.
2. Hauptschriftsatz als Datei 01 und alle Anlagen in logischer Reihenfolge öffnen.
3. Dateiname, sichtbare Anlagenbezeichnung, Schriftsatzzitat und Manifest zeilenweise abgleichen.
4. Quellhash, Ausgabehash, Seitenzahl und Sichtstatus nach dem [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md) für Hauptschriftsatz und jede Anlage abgleichen. Ohne geschlossene Quell-zu-PDF-Kette keine Freigabe.
5. Den lokalen Paketvalidator gegen genau diesen Ausgabeordner ausführen. Er prüft PDF-Struktur, SHA-256, Bytes, Seitenzahl, Manifestkopf, relative Quellenpfade, Reihenfolge und Rollen; jeder Fehler ist rot.
6. Dateinamen auf ASCII-Zeichen, Unterstriche, genau einen Endungspunkt und höchstens 80 Zeichen prüfen.
7. Anzahl und Gesamtgröße exakt berechnen. Über 900 Dateien oder 180 MB gelb warnen; über 1.000 Dateien oder 200 MB rot stoppen.
8. Erzeugt das reale Signatur-/Versandsystem bei qeS ein abgesetztes CAdES-Artefakt, nur `.p7`, `.p7s`, `.p7m` oder `.pkcs7` zulassen und `signaturmanifest.csv` vollständig führen. Ziel-PDF und Zielhash, Signaturhash und Bytes, CAdES/qeS, Unterzeichner, grünen Prüfstatus und internes Prüfprotokoll abgleichen. Dateizahl und Gesamtbytes danach neu rechnen. Das Artefakt weder umbenennen noch vorab simulieren.
9. Kein ZIP, keine Office-Datei, kein internes Protokoll, kein Passwortschutz und kein ausführbarer Inhalt im Upload-Ordner. Neben Versand-PDFs sind nur die nach Schritt 8 zugeordneten CAdES-Dateien zulässig.
10. Das fertige Paket im tatsächlich vorgesehenen beA-/eBO-/Kanzleisystem als Entwurf laden oder dessen aktuelle Vorprüfung verwenden. Datum, sichtbaren Clientstand, XJustiz-Profil und jede Dateinamens-, Anhangs-, Signatur- oder Strukturwarnung wörtlich protokollieren. Eine lokal grüne Prüfung überstimmt keine Clientwarnung; offene Warnungen bleiben gelb oder rot.
11. Gericht, SAFE-Empfänger, Aktenzeichen/Neueingang, Betreff, Frist und ein Verfahren je Nachricht durch reale Person bestätigen lassen. Empfänger- oder XJustiz-Daten nie aus dem Dateinamen ableiten oder ergänzen.
12. Signaturweg aus Skill 07 muss grün sein. Bei einfacher Signatur verantwortliche und versendende Person erneut abgleichen.
13. Die einschlägigen Punkte des [100-Punkte-Fehlerkatalogs](../../references/100-punkte-fehlerkatalog.md) abschließen. Automatische und personengebundene Prüfungen getrennt ausweisen.
14. Freigabekarte aus der [Vorlage](../../templates/pruefprotokoll.md) ausfüllen. Status bleibt `ENTWURF - NICHT VERSENDEN/EINREICHEN`, bis eine reale Person die konkrete Hashfassung freigibt.
15. Nach realer Freigabe internen Status `FREIGEGEBEN - ZUR TECHNISCHEN ÜBERMITTLUNG DURCH [NAME]` setzen. Diese Kennzeichnung gehört nicht in den Schriftsatz.
16. [Versandauftrag](../../templates/versandauftrag.md) mit Dateizahl, Gesamtgröße, Manifest-Hash, Validatorlauf und versendender Person ausgeben.

## Quellenpflicht

Paketgrenzen, Dateiformate und Signaturweg folgen dem [ERV-Versandstandard](../../references/erv-versandstandard.md); Benennung und Manifest dem [Dateinamen- und Manifeststandard](../../references/dateinamen-und-manifest.md); Quellbindung und Sichtabgleich dem [Inhaltstreue- und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md); der Preflight dem [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Keine Rechtsprechungsanker.

## Ausgabeformat

1. Preflight-Matrix mit grün/gelb/rot.
2. exakte Dateiliste mit Hash, Seiten und Bytes.
3. interne Freigabekarte.
4. vollständig ausgefüllter Versandauftrag.
5. klarer Hinweis, dass nur die benannte reale Person versendet.

Alle Protokolle werden in vollständigen Sätzen ausgefüllt. Offene Platzhalter, ungeprüfte PDFs oder eine vom System behauptete Freigabe schließen das Paket aus.

## Beispiele

- 14 PDFs, 28 MB, alle Hashes passend, einfacher Namenszug und identischer Versender: technisch freigabefähig.
- 181 MB: gelbe Warnung und Paketreserve prüfen, obwohl amtliche Obergrenze noch nicht überschritten ist.
- Upload-Ordner enthält `manifest.csv`: entfernen; interne Datei nicht mitsenden.
