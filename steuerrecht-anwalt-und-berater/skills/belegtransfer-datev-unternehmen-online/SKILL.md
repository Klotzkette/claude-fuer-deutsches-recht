---
name: belegtransfer-datev-unternehmen-online
description: "Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard."
---

# Belegtransfer ueber DATEV Unternehmen Online

## Fachlicher Anker

- **Normen:** § 6a, §§ 146.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

DATEV Unternehmen Online (DUO) ist die Standardplattform für Belegtransfer zwischen Mandant und StB. Mandant erfasst Belege ueber Smartphone-App, Scanner oder Mailpostfach; StB greift in DATEV Kanzlei-Rechnungswesen direkt zu. Dieser Skill konkretisiert den Belegfluss und die Standard-Workflow-Konfiguration.

## Kaltstart-Rueckfragen

1. Welche Mandanten arbeiten bereits mit DUO?
2. Welche Belegart wird transferiert?
3. Welche Erfassungs-Kanaele (App, Mail, Scanner)?
4. Welche OCR-Qualitaet erforderlich?
5. Welche Bank-Anbindung?
6. Welche eRechnung-Empfaenger?
7. Welche Mandantenfreigabe-Workflow?
8. Welche Archivierung GoBD-konform?

## Workflow

### Phase 1 — Belegerfassung

| Kanal | Anwendung |
|---|---|
| DATEV Upload Online (Mobile App) | Belege per Smartphone scannen |
| Mailpostfach | E-Mail-Rechnungen direkt an DUO-Postfach |
| Scanner | Buero-Scanner mit Standard-PDF |
| eRechnung | XRechnung/ZUGFeRD direkt empfangen |
| Bank-Online | PSD2-Anbindung; Bankbewegungen automatisch |

### Phase 2 — OCR und Beleg-Klassifizierung

- OCR-Erkennung des Beleg-Inhalts (Lieferant, Betrag, Datum, USt).
- Automatische Klassifizierung in DATEV-Konten-Vorschlag.
- Mandantenfreigabe oder direkte Verbuchung.

### Phase 3 — Buchungs-Vorschlag

- DATEV "Belege Online" / Belegcockpit zeigt Beleg-Bild und Buchungsvorschlag (Konto, USt-Schluessel, Buchungstext) nebeneinander an.
- Sachbearbeiter prueft den Vorschlag, korrigiert ggf. die Kontierung und gibt frei.
- Bei manueller Klaerung wird die Mandantenanfrage ueber das DUO-Postfach gestellt (revisionssichere Dokumentation).
- Konkrete Menue-Pfade in der aktuellen DATEV-Programmversion ggf. abweichend.

### Phase 4 — Bank-Anbindung

- Bank-Online ueber PSD2.
- Bankbewegungen automatisch.
- Zuordnung zu Belegen ueber Verwendungszweck.

### Phase 5 — eRechnungs-Empfang

- DUO mit eRechnungs-Postfach.
- XRechnung/ZUGFeRD-Auswertung.
- Automatische Verbuchung moeglich.

### Phase 6 — Archivierung

- GoBD-konform im Originalformat.
- 10 Jahre Aufbewahrung.
- Belege im Mandanten-Online-Postfach.

## Output

- Konfigurierter Belegfluss DUO.
- Buchungen mit Belegverknuepfung.
- GoBD-konforme Archivierung.

## Strategie und Praxis-Tipps

- DUO + DATEV Upload Online = Killer-Kombination für effizienten Belegfluss.
- OCR-Qualitaet variabel — Kontrolle durch Sachbearbeiter bleibt Pflicht.
- Bei vielen kleinen Belegen: Mandant taeglich scannen, Sachbearbeiter woechentlich pruefen.
- Bei eRechnungs-Empfang: Automatisierung Hebel.
- DATEV-Tipp: DATEV Upload Online mit GoBD-konformer Mandanten-Schulung.

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-erechnung-pflicht-b2b-2025-2026` — eRechnung.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 147.
- BMF v. 28.11.2019 zu GoBD.
- DATEV Unternehmen Online und "Belege Online" Dokumentation (aktuelle Version pruefen).
- Verifikations-Hinweis: konkrete Programmpfade und Modul-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8 AO (Wohnsitz, Aufenthalt)
- §§ 33, 34 AO (Steuerpflichtiger, gesetzliche Vertreter)
- § 42 AO (Gestaltungsmissbrauch)
- §§ 169-171 AO (Festsetzungsverjährung)
- §§ 233a, 235 AO (Verzinsung, Hinterziehungszinsen)
- § 370 AO (Steuerhinterziehung)
- §§ 153, 371 AO (Berichtigungserklärung, Selbstanzeige)
- §§ 15, 32a EStG (Einkünfte aus Gewerbebetrieb, Tarif)
- § 8 KStG, § 7 GewStG (Einkommen, Gewerbeertrag)
- §§ 1, 15 UStG (Steuerbare Umsätze, Vorsteuerabzug)

### Leitentscheidungen

- BFH I R 36/18 (Hinzurechnungsbesteuerung AStG)
- BFH XI R 11/22 (Reverse-Charge-Verfahren)
- BFH IX R 49/13 (Liebhaberei vs. Einkunftserzielungsabsicht)
- BVerfG 2 BvL 1/03 (Steuerfreistellung Existenzminimum)
- EuGH C-280/10 (Vorsteuerabzug bei wirtschaftlicher Tätigkeit)

### Anwendung im Skill

- Beraterhaftung gegen Mandantenpflicht (§§ 153, 154 AO) klar trennen; Selbstanzeige nach § 371 AO ist eine Strafnorm, kein Steueroptimierungs-Tool.
- Festsetzungsverjaehrung nach §§ 169-171 AO im Zweifel zugunsten des Steuerpflichtigen; Hemmung durch Aussenpruefung beachten.
- Bei Gestaltungsmissbrauch § 42 AO immer alternative Wirtschaftsgruende dokumentieren.
