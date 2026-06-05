---
name: versand-check-weihnachtskarten
description: "Versand Check Weihnachtskarten: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versand Check Weihnachtskarten

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Versand Check Weihnachtskarten** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versand-vor-check` | Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhaendig oder qualifizierte elektronische Signatur?) Adressat (richtiges Gericht / Behoerde / Mandant? richtige Adresse beA-SAFE-ID EGVP-Adresse?) Anlagen (vollständig? im Inhaltsverzeichnis aufgeführt? Sigel richtig?) Versandweg (Post / beA / EGVP / E-Mail / De-Mail). Versandquittung sichern. Audit-Eintrag. Bei Mangel Versand sperren. |
| `weihnachtskarten` | Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persoenlich. Druckliste für Postversand inkl Adressetiketten und Frankierhinweis. Versandzeitraum (vor Weihnachten) und Erinnerungen. Datenschutz Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Mandantenpflege; Widerspruchsrecht. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Versand Check Weihnachtskarten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versand-vor-check`

**Fokus:** Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhaendig oder qualifizierte elektronische Signatur?) Adressat (richtiges Gericht / Behoerde / Mandant? richtige Adresse beA-SAFE-ID EGVP-Adresse?) Anlagen (vollständig? im Inhaltsverzeichnis aufgeführt? Sigel richtig?) Versandweg (Post / beA / EGVP / E-Mail / De-Mail). Versandquittung sichern. Audit-Eintrag. Bei Mangel Versand sperren.

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

## 2. `weihnachtskarten`

**Fokus:** Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persoenlich. Druckliste für Postversand inkl Adressetiketten und Frankierhinweis. Versandzeitraum (vor Weihnachten) und Erinnerungen. Datenschutz Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Mandantenpflege; Widerspruchsrecht.

# Weihnachtskarten Mandantenpflege


## Triage zu Beginn
1. Wann soll der Versand beginnen und soll postalisch, digital oder beides versandt werden?
2. Sind alle Empfaenger datenschutzrechtlich geprueft (Einwilligung oder berechtigtes Interesse, Art. 6 Abs. 1 lit. f DSGVO)?
3. Gibt es Widersprueche (Art. 21 DSGVO) von einzelnen Empfaengern, die aus dem Verteiler zu loeschen sind?
4. Welche Anredeform und welcher Ton soll verwendet werden: formell-zurueckhaltend, warm-persoenlich oder neutral?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse als Rechtsgrundlage fuer Mandanten-Karten
- Art. 21 Abs. 2 DSGVO — Widerspruchsrecht bei Direktmarketing: sofortige Wirkung
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit im Kartenverteiler
- § 7 UWG — Unzumutbare Belaestigung: E-Mail ohne klare Einwilligung bei Verbrauchern riskant

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verteilerpflege

```yaml
- name: Mueller, Hans
 anrede: foermlich
 empfaenger: Mueller GmbH (zu Hd. Hans Mueller)
 anschrift: ...
 e-mail: hmueller@mueller-gmbh.de
 versandweg: digital # digital / post / beides
 beziehung: Mandant Aktenkreis 2026/0042
 ton: warm-foermlich
 letzte-karte: 2025-12-15
 widerspruch: false
```

## Texte

### Förmlich-zurückhaltend (Mandanten gemischter Branchen)

```
Sehr geehrter Herr [Nachname],

zum Ende dieses Jahres moechte ich Ihnen für die vertrauensvolle
Zusammenarbeit danken. Ich wünsche Ihnen ruhige besinnliche Feiertage
einen guten Übergang ins neue Jahr und vor allem Gesundheit.

Mit freundlichen Grüßen

[Anwalt]
Kanzlei XYZ
```

### Warm (langjaehrige Geschäftspartner Kollegen)

```
Liebe(r) [Vorname],

am Ende eines arbeitsreichen Jahres ein herzliches Dankeschoen für die
gute Zusammenarbeit. Ich wünsche Ihnen besinnliche Festtage einen
guten Rutsch und ein gesundes glückliches neues Jahr.

Beste Grüße
[Anwalt]
```

### Persönlich (engster Kreis)

Individuell formuliert — kein Templating; auf der persönlichen Beziehung aufbauend.

## Versandformen

### Postversand

- **Karten** mit handgeschriebener Unterschrift Pflicht.
- **Druckliste** für Adressetiketten oder Briefumschlag-Druck.
- **Frankierung** als Standardbrief oder Postkarte.
- **Versandzeitraum** zweite Dezemberwoche damit vor Weihnachten ankommt.

### Digitaler Versand

- **E-Mail** mit kurzer persönlicher Anrede.
- **Anhang** optional als PDF-Karte (Briefkopf der Kanzlei).
- **Versandzeitraum** kurz vor Weihnachten (z. B. 22./23. Dezember).
- **Massenversand vermeiden** — pro Empfänger einzeln im Bcc nicht zulässig wegen DSGVO; lieber serienmaessig versenden.

### Hybrid

- Engste Mandanten und Partner Postkarte plus zusätzlich kurze E-Mail.
- Sonstige nur digital.

## Druckliste für Postversand

CSV mit Spalten: Name Anschrift Stadt PLZ Land Ansprache.

## Versandkontrolle

- **Doppelversand** vermeiden (mit `letzte-karte`-Eintrag).
- **Verstorbene Empfänger** entfernen.
- **Mandate beendet im Streit** ggf. entfernen.
- **Widerspruch** dauerhaft beachten.

## Datenschutz

- Erläuterung im Mandantenintake auf mögliche Weihnachtsgrüße.
- Widerspruchsrecht jederzeit möglich (Art. 21 DSGVO).
- Löschung auf Widerspruch (Art. 17 DSGVO).

## Ausgabe

- Aktualisierter Verteiler.
- Druckliste (CSV).
- E-Mail-Entwuerfe zur Freigabe.
- Audit mit Versanddatum pro Empfänger.
