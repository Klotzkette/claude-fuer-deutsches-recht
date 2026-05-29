---
name: kanzlei-allgemein-output-versand
description: "Steuert Output und Versand für Schriftsatz Brief E-Mail Fax beA SMS Messenger Teams und Mandantenportal. Fragt vor beA-Versand ausdrücklich nach Freigabe warnt vor PIN Token und Geheimnissen und dokumentiert Journal Screenshot ZIP-Archiv Anlagen Frist und Protokoll."
---

# Output und Versandsteuerung


## Triage zu Beginn
1. Welcher Versandkanal ist fuer diesen Ausgang vorgesehen: beA, Brief, Fax, E-Mail, Mandantenportal?
2. Ist der Entwurf vom Anwalt freigegeben (persoenliche Freigabe Pflicht bei beA-Versand)?
3. Wurde der Versand-Vor-Check bereits durchgefuehrt (Dokument, Unterschrift, Adressat, Anlagen)?
4. Ist ein fristgebundenes Dokument dabei, das sofort nach Versand ins Fristenbuch muss?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 130a ZPO — Elektronisches Dokument: Anforderungen an Inhalt und Uebermittlungsweg
- § 174 ZPO — Zustellungen von Anwalt zu Anwalt: Empfangsbekenntnis und Fristen
- § 43 BRAO — Sorgfaltspflicht: umfasst Pruefung vor Ausgang
- § 31a BRAO — beA-Nutzungspflicht: persoenlicher Versand durch Inhaber

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt vom Entwurf zum kontrollierten Ausgang. Er versendet nicht still. Jeder Versand braucht eine ausdrückliche Einzelentscheidung.

## Output-Kanäle

- beA.
- Brief.
- Fax.
- E-Mail.
- SMS, iMessage, WhatsApp, Telegram, Teams.
- Mandantenportal.
- interner Vermerk.

## Ablauf

1. Akte und Empfänger bestätigen.
2. Dokumentfassung bestimmen.
3. Anlagenliste prüfen.
4. Signatur und Vollmacht prüfen.
5. Fristbezug prüfen.
6. Versandweg wählen.
7. Sicherheitscheck durchführen.
8. Freigabe abfragen.
9. Versandprotokoll erzeugen.

Wenn der Text aus dem Schreib-Canvas kommt und juristisch noch unsubstantiiert wirkt, vor Versand `kanzlei-allgemein-freundlicher-copilot`, `kanzlei-allgemein-schreibcanvas` und `kanzlei-allgemein-qualitaetsgate-hardening` einschalten. Keine schwachen Schriftsätze wegen eines Versandwunsches ungeprüft durchreichen.

Bei Klage, Replik oder gerichtlichem Antrag vor Versand zusätzlich `kanzlei-allgemein-schriftsatz-turbo` und das Anlagenverzeichnis prüfen.

## beA-Sonderregeln

Vor beA-Versand immer ausgeben:

> beA-Sicherheitswarnung: Software-Token, Zertifikatsdatei, PIN und Passwörter nicht in den Chat eingeben und nicht speichern. PIN nur in der lokalen beA-Komponente eingeben. Versand nur nach Prüfung von Empfänger, Akte, Schriftsatzfassung, Anlagen, Signatur und Frist.

Wenn der Nutzer fragt, ob das System beA versenden soll:

1. Technische Umgebung klären.
2. Versandberechtigung klären.
3. Darauf hinweisen, dass der sichere Übermittlungsweg und die Berufsträgerverantwortung beim Nutzer bleiben.
4. Keine Zugangsdaten entgegennehmen.
5. Versand nur vorbereiten oder nach lokalem, bestätigtem Tool-Aufruf protokollieren.

Nach jedem technisch bestätigten beA-Versand immer `kanzlei-allgemein-bea-journal` ausführen oder anbieten:

1. Gesendet- oder Ausgangsjournal öffnen und einsehen.
2. Nachrichtenjournal oder Versandstatus als Screenshot sichern.
3. Versandte beA-Nachricht als ZIP-Archiv herunterladen oder exportieren.
4. ZIP-Archiv entpacken und Schriftsatzfassung, Anlagen, Empfänger, Zeitpunkt und Versandstatus abgleichen.
5. Versandnachweis und entpackten Ablagepfad in `assets/templates/output-versandprotokoll.md` dokumentieren.
6. Fristen- oder EB-Folgen an `kanzlei-allgemein-fristen-monitor` übergeben.

Wenn kein technischer Zugriff möglich ist, eine Checkliste ausgeben und den Nutzer bitten, Journal-Screenshot, Versand-ZIP und Versandnachweis hochzuladen.

## Messenger-Ausgang

Messenger nur für geeignete Inhalte nutzen. Bei Fristen, vertraulichen Dokumenten, sensiblen Daten oder unklarer Identität sichere Kanäle bevorzugen.

## Ausgabe

`assets/templates/output-versandprotokoll.md` verwenden.
