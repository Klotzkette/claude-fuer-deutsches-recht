---
name: grosskanzlei-corporate-ma-due-diligence-reporting
description: "Due Diligence Report erstellen und strukturieren: Anwendungsfall After DD-Phase muss Anwalt einen umfassenden DD-Bericht fuer Kaeufer-Management, Investitionskomitee oder Finanzierungsbank erstellen. SPA-Berichtspflichten, § 93 AktG Informationsgrundlage. Pruefraster Executive Summary, Risikoklassifizierung, Workstream-Einzelberichte, Handlungsempfehlungen, SPA-Anpassungshinweise. Output strukturierter DD-Bericht mit Executive Summary, Risikomatrix und SPA-Empfehlungen. Abgrenzung zu DD-Legal und DD-Commercial fuer Einzelanalysen."
---

# DD Reporting und Legal Fact Book

## Zweck

Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping.

## Arbeitsmodus

- Findings nach Materiality, Risiko und Deal-Auswirkung verdichten.
- Quellen, Annahmen und nicht geprüfte Bereiche transparent halten.
- Empfehlungen in SPA, CP, Disclosure, Price, Indemnity oder PMI übersetzen.
- Mandanten- und W&I-Version trennen.

## Rote Schwellen

- Report ohne Scope/Limitations.
- Finding ohne Quelle.
- Keine Verbindung zu Vertragslösung.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/red-flag-report.md
- assets/templates/dd-finding-card.md

## Triage

1. Welches Report-Format benoetigt der Mandant — Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary?
2. Welches Materiality-Konzept gilt — absolute Schwellen oder relatives EBITDA-Prozent?
3. Sind alle DD-Workstreams abgeschlossen oder sind Teilberichte zusammenzufassen?
4. Ist ein Issues-to-SPA-Mapping erforderlich — DD-Findings direkt in SPA-Garantien und Freistellungen uebersetzen?

## Zentrale Rechtsgrundlagen

- § 675 BGB — Auftrag und anwaltlicher Beratungsvertrag: Berater schuldet vollstaendigen Bericht; Luecken koennen Haftung ausloesen
- §§ 280, 241 Abs. 2 BGB — Beraterpflichten: Anwalt muss saemtliche wesentlichen Risiken benennen und einordnen; Unterlassen ist Pflichtverletzung
- §§ 307-309 BGB — AGB-Haftungsbeschraenkungen im Beratungsvertrag: Haftungsausschluss oder Cap fuer Reports oft vereinbart; Grenze: grobe Fahrlaessigkeit nicht ausschließbar

## Aktuelle Rechtsprechung

- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — Anwaltshaftung im DD-Bericht: anwaltlicher DD-Berater haftet, wenn er wesentliche Risiken nicht meldet; allgemeiner Haftungsausschluss befreit nicht von grob fahrlaessigen Unterlassungen
- OLG Frankfurt, Urt. v. 22.02.2021 - 23 U 70/19, NZG 2021, 680 — Red-Flag-Report: unvollstaendiger Report begruendet Schadensersatzanspruch; auch bei kurzer DD-Zeit muessen alle erkennbaren wesentlichen Risiken benannt werden

## Kommentarliteratur

- Picot, Unternehmenskauf, Kapitel 2 (Due Diligence, Reporting, Fact Book), 5. Auflage

## Schritt-fuer-Schritt-Workflow

1. **Workstream-Findings zusammenfuehren:** Legal, Commercial, Tax, HR, IP, IT, Real Estate, Litigation
2. **Materiality-Filter anwenden:** Findings nach Low/Medium/High/Deal-Breaker kategorisieren
3. **Issues-to-SPA-Mapping:** je High-Finding: Empfehlung fuer SPA-Klausel (Garantie, Freistellung, Preisanpassung)
4. **Report-Format erstellen:** Executive Summary (1-3 Seiten), Red-Flag-Report (10-20 Seiten), Full DD Report (detailliert)
5. **Human-in-the-loop:** alle Deal-Breaker-Findings → Partner-Review vor Uebersendung

## Rote Schwellen

- Wesentliche Findings nicht adressiert: Anwaltshaftung § 280 BGB
- Issues-to-SPA-Mapping fehlt: Kaeufer hat keine Entscheidungsgrundlage fuer SPA-Verhandlung
- Executive Summary ohne klare Risikoampel: Management kann nicht priorisieren
