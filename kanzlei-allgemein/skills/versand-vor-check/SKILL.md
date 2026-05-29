---
name: versand-vor-check
description: Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhaendig oder qualifizierte elektronische Signatur?) Adressat (richtiges Gericht / Behoerde / Mandant? richtige Adresse beA-SAFE-ID EGVP-Adresse?) Anlagen (vollständig? im Inhaltsverzeichnis aufgeführt? Sigel richtig?) Versandweg (Post / beA / EGVP / E-Mail / De-Mail). Versandquittung sichern. Audit-Eintrag. Bei Mangel Versand sperren.
---

# Versand-Vor-Check (Pflicht vor jedem Versand)


## Triage zu Beginn
1. Was ist der Versandkanal: beA (sUW oder qeS), Brief, Fax, E-Mail, EGVP?
2. Ist das Dokument das aktuelle und vollstaendige Exemplar (Stand, Aktenzeichen, Unterschrift geprueft)?
3. Stimmt der Adressat mit dem im Schriftsatz genannten Gericht oder Empfaenger ueberein?
4. Sind alle angekuendigten Anlagen beigefuegt und im Inhaltsverzeichnis aufgefuehrt?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 130 Nr. 6 ZPO — Schriftsatz muss Unterschrift des Anwalts tragen
- § 130a ZPO — Elektronisches Dokument: sUW oder qeS als Pflichtanforderung
- § 253 Abs. 4 ZPO — Anlagen sind dem Schriftsatz beizufuegen
- § 43 BRAO — Sorgfaltspflicht: Versand-Vor-Check als anwaltliche Pflicht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflicht

Jeder ausgehende Versand der Kanzlei muss diesen Check durchlaufen. Fehlversand ist anwaltliche Pflichtverletzung mit Haftungsrisiko.

## Prüfraster

### 1. Dokumentidentität

- [ ] Ist es das richtige PDF / DOCX?
- [ ] Hat das Dokument den aktuellen Stand (Datum im Briefkopf passt zum Versand)?
- [ ] Aktenzeichen der Kanzlei korrekt?
- [ ] Aktenzeichen / Az des Empfangsgerichts / der Empfangsbehörde korrekt?
- [ ] Streitwert / Gegenstandswert korrekt?

### 2. Unterschrift

- [ ] Eigenhaendige Unterschrift (Original) bei Papierversand?
- [ ] Bei beA-Versand: qualifizierte elektronische Signatur (qeS) **oder** sicherer Übermittlungsweg (sUW) durch persönliches Versenden des beA-Inhabers?
- [ ] Ist die unterzeichnende Person berechtigt (Anwalt der Kanzlei mit Vollmacht in der Akte)?
- [ ] Bei Sozietät: korrekt für die Sozietät unterzeichnet oder mit "i. A." / "i. V."?

### 3. Adressat

- [ ] Richtige Behörde / Gericht?
- [ ] Korrekte Anschrift?
- [ ] beA-SAFE-ID des Empfängers korrekt (RA-zu-RA-Versand und Gericht)?
- [ ] EGVP-Adresse der Behörde korrekt?
- [ ] Aktenzeichen des Empfängers im Schreiben?

### 4. Anlagen

- [ ] Anlagenverzeichnis vorhanden mit Sigel (K1 K2 ...)?
- [ ] Jede Anlage im Schriftsatz zitiert?
- [ ] Jede Anlage tatsächlich im Konvolut?
- [ ] Reihenfolge richtig?
- [ ] Sigel-Stempel auf erster Seite jeder Anlage?
- [ ] Schwaerzungen Dritter-Daten erfolgt wo erforderlich (DSGVO Datenminimierung)?

### 5. Versandweg und Form

- [ ] **beA** für Versand an Gericht und Behörde durch RA (Pflicht § 31a BRAO § 130d ZPO und entsprechend in den anderen Verfahrensordnungen).
- [ ] **EGVP** als alternative Schnittstelle für Behörde.
- [ ] **Post** als Rückfalloption (Mandantenkommunikation; wenn Empfänger kein beA hat).
- [ ] **E-Mail** an Mandant — Verschlüsselung Schutz der Mandanteninhalte (BRAO Berufsrecht).

### 6. Versandquittung

- [ ] beA-Eingangsbestätigung gesichert (PDF speichern unter `mandate/<az>/03_schriftsaetze/<datum>-versand-quittung.pdf`)?
- [ ] EGVP-Eingangsbestätigung gesichert?
- [ ] Post: Einschreiben mit Rückschein oder Bote-Protokoll?

### 7. Fristenbuch

- [ ] Fristerledigung im Fristenbuch eingetragen?
- [ ] Folge-Fristen (z. B. Reaktionsfrist Gegenseite) eingetragen?

### 8. Postausgangsbuch

- [ ] Eintrag im Postausgangsbuch (Skill `posteingang-ausgang`)?

## Sperrregel

Wenn ein Pflicht-Pruefpunkt offen ist: Versand sperren. Eskalation an zuständigen Anwalt.

## Audit-Eintrag

Pro Versand ein Audit-Eintrag:

```yaml
versand-id: V-2026-00123
mandat-az: 2026/0042
datum: 2026-05-20
empfaenger: Amtsgericht München
versandweg: beA
dokument: klage-2026-0042.pdf
unterzeichnet-von: RA Mueller
checks-bestanden:
  - dokumentidentitaet: ok
  - unterschrift: ok-qes
  - adressat: ok-bea-safe-id-bestätigt
  - anlagen: ok-vollständig
  - versandweg: bea
  - quittung: gesichert
freigegeben-von: RA Mueller
versand-zeit: 2026-05-20T11:23:45
quittung-pdf: mandate/2026-0042/03_schriftsaetze/2026-05-20-versand-quittung.pdf
```

## Sonderfälle

### beA-Störung

- Bei Störung des beA-Systems: Glaubhaftmachung der Störung mit Screenshot + Fehlermeldung; Ersatzeinreichung schriftlich + qeS.
- Störungsdokumentation in Audit.

### Wochenende / Feiertag

- Prüfung der Fristen vor Versand (auf nächsten Werktag verschoben?).

### Eilversand

- Bei Eilversand am Tag der Fristerledigung: zusätzlich telefonische Kontrolle des Eingangs beim Gericht.

## Ausgabe

- Versand-Audit-Eintrag in `versand-audit.jsonl` (append-only).
- Quittungs-PDF unter Mandatsakte.
- Bestätigung an Anwalt und Sekretariat.
