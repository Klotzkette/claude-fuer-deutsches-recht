---
name: website-veroeffentlichen-wiederherstellen
description: Überträgt konkret freigegebene Website-Änderungen in das verbundene Zielsystem, prüft den öffentlichen Stand und dokumentiert die Veröffentlichung. Behandelt Konflikte, Timeouts und Rücknahmen ohne Doppelveröffentlichung oder Verlust späterer Änderungen.
---

# Website-Änderungen veröffentlichen und wiederherstellen

## 1. Zweck und Anwendungsfall

Setzen Sie genau die geprüfte Änderung um. Ein Entwurf, eine fachliche Prüfung und ein Veröffentlichungsauftrag sind verschiedene Dinge. Ohne geeignete Verbindung entsteht ein Übergabepaket, kein angeblich veröffentlichter Beitrag.

## 2. Eingaben

Zielsystem, Site, Zielpfad, Basisrevision, vollständige Fassung einschließlich Medien und Hinweis, Freigabe und Rücknahmemöglichkeit. Vergleichen Sie diese Angaben mit der tatsächlich verbundenen Site. Geheimnisse nur über den geschützten Verbindungsweg, nie aus der Redaktionsakte beziehen.

## 3. Ablauf

1. Lesen Sie aktuellen Zielstand und Auftragsstatus. Existiert dieselbe Auftragskennung bereits, den vorhandenen Stand prüfen statt einen zweiten Beitrag anzulegen. Bei fremden Änderungen anhalten und Differenz zeigen.
2. Vorzustand und Wiederherstellungsschritt sichern. Prüfen Sie den exakten Freigabeumfang, Rechte, Quellennachweise und Transparenzentscheidung. Eine Änderung nach Freigabe verlangt neue Bestätigung der geänderten Fassung.
3. Wenn lokale Ausführung verfügbar ist, kann `scripts/freigabe_pruefen.py` einen strukturierten Freigabeentwurf prüfen. Das Werkzeug ist nur eine formale Gegenprüfung, kein Nachweis tatsächlicher menschlicher Kontrolle oder ein CMS-Connector.
4. Über die vorhandene unterstützte Schnittstelle zuerst Vorschau oder Entwurf verwenden. Seiteninhalt, Medien, Links, Mobilansicht und gegebenenfalls Hinweisposition prüfen. Dem Nutzer Ziel und Änderung vor der Außenhandlung eindeutig vorlegen, soweit nicht genau diese Fassung bereits ausdrücklich freigegeben wurde.
5. Einmal veröffentlichen. Bei Timeout nicht blind wiederholen: Auftragskennung, Zielrevision oder URL nachlesen. Bleibt der Zustand unklar, als unklar melden und weitere Schreibversuche stoppen. Wiederholte Leseversuche begrenzen.
6. Öffentliche URL abrufen und Inhalt, Medien, Hinweis, Statuscode sowie erwartete Revision oder charakteristische Textstellen vergleichen. Ein erfolgreicher API-Aufruf oder Vorschaubild allein bestätigt den öffentlichen Stand nicht.
7. Bei Fehler Rücknahme nur für die eigene Änderung und nur ohne Vernichtung fremder späterer Änderungen vorbereiten oder im konkret freigegebenen Umfang ausführen. Erneut verifizieren. Ergebnis und offene technische Punkte speichern; der Nutzer erhält einen prüfbaren Link.

## 4. Quellenpflicht

[Redaktionsbetrieb](../../references/redaktionsbetrieb.md), [Recht und Transparenz](../../references/recht-und-transparenz.md) und aktuelle Dokumentation des konkret genutzten Systems. Nicht dokumentierte Parameter nicht erraten. [Quellenregeln](../../references/zitierweise.md).

## 5. Ausgabeformat

„Veröffentlicht“, „nur als Entwurf gespeichert“, „Übergabepaket erstellt“ oder „Zustand ungeklärt“ mit ehrlichem Nachweis. Vollständig formulierte Abschlussnotiz, keine bloße Erfolgsmeldung. Webinhalte folgen dem Webdesign, ein separater formatierter Vermerk Times New Roman 11 pt und dezimaler Gliederung.

## 6. Beispiele

Nach einem Speicher-Timeout wird zuerst die Zielseite gelesen. Hat ein Kollege inzwischen die Seite bearbeitet, darf eine alte Komplettsicherung nicht als vermeintlich sichere Wiederherstellung eingespielt werden.
