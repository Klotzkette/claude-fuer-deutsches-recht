---
name: aktenbestand-pflege-bea-versand
description: "Aktenbestand Pflege BEA Versand: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aktenbestand Pflege BEA Versand

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Aktenbestand Pflege BEA Versand** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50 BRAO sechs Jahre nach Mandatsende) Wiedervorlagen. Monatliche und jaehrliche Auswertung Aktenanzahl je Anwalt. Markiert lange ruhende Mandate zur Klaerung. Verhindert Datenlecks bei abgeschlossenen Mandaten (DSGVO Art. 5 Speicherbegrenzung). |
| `bea-versand-pruefen` | Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers) oder qualifizierte elektronische Signatur (qeS). Prüft Versand-Quittung Eingangsbestätigung und Verwertbarkeit für Fristnachweis. Hinweis Wiedereinsetzung bei beA-Stoerung mit Glaubhaftmachung. Pflichtschritt bei elektronischem Versand an Gerichte und Behoerden. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Aktenbestand Pflege BEA Versand**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aktenbestand-pflege`

**Fokus:** Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50 BRAO sechs Jahre nach Mandatsende) Wiedervorlagen. Monatliche und jaehrliche Auswertung Aktenanzahl je Anwalt. Markiert lange ruhende Mandate zur Klaerung. Verhindert Datenlecks bei abgeschlossenen Mandaten (DSGVO Art. 5 Speicherbegrenzung).

# Aktenbestandspflege

## Aktenstatus

| Status | Bedeutung |
|---|---|
| **laufend** | aktive Bearbeitung |
| **ruhend** | wartet auf Reaktion Gegenseite Behörde oder Mandant |
| **abgeschlossen** | Mandat beendet — Schlussrechnung gestellt |
| **archiviert** | im Archiv abgelegt — Zugriff nur für Aufbewahrung |
| **vernichtet** | nach Ablauf der Aufbewahrungsfrist vernichtet (Audit-Eintrag) |

## Wartung pro Akte

```yaml
mandat-az: 2026/0042
status: laufend
letztes-ereignis: 2026-05-20 — Versand Berufung
letzte-pflege: 2026-05-21
naechstes-ereignis-erwartet: 2026-06-20 (Berufungsbegründungsfrist)
ruhend-seit: null
abgeschlossen-am: null
abgeschlossen-begruendung: null
archivierung-faellig: null # bei Abschluss berechnen: + 6 Jahre § 50 BRAO
vernichtung-faellig: null # 6 Jahre nach Mandatsende
```

## Mandatsende

Bei Abschluss:

1. **Schlussrechnung** über Skill `rechnungserstellung-rvg`.
2. **Aktenherausgabe** an Mandanten falls gewünscht (Originalbelege Restmaterial — Akteneinsichtsrecht des Mandanten § 50 Abs. 5 BRAO).
3. **Aufbewahrungspflicht** sechs Jahre nach Mandatsende (§ 50 Abs. 1 BRAO).
4. **Status** auf `abgeschlossen` setzen.
5. **Archivierungsdatum** und **Vernichtungsdatum** berechnen.

## Wiedervorlagen

Pro Akte: Wiedervorlagedatum erfassen — z. B. bei ruhenden Mandaten ein Drei-Monats-Check ob das Mandat noch aktuell ist.

## Lange ruhende Mandate

Skript prüft alle drei Monate:

- Welche Mandate sind seit mehr als sechs Monaten in Status `ruhend`?
- Liste an zuständigen Anwalt — Klärung ob Mandat weiter offen ist abgeschlossen werden kann oder vergessen wurde.

## Datenschutz und Löschung

- **Aufbewahrungsfrist** § 50 Abs. 1 BRAO sechs Jahre nach Mandatsende.
- **Steuerlich** § 147 AO bei Buchhaltungsunterlagen acht oder zehn Jahre.
- **Nach Ablauf** vernichten — physisch durch Aktenvernichter oder digital durch sicheres Löschen.
- **DSGVO Art. 5 Abs. 1 lit. e** Speicherbegrenzung: Daten nicht laenger als notwendig.

## Auswertung

### Monatlich

| Anwalt | Laufende Akten | Neu | Abgeschlossen |
|---|---|---|---|
| ... | ... | ... | ... |

### Jaehrlich

- Aktenanzahl gesamt
- Aktenverteilung nach Rechtsgebieten
- Durchschnittliche Mandatsdauer
- Schwellen: Wenn ein Anwalt mehr als X laufende Akten hat — Auslastungsalarm.

## Archivierung

- Physisch: Archivraum mit beschrifteten Aktenkartons (Az Jahr Mandant Vernichtungsdatum).
- Digital: separates Archiv-Verzeichnis `_archiv/` mit eingeschraenkten Zugriffsrechten.

## Audit-Trail

- Statusänderungen mit Datum und ausführender Person.
- Archivierung und Vernichtung mit Audit-Eintrag.

## Ausgabe

- Aktualisierter Aktenbestand.
- Monatlicher und jaehrlicher Report.
- Liste lang ruhender Mandate zur Klärung.
- Wiedervorlagen-Einträge im Tagesbrief.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `bea-versand-pruefen`

**Fokus:** Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers) oder qualifizierte elektronische Signatur (qeS). Prüft Versand-Quittung Eingangsbestätigung und Verwertbarkeit für Fristnachweis. Hinweis Wiedereinsetzung bei beA-Stoerung mit Glaubhaftmachung. Pflichtschritt bei elektronischem Versand an Gerichte und Behoerden.

# beA-Versand prüfen


## Triage zu Beginn
1. Ueber welchen Versandweg soll der Schriftsatz eingereicht werden: sUW (persoenliches Versenden des Inhabers) oder qeS (qualifizierte elektronische Signatur)?
2. Liegt eine beA-Versandquittung oder Eingangsbestaetigung vor, die die Fristwahrung belegt?
3. Gibt es Anzeichen fuer eine beA-Stoerung oder technische Uebermittlungspanne (§ 130a Abs. 6 ZPO Wiedereinsetzung)?
4. Muss ein elektronisches Empfangsbekenntnis (EB) erteilt werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 130a ZPO — Elektronische Einreichung Zivilprozess; sUW oder qeS als Pflichtalternativen
- § 31a BRAO — beA-Nutzungspflicht fuer alle zugelassenen Rechtsanwaelte
- § 12 ERVV — Technische Anforderungen an den elektronischen Rechtsverkehr
- § 130a Abs. 6 ZPO — Wiedereinsetzung bei nachgewiesener technischer Stoerung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Rechtsgrundlagen

- **§ 31a BRAO** beA-Pflicht für Rechtsanwälte.
- **§ 130a ZPO** elektronische Einreichung Zivilprozess.
- **§ 32d StPO** elektronische Einreichung Strafprozess.
- **§ 65d SGG** Sozialgerichtsverfahren.
- **§ 55a VwGO** Verwaltungsgerichtsverfahren.
- **§ 52d FGO** Finanzgerichtsverfahren.
- **§ 12 ERVV** Elektronischer-Rechtsverkehr-Verordnung.

## Zwei zulässige Versandwege

### 1. Sicherer Übermittlungsweg (sUW)

- Versand erfolgt persönlich durch den beA-Inhaber.
- Anmeldung mit beA-Karte und PIN.
- Keine qualifizierte elektronische Signatur erforderlich am einzelnen Schriftsatz.
- Signatur durch sUW gilt als ausreichend (§ 130a Abs. 3 Satz 1 Var. 2 ZPO).

### 2. Qualifizierte elektronische Signatur (qeS)

- Schriftsatz wird mit qeS unterzeichnet.
- Versand durch eine andere Person (z. B. Sekretariat) zulässig.
- qeS muss vom Anwalt mit beA-Karte erstellt sein.

## Pflichtprüfung

### Vor Versand

- [ ] Schriftsatz unterzeichnet durch qeS **oder** Versand durch den beA-Inhaber selbst (sUW)?
- [ ] Empfänger über das beA-Adressbuch identifiziert (SAFE-ID)?
- [ ] PDF im Format PDF/A oder Standard-PDF (lesbar)?
- [ ] Anlagen als einzelne PDF oder im Hauptdokument eingebunden?
- [ ] Gesamtnachrichtgroesse unter beA-Limit (200 MB; bei sehr großen Anlagen sequenziell)?

### Nach Versand

- [ ] **Versandbestätigung** des beA-Systems gespeichert?
- [ ] **Eingangsbestätigung** des Empfangsgerichts / der Empfangsbehörde liegt vor?
- [ ] Zeitstempel auf der Quittung passt zum Versand?
- [ ] Bei Fristsache: Quittung **vor** Fristablauf erzeugt?

## Quittungsformate

Das beA gibt zwei Quittungen:

1. **Sendebericht** der eigenen beA-Anwendung — Zeitpunkt der erfolgreichen Übertragung an den Server.
2. **Eingangsbestätigung** des Empfängers (Gericht) — bestätigt Eingang in der Posteingangsstelle.

Beide gehören in die Mandatsakte unter `mandate/<az>/03_schriftsaetze/<datum>-bea-quittung.pdf`.

## Fristnachweis

- **Eingang beim Gericht** bestimmt Fristwahrung (§ 130a Abs. 5 ZPO Eingang in die für das Gericht bestimmte Posteingangsstelle).
- **Eigene Sendebestätigung allein** reicht nicht — entscheidend ist die Eingangsbestätigung beim Empfänger.

## Störung des beA

- **Störungsdokumentation** Screenshot Fehlermeldung Datum Uhrzeit.
- **Ersatzeinreichung** schriftlich + qeS gemäß § 130d Satz 3 ZPO.
- **Glaubhaftmachung** der Störung unverzueglich nach Wegfall (§ 130d Satz 2 ZPO iVm § 67 SGG analog).
- **Wiedereinsetzung** § 233 ZPO bei unverschuldetem Fristversäumnis.

## Audit

- Eintrag im `versand-audit.jsonl`.
- Quittungs-PDFs gesichert.
- Verbindung zum Fristenbuch (Fristerledigung markiert).

## Sonderfälle

### Mehrere Anlagen

- Inhaltsverzeichnis der Nachricht klar (Hauptschriftsatz + Anlagen K1 K2 ...).
- Anlagen einzeln als PDF oder im Konvolut — je nach Gerichtspraxis.

### Empfänger ohne beA

- Wenn die Empfänger-Behörde noch nicht über beA / EGVP erreichbar: Postversand mit qualifizierter Bestätigung (Bote Einschreiben).
- Bei Gerichten in Deutschland generell EGVP-Eingang vorhanden — Prüfung im beA-Adressbuch.

### RA-zu-RA

- Versand an gegnerischen Anwalt über beA ist zulässig.
- Nicht Pflicht (§ 14 BORA gilt für Pflichten zwischen Anwälten; beA-Pflicht ist nur ggu. Gerichten und Behörden).

## Ausgabe

- Eintrag im `versand-audit.jsonl`.
- Quittungen unter Mandatsakte.
- Bei Störung: Störungsdokumentation als PDF.
