---
name: bea-paketierung-groessen-und-versandplan
description: "Plant große beA-Einreichungen nach ERVV und ERVB 2025: zählt Dateien und Bytes, hält mehrseitige Anlagen zusammen, bildet nachvollziehbare Teilnachrichten, führt Anlagenbereiche und Hashwerte fort und liefert Betreff, Begleitvermerk, Versandfolge sowie getrennte Eingangskontrollen für jede Nachricht."
---

# beA-Paketierung und Versandplan

## 1. Einsatz

Nutze diesen Skill, wenn die Versandmappe die technische Grenze einer Nachricht erreichen könnte oder mehrere Schriftsätze und Anlagen in kontrollierter Reihenfolge eingereicht werden müssen.

## 2. Rechts- und Technikanker

- ZPO Paragraf 130a Absatz 5: Eingang und automatisierte Eingangsbestätigung.
- ZPO Paragraf 130a Absatz 6: unverzügliche Nachreichung eines geeigneten Dokuments nach gerichtlichem Hinweis auf technische Ungeeignetheit.
- ZPO Paragraf 130d: elektronische Nutzungspflicht und Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit.
- ERVV Paragraf 2: PDF und technische Eignung.
- ERVB 2025: höchstens 1000 Dateien und insgesamt 200 MB je Nachricht; Dateiname höchstens 90 Zeichen einschließlich Endung.

## 3. Paketierungsregeln

1. Hauptschriftsatz und sein vollständiger Anlagenbereich werden logisch zusammengehalten.
2. Eine mehrseitige Anlage wird nie zwischen zwei Nachrichten geteilt.
3. Jede Nachricht erhält `Teil X von Y`, den enthaltenen Anlagenbereich und einen Verweis auf die übrigen Teile.
4. Nummernkreis, Dateifolge und Anlagenverzeichnis bleiben über alle Nachrichten lückenlos.
5. Für jede Nachricht wird eine eigene automatisierte Eingangsbestätigung erwartet und geprüft.
6. Ein internes Prüfkonvolut darf erzeugt werden; versandt werden die nach Gerichtshinweis vorgesehenen Einzeldateien.

## 4. Versandplan

| Teil | Hauptdokument | Anlagenbereich | Dateien | Bytes | letzter Hash | Eingangsbestätigung |
| --- | --- | --- | --- | --- | --- | --- |
| 1 von 2 | Schriftsatz | K 1 bis K 28 | Zahl | Zahl | SHA-256 | offen oder geprüft |

Beispiel für den Begleitvermerk:

> Wegen des Datenumfangs wird die Einreichung in zwei unmittelbar aufeinanderfolgenden Nachrichten übermittelt. Diese Nachricht enthält Teil 1 von 2 mit dem Schriftsatz und den Anlagen K 1 bis K 28. Teil 2 von 2 enthält die Anlagen K 29 bis K 47. Der Nummernkreis wird lückenlos fortgeführt.

## 5. Stop-Fehler

- Paketgrenze nur geschätzt statt aus den finalen Dateien berechnet.
- Hauptdokument in einem späteren Teil ohne eindeutigen Bezug.
- Anlage oder Konvolut über zwei Nachrichten aufgespalten.
- Teilnummer im Betreff widerspricht Begleitvermerk.
- Frist wird erledigt, obwohl nur für einen Teil eine positive Eingangsbestätigung vorliegt.

## 6. Output

Liefere Paketierungstabelle, Dateiliste je Teil, fertigen Begleitvermerk, Versandfolge mit Verantwortlichem und eine Eingangskontrollzeile für jede Nachricht. Nutze danach `bea-versandmappe-endfertigung` für die Freigabe.
