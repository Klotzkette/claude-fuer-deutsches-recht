---
name: bea-versand-pruefen
description: Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers) oder qualifizierte elektronische Signatur (qeS). Prüft Versand-Quittung Eingangsbestätigung und Verwertbarkeit für Fristnachweis. Hinweis Wiedereinsetzung bei beA-Stoerung mit Glaubhaftmachung. Pflichtschritt bei elektronischem Versand an Gerichte und Behoerden.
---

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
