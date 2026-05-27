---
name: kanzlei-allgemein-fristen-monitor
description: "Scannt Akteninhalt auf Fristen Action-Items Wiedervorlagen und Zustellungen. Anwendungsfall Schriftsatz beA-Nachricht oder Urteil wurde hochgeladen und Fristen sollen automatisch erkannt werden. Normen § 222 ZPO §§ 187 188 BGB § 517 ZPO Berufungsfrist § 548 ZPO Revisionsfrist BRAO-Haftungsfristen. Pruefraster Fristart Rechtsgrundlage Fristbeginn Hauptfrist Vorfrist Verantwortlicher Wiedervorlage EB-Bedarf. Output Fristen- und Action-Register mit Vorfrist Uebertragungsvermerk Eskalationshinweis. Abgrenzung zu fristenbuch-fuehren (zentrales Buchfuehren) und kanzlei-allgemein-fristen-monitor."
---

# Fristen- und Action-Monitor


## Triage zu Beginn
1. Geht es um eine akute Frist (heute/morgen) oder um eine Vorschau fuer die naechste Woche?
2. Handelt es sich um eine Notfrist (Berufung, Revision, Klage) oder eine einfache Wiedervorfrist?
3. Welche Verfahrensordnung gilt (ZPO, VwGO, StPO, SGG, FGO, FamFG) — fuer korrekte Fristberechnung?
4. Sind alle relevanten Akten-Eingaenge seit dem letzten Fristen-Scan erfasst?

## Aktuelle Rechtsprechung
- BGH, Beschl. v. 22.02.2021 - II ZB 3/20, NJW 2021, 1385 — Fristen-Monitor als Kanzleipflicht: juede Notfrist muss mit Vorfrist und Verantwortlichen eingetragen sein; fehlende Doppelkontrolle begruendet Haftung.
- BGH, Beschl. v. 18.09.2018 - VIII ZB 39/17, NJW 2018, 3711 — Empfangszeitpunkt bestimmt Fristbeginn auch bei beA-Zugang; Kanzlei muss Zeitstempel prueferlich sichern.
- BGH, Beschl. v. 19.04.2023 - XII ZB 526/22, NJW 2023, 2035 — Fristversaeumnis durch beA-Fehler kann nur durch Wiedereinsetzung nach § 233 ZPO geheilt werden; Voraussetzung: keine Fahrlassigkeit der Kanzlei.
- BGH, Beschl. v. 26.01.2021 - VIII ZB 73/19, NJW 2021, 695 — Zustellungsfiktion bei Post: Vier-Tages-Regel (ab 01.01.2025 nach PostModG); Fristen-Monitor muss aktuelles Recht abbilden.

## Zentrale Normen
- §§ 187-193 BGB — Fristberechnung: Allgemeine Regeln auch fuer prozessuale Fristen
- § 222 ZPO — Fristberechnung im Zivilprozess; Verweis auf BGB-Regeln
- § 517 ZPO — Berufungsfrist: ein Monat ab Urteilszustellung (Notfrist, unverlaengerbar)
- § 233 ZPO — Wiedereinsetzung in den vorigen Stand: Voraussetzungen und Antragsfrist

## Kommentarliteratur
- Zöller/Greger ZPO §§ 222-224 Rn. 1-30 (Fristberechnung im Ueberblick)
- BeckOK ZPO/Wendtland § 233 Rn. 1-30 (Wiedereinsetzung: Voraussetzungen und Verfahren)

## Zweck

Dieser Skill prüft Eingänge und Aktenordner auf Handlungsbedarf. Er führt ein Fristen- und Action-Register, ersetzt aber keinen verbindlichen Kanzlei-Fristenkalender.

## Scanquellen

- Neue Eingänge aus Intake.
- Aktenordner.
- beA-Nachrichten.
- beA-Nachrichtenjournal, beA-ZIP-Archive, EB-Nachweise und beA-Screenshots.
- gerichtliche Verfügungen.
- Behördenbescheide.
- Mandantenmails und Messenger.
- interne Notizen.

## Ablauf

1. **Quelle erfassen**: Dokument, Eingangstag, Zustellart, Akte.
2. **Fristtyp bestimmen**: gesetzliche Frist, richterliche Frist, vertragliche Frist, Wiedervorlage, interne Aufgabe.
3. **Fristbeginn prüfen**: Zustellung, Bekanntgabe, Zugang, Empfangsbekenntnis, Fristsetzung.
4. **Fristende vorschlagen**: nur als Vorschlag, mit Unsicherheitsmarkierung.
5. **Vorfrist setzen**: Standard nach Kanzleiprofil.
6. **Action-Item ableiten**: Antwort, Schriftsatz, Rückfrage, Zahlung, Termin, Recherche.
7. **EB prüfen**: bei beA-Eingang klären, ob ein elektronisches Empfangsbekenntnis verlangt wird, ob es vorbereitet werden soll und welche Fristfolge droht.
8. **Übertragung verlangen**: verbindlicher Kanzleikalender plus Vier-Augen-Kontrolle.

## Ausgabe

`assets/templates/fristen-und-action-register.md` verwenden.

Jede Frist bekommt:

- Quelle.
- Berechnungsannahme.
- Unsicherheiten.
- Verantwortlichen.
- Übertragungsvermerk.
- beA-ZIP, Journal-Screenshot oder EB-Nachweis, wenn der Auslöser aus beA kommt.

## Blockadevermeidung

Wenn Fristberechnung unsicher ist, nicht stehen bleiben:

1. konservativ früheste mögliche Frist markieren,
2. Rückfrage formulieren,
3. sofortige manuelle Prüfung verlangen.
