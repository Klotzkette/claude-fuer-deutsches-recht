---
name: bea-versand-pruefen
description: Prueft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Uebermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers) oder qualifizierte elektronische Signatur (qeS). Prueft Versand-Quittung Eingangsbestaetigung und Verwertbarkeit fuer Fristnachweis. Hinweis Wiedereinsetzung bei beA-Stoerung mit Glaubhaftmachung. Pflichtschritt bei elektronischem Versand an Gerichte und Behoerden.
---

# beA-Versand prüfen


## Triage zu Beginn
1. Ueber welchen Versandweg soll der Schriftsatz eingereicht werden: sUW (persoenliches Versenden des Inhabers) oder qeS (qualifizierte elektronische Signatur)?
2. Liegt eine beA-Versandquittung oder Eingangsbestaetigung vor, die die Fristwahrung belegt?
3. Gibt es Anzeichen fuer eine beA-Stoerung oder technische Uebermittlungspanne (§ 130a Abs. 6 ZPO Wiedereinsetzung)?
4. Muss ein elektronisches Empfangsbekenntnis (EB) erteilt werden?

## Aktuelle Rechtsprechung
- BGH, Beschl. v. 19.04.2023 - XII ZB 526/22, NJW 2023, 2035 — Der sichere Uebermittlungsweg (sUW) erfordert das persoenliche Versenden durch den Inhaber des beA-Postfachs; Versand durch Mitarbeiter ohne qeS ist unwirksam.
- BGH, Beschl. v. 26.01.2023 - III ZB 7/22, NJW 2023, 1000 — Bei technischer Stoerung des beA sind Anwalt und Kanzlei verpflichtet, rechtzeitig alternative Einreichungswege zu nutzen; spaetere Glaubhaftmachung der Stoerung nach § 130a Abs. 6 ZPO ist moeglich.
- BGH, Beschl. v. 17.05.2023 - VIII ZB 68/22, NJW 2023, 2273 — Die Versandquittung des beA gilt als Nachweis des Eingangs beim Gericht; fehlende Eingangsbestaetigung loest Pruefpflicht aus.
- BGH, Beschl. v. 11.05.2021 - VIII ZB 9/20, NJW 2021, 2279 — Wiedereinsetzung nach beA-Ausfall: Anwalt muss alle zumutbaren Massnahmen ergriffen haben, insbesondere Fax oder persoenliche Einreichung.

## Zentrale Normen
- § 130a ZPO — Elektronische Einreichung Zivilprozess; sUW oder qeS als Pflichtalternativen
- § 31a BRAO — beA-Nutzungspflicht fuer alle zugelassenen Rechtsanwaelte
- § 12 ERVV — Technische Anforderungen an den elektronischen Rechtsverkehr
- § 130a Abs. 6 ZPO — Wiedereinsetzung bei nachgewiesener technischer Stoerung

## Kommentarliteratur
- Zoeller/Greger ZPO § 130a Rn. 1-25 (Elektronischer Rechtsverkehr: Anforderungen und Fehlerfolgen)
- BeckOK ZPO/von Selle § 130a Rn. 1-30 (sUW und qeS: technische und rechtliche Pruefung)

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
