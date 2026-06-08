---
name: avv-loeschung-rueckgabe-nach-vertragsende
description: "Pflicht zur Loeschung oder Rueckgabe personenbezogener Daten nach Ende des Auftragsverarbeitungsvertrags gemaess Art. 28 Abs. 3 lit. g DSGVO. Wahlrecht des Verantwortlichen Format und Nachweis Aufbewahrungsausnahmen sowie Backup- und Logfile-Behandlung. Output: Loeschkonzept-Klausel und Loeschprotokoll-Muster."
---

# Loeschung und Rueckgabe nach Vertragsende – Art. 28 Abs. 3 lit. g DSGVO

## Zweck / Purpose

Strukturierung des Endphase-Managements im AVV: Wahlrecht des Verantwortlichen, Formate, Fristen, Nachweise und Aufbewahrungsausnahmen. Purpose (EN): End-of-contract data return and deletion under Article 28 (3) (g) GDPR.

## Wann dieses Modul hilft

- Vertragsende eines AVV steht bevor oder ist eingetreten.
- Es ist zu klaeren, ob Loeschung oder Rueckgabe verlangt wird.
- Gesetzliche Aufbewahrungspflichten kollidieren mit Loeschanforderungen.
- Backups, Logfiles oder forensische Kopien sind zu behandeln.

## Rechtlicher Rahmen

- Art. 28 Abs. 3 lit. g DSGVO: "alle personenbezogenen Daten nach Abschluss der Erbringung der Verarbeitungsleistungen nach Wahl des Verantwortlichen entweder loescht oder zurueckgibt, sofern nicht nach dem Unionsrecht oder dem Recht der Mitgliedstaaten eine Verpflichtung zur Speicherung der personenbezogenen Daten besteht".
- Art. 17 DSGVO: Recht auf Loeschung.
- Art. 5 Abs. 1 lit. e DSGVO: Speicherbegrenzung.
- § 257 HGB, § 147 AO, § 50 BDSG, § 11 BORA – steuer-, handels- und berufsrechtliche Aufbewahrungspflichten.

## Ablauf / Checkliste

1. **Wahlrecht ausueben.**
 - Verantwortlicher entscheidet: Loeschung, Rueckgabe oder eine Kombination (z. B. Rueckgabe aktiver Daten, Loeschung der Kopien).
 - Wahl muss vor Ende der Verarbeitungsleistungen kommuniziert werden – Vertrag sieht typischerweise 30 Kalendertage vor.

2. **Format definieren.**
 - Strukturierte, gaengige und maschinenlesbare Formate (CSV, JSON, XML) analog Art. 20 DSGVO.
 - Verschluesselter Transport.
 - Datentraegerformat oder API-Endpunkt definieren.

3. **Loeschmethodik.**
 - Loeschstandards: DIN 66399, NIST SP 800-88 Rev. 1.
 - Backups: Loeschung in der naechsten regulaeren Backup-Rotation oder gezielte Loeschung.
 - Logfiles: Aufbewahrungspflicht versus Datensparsamkeit abwaegen.

4. **Aufbewahrungsausnahmen.**
 - § 257 HGB, § 147 AO: 10 Jahre, 6 Jahre.
 - § 50 BDSG: bis Zweckerreichung beendet.
 - § 195 BGB i.V.m. § 199 BGB: Verjährungsablauf abwarten.
 - Sicherstellen: Aufbewahrungsdaten sind separiert, zugriffsbeschraenkt und nicht weiter verarbeitet (Sperrung).

5. **Nachweis.**
 - Loeschprotokoll mit Datum, Bestand, Methode, verantwortlicher Person.
 - Unterschrift durch den Auftragsverarbeiter.
 - Bei Sub-AV: Loeschnachweise aller Sub-AV in der Kette.

## Mustertext / Template

Klausel zu Loeschung und Rueckgabe:

> "§ X Beendigung der Verarbeitung
>
> (1) Nach Beendigung der Erbringung der Verarbeitungsleistungen entscheidet der Verantwortliche innerhalb von dreissig (30) Kalendertagen, ob die personenbezogenen Daten zurueckgegeben oder geloescht werden sollen. Der Verantwortliche kann für verschiedene Datenbestaende unterschiedliche Optionen waehlen.
>
> (2) Bei Wahl der Rueckgabe uebergibt der Auftragsverarbeiter die personenbezogenen Daten innerhalb von dreissig (30) Kalendertagen in einem strukturierten, gaengigen und maschinenlesbaren Format an einen vom Verantwortlichen benannten Empfaenger. Die Uebertragung erfolgt verschluesselt nach dem Stand der Technik.
>
> (3) Bei Wahl der Loeschung loescht der Auftragsverarbeiter die personenbezogenen Daten innerhalb von dreissig (30) Kalendertagen vollstaendig und unwiederbringlich. Backups werden in der naechsten regulaeren Backup-Rotation, spaetestens jedoch innerhalb von neunzig (90) Kalendertagen, ueberschrieben oder geloescht. Die Loeschung erfolgt nach DIN 66399 mindestens nach Schutzklasse 2.
>
> (4) Soweit Unionsrecht oder Recht eines Mitgliedstaats die weitere Speicherung der personenbezogenen Daten vorschreibt (insbesondere § 257 HGB, § 147 AO), bleibt der Auftragsverarbeiter berechtigt, die betroffenen Datensaetze für die gesetzliche Aufbewahrungsdauer in einem zugriffsbeschraenkten, ausschliesslich der Erfuellung der gesetzlichen Pflicht dienenden Bereich vorzuhalten. Der Auftragsverarbeiter dokumentiert Datenart, Rechtsgrundlage und Aufbewahrungsdauer und loescht die Daten unverzueglich nach Ablauf der Aufbewahrungspflicht.
>
> (5) Der Auftragsverarbeiter dokumentiert die Loeschung oder Rueckgabe in einem schriftlichen Protokoll, das dem Verantwortlichen innerhalb von zehn (10) Kalendertagen nach Abschluss der Massnahme vorzulegen ist. Das Protokoll enthaelt Datum, Datenarten, Mengenangaben, Loeschmethode und die verantwortliche Person.
>
> (6) Der Auftragsverarbeiter veranlasst, dass jeder Sub-Auftragsverarbeiter die Pflichten aus diesem Paragraphen entsprechend erfuellt und legt dem Verantwortlichen die Loeschnachweise der Sub-Auftragsverarbeiter auf Verlangen vor."

## Typische Drafting-Fehler

- Kein Wahlrecht des Verantwortlichen ("Daten werden geloescht") – das verletzt Art. 28 Abs. 3 lit. g DSGVO.
- Kein definiertes Format der Rueckgabe – faktische Vendor-Lock-in-Wirkung.
- Aufbewahrungspflichten nicht beruecksichtigt – Konflikt mit § 257 HGB, § 147 AO.
- Backups vergessen.
- Kein Loeschprotokoll und kein Nachweis.
- Sub-AV-Kette nicht erfasst.

## Querverweise

- `datenschutzrecht/skills/avv-art-28-mindestinhalte-checkliste/SKILL.md`
- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`
- `datenschutzrecht/skills/avv-pruefung-bestehender-vertraege-audit/SKILL.md`

## Quellen Stand 06/2026

- Art. 28 Abs. 3 lit. g, Art. 17, Art. 5 Abs. 1 lit. e DSGVO.
- § 257 HGB, § 147 AO, § 50 BDSG, § 11 BORA.
- DIN 66399 – Vernichtung von Datentraegern.
- NIST SP 800-88 Rev. 1 – Guidelines for Media Sanitization.
- Zitierweise: `../../../references/zitierweise.md`.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
