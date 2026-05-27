---
name: mittelstand-corporate-ma-due-diligence-commercial-contracts
description: "Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Haendler-, SaaS-, Lizenz- und Materialvertraege auf Change of Control, Kündigung, Exklusivitaet, Haftung, IP und Preisrisiken."
---

# Kommerzielle Vertrags-DD

## Zweck

Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und Preisrisiken.

## Arbeitsmodus

- Vertragstypen clustern.
- Prüfmatrix je Vertragstyp anwenden.
- Ungewoehnliche Klauseln und Abweichungen vom Standard hervorheben.
- Disclosure Schedules und SPA-Schutz ableiten.

## Rote Schwellen

- Change-of-Control-Frage offen.
- Top-Kunde/Lieferant nicht erfasst.
- Vertragsanlage fehlt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/commercial-contract-review-grid.md
- assets/templates/disclosure-schedules-matrix.md

## Triage — klaere vor DD-Vertragspruefung

1. Welche Vertragstypen sind vorrangig — Top-5-Kundenvertraege, Top-5-Lieferantenvertraege, SaaS-Lizenzvertraege, Lizenzvertraege IP?
2. Wo liegt der Materiality-Schwellenwert — absolute Umsatzschwelle (z.B. Vertraege mit mehr als 500.000 EUR Jahresumsatz)?
3. Gibt es bekannte Change-of-Control-Klauseln aus dem DD-Scope-Meeting?
4. Sind Exklusivitaeten vorhanden, die die Wettbewerbsposition des Unternehmens nach Closing veraendern?

## Zentrale Rechtsgrundlagen

- §§ 305-310 BGB — AGB-Kontrolle: ungewoehnliche Klauseln in Standardvertraegen koennen unwirksam sein; relevant fuer Haftungsobergrenzen, Kuendigungsklauseln
- §§ 433 ff. BGB — Kaufvertragsrecht: Gewaehrleistung bei mangelhafter Vertragsuebertragung
- § 613a BGB — Betriebsuebergang: bei Asset Deal gehen Arbeitsverhaeltnisse kraft Gesetzes ueber; Change-of-Control in Arbeitsvertraegen unwirksam, soweit sie § 613a BGB umgehen
- §§ 15 ff. MarkenG / §§ 58 ff. PatG — IP-Lizenzvertraege: Einschrankung der Rechte bei Inhaberwechsel; Zustimmungsvorbehalte

## Aktuelle Rechtsprechung

- BGH, Urt. v. 16.12.2020 - VIII ZR 304/19, NJW 2021, 1016 — Change-of-Control: KoC-Klausel greift auch bei mittelbarem Anteilserwerb; wirtschaftlicher Durchgriff auf die Zielgesellschaft ist massgeblich; nicht nur formaler Kontrollerwerb
- BGH, Urt. v. 22.06.2011 - VIII ZR 98/10, BGHZ 190, 94 — AGB-Haftungsklausel: Pauschalschadenersatz-Klausel in B2B-Liefervertrag ist unwirksam nach § 309 Nr. 5 BGB, wenn sie den tatsaechlichen Schaden erheblich uebersteigt
- BGH, Urt. v. 25.09.2014 - I ZR 24/14, NJW 2015, 328 — IP-Lizenzvertrag: bei Change-of-Ownership greift Kuendigungsrecht des Lizenzgebers, sofern vertraglich vereinbart; Zustimmungsklausel ist zu beachten

## Kommentarliteratur

- MueKo BGB/Basedow, §§ 305-310 Rn. 1-100 (AGB-Recht)
- Beisel/Klumpp, Unternehmenskauf, Kapitel 2 § 4 (Kommerzielle Vertrags-DD), 8. Auflage

## Schritt-fuer-Schritt-Workflow

1. **Vertragsmatrix erstellen:** alle materiellen Vertraege auflisten; je Vertrag: Parteien, Laufzeit, Kuendigungsrechte, Wert, Change-of-Control-Klausel
2. **Change-of-Control-Screening:** jeder Vertrag auf Kuendigungsrecht oder Zustimmungspflicht bei Anteilsuebertragung pruefen
3. **Exklusivitaets-Mapping:** Exklusivitaeten, Wettbewerbsverbote, Alleinvertriebsrechte, die nach Closing problematisch sind
4. **Haftungs- und Garantieklauseln:** Haftungsobergrenzen, Gewichtung Vertragsrisiken fuer SPA-Garantien
5. **IP-Lizenz-Check:** Marken, Patente, Software-Lizenzen; Change-of-Control und Zustimmungserfordernisse
6. **Findings in SPA-Garantien ubersetzen:** Change-of-Control-Klauseln → Disclosure; Kuendigungsrechte → Freistellung oder Preisanpassung

## Rote Schwellen

- Wesentlicher Kundenvertrag mit Change-of-Control ohne Kaeufer-Consent: Deal-Breaker-Risiko
- Exklusivitaet zulasten Kaeufer nach Closing: wirtschaftlicher Schaden
- IP-Lizenz mit Kuendigungsrecht: Verlust wesentlicher IP-Basis
