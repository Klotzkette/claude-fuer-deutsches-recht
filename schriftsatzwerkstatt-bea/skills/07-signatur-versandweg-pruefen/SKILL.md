---
name: 07-signatur-versandweg-pruefen
description: "Vor beA-Versand bei einfacher Signatur, qeS, Vertretung oder Mitarbeiterzugang: prüft verantwortliche Person, tatsächlichen Versender, Berechtigung und Signaturbezug zur finalen PDF. Kontrolliert bei einfacher Signatur den persönlichen Versand durch die verantwortliche Person. Liefert Prüfmatrix und konkrete Stopps."
---

# Signatur und tatsächlichen Versandweg prüfen

## Zweck und Anwendungsfall

Dieser Skill entscheidet nicht über den Schriftsatzinhalt. Er verhindert, dass ein technisch fertiges Paket mit unpassender Signatur-/Versenderkonstellation übergeben wird.

## Eingaben

- finale Hauptschriftsatz-PDF und deren Hash.
- Name und Funktion der verantwortlichen Person.
- Name der Person, die den Versand tatsächlich auslösen soll.
- Signaturmodell: qeS oder einfache Signatur plus sicherer Übermittlungsweg.
- verwendetes Postfach und organisatorische Versandberechtigung.

## Ablauf / Checkliste

1. Verantwortliche Person und tatsächlichen Versender getrennt abfragen; keine Identität unterstellen.
2. **Einfache Signatur:** Prüfen, ob der Name der verantwortlichen Person am Ende des Schriftsatzes lesbar wiedergegeben und eindeutig zugeordnet ist. Eine Unterschriftsgrafik wird nicht ohne diesen Namens- und Zuordnungsabgleich freigegeben.
3. Bei einfacher Signatur muss genau diese verantwortliche Person den Versand persönlich über ihren sicheren Übermittlungsweg auslösen. Ist eine andere Person vorgesehen, rot stoppen.
4. **qeS:** Prüfen, ob die qualifizierte elektronische Signatur von der verantwortlichen Person stammt, gültig prüfbar ist und exakt die finale Hauptschriftsatz-PDF erfasst. Keine gemeinsame qeS für mehrere elektronische Dokumente oder ein Anlagenpaket verwenden. Bei eingebettetem PAdES bleibt die PDF allein. Eine abgesetzte CAdES-Datei mit `.p7`, `.p7s`, `.p7m` oder `.pkcs7` weder vorab erfinden noch umbenennen; Ziel-PDF, Zielhash, Signaturhash, Bytes, Unterzeichner und grünes Prüfprotokoll im `signaturmanifest.csv` festhalten.
5. Bei qeS darf die technisch übermittelnde Person nur im Rahmen ihrer realen Berechtigung handeln. Berechtigung nicht erfinden oder selbst erteilen.
6. Anlagen brauchen keine eigene Signatur, wenn sie dem formgerechten Schriftsatz beigefügt werden. Vorhandene Signaturen in Anlagen trotzdem dokumentieren und schützen.
7. Jede Änderung der Haupt-PDF nach Signatur hebt Signaturstatus und Paketfreigabe auf.
8. Postfach, Gericht/SAFE-Empfänger, Aktenzeichen oder `Neueingang`, ein Verfahren je Nachricht und Betreff erfassen.
9. Ergebnis als klare Matrix `grün`, `gelb` oder `rot` ausgeben. Bei rot den genauen Korrekturweg nennen: identischer persönlicher Versand, qeS oder verantwortliche anwaltliche Klärung.
10. Das Plugin meldet sich niemals selbst im beA an und löst keinen Versand aus.

## Quellenpflicht

Die Signaturalternativen stehen im [ERV-Versandstandard](../../references/erv-versandstandard.md) mit Verweis auf § 130a ZPO; Versions- und Hashbindung folgen [Inhaltstreue und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md), die personengebundenen Stopps dem [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Es werden keine Rechtsprechungsanker verwendet.

## Ausgabeformat

| Prüfung | Ergebnis | Nachweis | Folge |
|---|---|---|---|
| verantwortliche Person | [Name] | Schriftsatz/Freigabe | weiter |
| tatsächlicher Versender | [Name] | Versandauftrag | weiter/rot |
| Signaturmodell | einfach/qeS | PDF/Signaturprüfung | weiter/rot |
| Identität bei einfacher Signatur | ja/nein | Namensabgleich | grün/rot |

Zusätzlich wird eine ausformulierte Versandwegentscheidung erzeugt. Das Ergebnis darf keine Person als versandberechtigt oder freigebend erfinden.

## Beispiele

- Anwältin A ist einfach signiert und versendet selbst aus ihrem beA: freigabefähig.
- Anwältin A ist einfach signiert, Mitarbeiter B soll senden: rot; qeS von A oder persönlicher Versand durch A.
- qeS gehört zu einer früheren PDF-Version: rot; finale PDF erneut signieren und Hash aktualisieren.
