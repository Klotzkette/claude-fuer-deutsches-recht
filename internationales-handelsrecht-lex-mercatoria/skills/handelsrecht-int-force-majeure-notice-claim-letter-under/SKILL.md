---
name: handelsrecht-int-force-majeure-notice-claim-letter-under
description: "INT Force Majeure Notice Claim Letter Under: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT Force Majeure Notice Claim Letter Under

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT Force Majeure Notice Claim Letter Under** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-085-force-majeure-notice-letter` | Internationales Handelsrecht: Force-Majeure-Notifikationsschreiben nach CISG Art. 79 Abs. 3, PICC Art. 7.1.7 und ICC Force Majeure Clause 2020. Inhalt, Fristen, Dokumentation und Folgen bei fehlerhafter oder verspäteter Notifikation. |
| `ihl-086-claim-letter-under-cisg` | Internationales Handelsrecht: Mängelrüge und Schadensersatzgeltendmachung nach CISG. Anforderungen an das Rügeschreiben (Art. 39 CISG), Aufhebungserklärung (Art. 26 CISG), Schadensersatzberechnung (Art. 74-76 CISG) und Musterkorrespondenz. |
| `ihl-088-contract-playbook-exporter` | Internationales Handelsrecht: Vertragshandbuch für den Exporteur. Standardpositionen in Verhandlungen, Fallback-Positionen, Prioritäten (Rechtswahl, Schiedsklausel, Haftungsbeschränkung, Eigentumsvorbehalt) und BATNA-Analyse für internationale Kaufverträge. |
| `ihl-089-contract-playbook-importer` | Internationales Handelsrecht: Vertragshandbuch für den Importeur. Käufer-Standardpositionen, Qualitätssicherungsklauseln, Lieferantenbewertung, Preisanpassung, Zahlungsbedingungen und Defensivstrategie bei Lieferverzug und Qualitätsmängeln. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT Force Majeure Notice Claim Letter Under**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-085-force-majeure-notice-letter`

**Fokus:** Internationales Handelsrecht: Force-Majeure-Notifikationsschreiben nach CISG Art. 79 Abs. 3, PICC Art. 7.1.7 und ICC Force Majeure Clause 2020. Inhalt, Fristen, Dokumentation und Folgen bei fehlerhafter oder verspäteter Notifikation.

# Force-Majeure-Notifikationsschreiben

## Worum es geht

Die Notifikationspflicht ist untrennbar mit der Force-Majeure-Berufung verbunden. CISG Art. 79 Abs. 3 verlangt unverzügliche Mitteilung nach Kenntnis des Hindernisses — Verspätung führt zu Haftung für den durch die Verzögerung entstandenen Schaden. Die Notifikation muss Art und Erwartete Dauer des Hindernisses benennen.

## Kernnormen / Kernquellen

- **CISG Art. 79 Abs. 3**: Notifikationspflicht — unverzüglich nach Kenntnis; Rechtsfolge bei Versäumnis
- **PICC Art. 7.1.7 Abs. 3**: Prompte Notifikation nach Kenntnis des FM-Ereignisses
- **ICC Force Majeure Clause 2020 Art. 5**: 30-Tage-Frist für Notifikation nach FM-Eintritt
- **BGB § 286 Abs. 4**: Kein Verzug bei Unmöglichkeit (nationales Pendant)
- **Geschäftsgeheimnisse**: Notifikation ohne Offenbarung von Betriebsgeheimnissen möglich

## Schlüsselbegriffe

- Unverzüglichkeit: sofort nach Kenntnis, ohne schuldhaftes Zögern (§ 121 BGB-Maßstab analog)
- Inhalt der Notifikation: (1) Art des Hindernisses, (2) Wirkung auf Leistungspflicht, (3) Erwartete Dauer
- Beweissicherung: Datum der Kenntnis dokumentieren (interne Notiz, E-Mail-Zeitstempel)
- Aktualisierungspflicht: bei Änderung des FM-Ereignisses (Verlängerung, Wegfall) erneute Notifikation
- Empfangsnachweis: Einschreiben/Fax/E-Mail mit Lesebestätigung (DHL/Courier für Originalschreiben)

## Typische Streitfragen / Anwendungsfälle

1. COVID-19: Wann begann Kenntnis — Ausbruch in China (Januar 2020) oder nationaler Lockdown?
2. Verspätete Notifikation: Welchen Schaden schuldet Schuldner bei 2-Wochen-Verzögerung?
3. ICC FM-Clause 30-Tage: Absolute Frist oder kann Kläger Versäumnis entschuldigen?
4. Notifikationsform: Reicht WhatsApp-Nachricht oder muss es formale Briefform sein?
5. Geheimhaltung: Notifikation erwähnt proprietäres Verfahren — wie Sicherheit herstellen?

## Methodik

- Datum der FM-Kenntnisnahme dokumentieren (Screenshot, Besprechungsprotokoll)
- Notifikationsschreiben: sofort, spätestens in 5 Werktagen; ICC-Clause: max. 30 Tage
- Inhalt: Ereignis beschreiben, Vertragspflichten benennen, voraussichtliche Dauer schätzen
- Empfang sichern: Courier + E-Mail parallel; Zugangsbestätigung verlangen

## Output

- FM-Notifikationsschreiben-Muster (CISG und ICC-Klausel-konform)
- Fristkalender (CISG unverzüglich vs. ICC 30 Tage)
- Beweissicherungs-Checkliste

## Quellenregel

CISG Art. 79: uncitral.un.org. PICC Art. 7.1.7: unidroit.org. ICC FM-Klausel 2020: iccwbo.org. BGB §§ 121, 286: gesetze-im-internet.de. Unsicherheit bleibt sichtbar.

## 2. `ihl-086-claim-letter-under-cisg`

**Fokus:** Internationales Handelsrecht: Mängelrüge und Schadensersatzgeltendmachung nach CISG. Anforderungen an das Rügeschreiben (Art. 39 CISG), Aufhebungserklärung (Art. 26 CISG), Schadensersatzberechnung (Art. 74-76 CISG) und Musterkorrespondenz.

# Claim-Letter unter CISG

## Worum es geht

Mängelrügen, Schadensersatzforderungen und Vertragsaufhebungserklärungen unter CISG unterliegen spezifischen formalen und inhaltlichen Anforderungen. Eine unspezifizierte Rüge verliert Mangelrechte (Art. 39 CISG). Das Claim-Letter muss Mangelart, Datum der Entdeckung, verlangte Rechtsbehelfe und Schadensberechnung klar benennen.

## Kernnormen / Kernquellen

- **CISG Art. 39 Abs. 1**: Spezifizierte Rüge — Art des Mangels, angemessene Frist
- **CISG Art. 26**: Aufhebungserklärung — formfrei, Zugang erforderlich
- **CISG Art. 74**: Schadensersatz — Berechnung Verlust und entgangener Gewinn
- **CISG Art. 75**: Deckungskauf als Schadensberechnungsmethode
- **CISG Art. 77**: Mitigation — Gläubiger muss Schadensminderungsmaßnahmen ergreifen
- **CISG Art. 78**: Zinsen — fällig ab Zahlungsverzug (Rate nach IPR)

## Schlüsselbegriffe

- Spezifizierung: Beschreibung der Mangelart (nicht "allgemeine Qualitätsprobleme")
- Datum der Rüge: maßgeblich für 2-Jahres-Frist Art. 39 Abs. 2
- Rechtsbehelfsklarheit: Minderung oder Ersatz? Aufhebung? Kombination
- Schadensberechnung: konkret mit Belegen (Deckungskauf-Rechnung, Gutachten)
- Mitigation-Ausweis: zeigen dass Gläubiger Schadensminderungsmaßnahmen ergriffen hat

## Typische Streitfragen / Anwendungsfälle

1. Rüge zu pauschal ("product does not meet specifications"): Wirksam nach Art. 39?
2. Claim-Letter als Aufhebungserklärung: Muss es explizit "I hereby avoid the contract" heißen?
3. Zinsen: Welchen Satz darf ich im Claim-Letter nennen ohne Art. 78 CISG zu überschreiten?
4. Mitigation: Kein Deckungskauf möglich (Marktknappheit) — wie im Claim-Letter dokumentieren?
5. Simultaner Rechtsbehelf: Können Minderung und Schadensersatz in einem Schreiben gefordert werden?

## Methodik

- Rügeschreiben: Datum, spezifischer Mangel, Entdeckungsdatum, Rechtsbehelfe, Frist zur Stellungnahme
- Aufhebung: klar und eindeutig; mit Begründung (wesentliche Verletzung oder Nachfrist)
- Schadensberechnung: Anlage mit Belegen (Rechnungen, Gutachten, Deckungskauf)
- Mitigation dokumentieren: eigene Schritte zur Schadensminderung nachweisen

## Output

- Mängelrüge-Schreiben-Muster (Art. 39 CISG-konform)
- Schadensersatz-Forderungsschreiben-Muster (Art. 74-77 CISG)
- Aufhebungserklärung-Muster (Art. 26 CISG)

## Quellenregel

CISG Art. 26, 39, 74-78: uncitral.un.org. Schrifttum: Lookofsky, CISG (2017) Art. 39. CISG-Rspr.: CISG-online.ch. Unsicherheit bleibt sichtbar.

## 3. `ihl-088-contract-playbook-exporter`

**Fokus:** Internationales Handelsrecht: Vertragshandbuch für den Exporteur. Standardpositionen in Verhandlungen, Fallback-Positionen, Prioritäten (Rechtswahl, Schiedsklausel, Haftungsbeschränkung, Eigentumsvorbehalt) und BATNA-Analyse für internationale Kaufverträge.

# Contract Playbook für Exporteure

## Worum es geht

Ein Contract Playbook hilft Exporteuren, ihre Standardpositionen und Verhandlungsstrategie zu systematisieren. Es definiert Must-Haves (Rechtswahl, Schiedsklausel), Should-Haves (Haftungscap, EV) und Nice-to-Haves (Audit-Recht, ESG-Klausel). BATNA-Analyse schärft Verhandlungsflexibilität.

## Kernnormen / Kernquellen

- **CISG Art. 6**: Opting-out vs. Opting-in (Rechtswahl-Priorität)
- **ICC Schiedsregeln 2021**: Schiedsklausel als Dispute-Resolution-Standard
- **BGB §§ 449, 929**: Eigentumsvorbehalt — Must-Have für alle Exporteure
- **CISG Art. 74-77**: Schadensersatz und Mitigation — Haftungscap-Rechtfertigung
- **LkSG §§ 3-5**: ESG/LkSG-Lieferkettenklausel als wachsendes Standard
- **VBER (EU) 2022/720**: Vertriebsklauseln im Exportkontext

## Schlüsselbegriffe

- Must-Have: ohne diese Klauseln kein Vertragsabschluss (Rechtswahl, Schiedsklausel, EV)
- Should-Have: starke Verhandlungsposition erforderlich (Haftungscap, FM-Klausel)
- Nice-to-Have: opportunistisch einfordern (ESG-Auditrecht, Indexklausel)
- Fallback-Position: was Exporteur akzeptiert wenn Must-Have abgelehnt wird
- BATNA: Best Alternative to a Negotiated Agreement — Mindeststandard definieren

## Typische Streitfragen / Anwendungsfälle

1. Käufer verlangt Anwendbarkeit seines nationalen Rechts: Akzeptabler Kompromiss?
2. Kein Schiedsgericht: Kann ICC-Mediation + staatliches Gericht Fallback sein?
3. Haftungscap verweigert: Wie alternativ mit Haftungsausschlussklausel für Folgeschäden?
4. Eigentumsvorbehalt in Nicht-Anerkennungsland: Welche Alternative (Akkreditiv, Bürgschaft)?
5. ESG-Klausel: Wann ist das verhandelbar und wann must-have (LkSG-Pflicht)?

## Methodik

- Playbook-Struktur: Klausel → Standardposition → Begründung → Fallback → Red Line
- BATNA-Analyse vor jeder Verhandlung definieren
- Länder-spezifische Anpassung: EV in USA (UCC Filing), China (lokale Registrierung)
- Revisionszyklus: Playbook jährlich auf Rechtsentwicklungen (CISG-Rspr., VBER, LkSG) aktualisieren

## Output

- Contract-Playbook-Struktur-Template
- Klausel-Prioritätenliste (Must/Should/Nice)
- BATNA-Analyse-Vorlage für internationale Kaufverhandlungen

## Quellenregel

CISG: uncitral.un.org. ICC Regeln 2021: iccwbo.org. LkSG: gesetze-im-internet.de. VBER 2022/720: eur-lex.europa.eu. Schrifttum: International Trade Law Handbook (Praxis-Quellen). Unsicherheit bleibt sichtbar.

## 4. `ihl-089-contract-playbook-importer`

**Fokus:** Internationales Handelsrecht: Vertragshandbuch für den Importeur. Käufer-Standardpositionen, Qualitätssicherungsklauseln, Lieferantenbewertung, Preisanpassung, Zahlungsbedingungen und Defensivstrategie bei Lieferverzug und Qualitätsmängeln.

# Contract Playbook für Importeure

## Worum es geht

Importeure verfolgen eine andere Verhandlungsstrategie als Exporteure: Qualitätssicherung (PSI, Audits), günstige Zahlungsbedingungen (Open Account oder Akkreditiv), Eigentumsvorbehalt des Lieferanten beschränken und CISG-Rechtsbehelfe (Art. 38-39 Rüge, Art. 50 Minderung) als Druckmittel nutzen.

## Kernnormen / Kernquellen

- **CISG Art. 35 Abs. 2 lit. b**: Besonderer Zweck — muss Lieferant mitgeteilt worden sein
- **CISG Art. 38-39**: Rügerecht — unverzüglich nach Entdeckung; Art des Mangels spezifizieren
- **CISG Art. 50**: Minderung — Verhältnis Istwert/Sollwert als Kalkulationsgrundlage
- **Incoterms 2020 FCA/CIP**: Käuferfreundlich: Versicherung durch Verkäufer, Übergabe klar
- **UCP 600**: Akkreditiv schützt Käufer — Zahlung nur bei konformen Dokumenten
- **LkSG §§ 4-5**: Importeur-Sorgfaltspflichten bei Drittlandslieferanten

## Schlüsselbegriffe

- Inspection Right: Recht des Importeurs auf Pre-Shipment Inspection
- Qualitätszertifikat-Klausel: Verlangen von ISO/IEC 17025 akkreditiertem Testlabor
- Nacherfüllungspflicht: Klausel die Verkäufer zu Nachbesserung oder Ersatz verpflichtet
- LkSG-Lieferantenklausel: Verpflichtung des Lieferanten zu Menschenrechts-Compliance
- Open Account mit Forderungsversicherung: Euler Hermes/Allianz Trade als Kreditabsicherung

## Typische Streitfragen / Anwendungsfälle

1. Verkäufer-EV: Wie schwächt Importeur Eigentumsvorbehalt ab in Vertrag?
2. Qualitätsrüge: Importeur verlangt 100% Nachlieferung, Verkäufer bietet Minderung — Kompromiss?
3. CISG Art. 38 Untersuchungspflicht: Bei Containerware — Muss Importeur sofort auspacken und prüfen?
4. LkSG: Welche Klauseln muss Importeur in Kaufvertrag mit chinesischem Lieferanten einbauen?
5. Incoterms-Wahl: Warum sollte Importeur CIP statt CIF fordern?

## Methodik

- Qualitäts-Must-Have: PSI-Klausel + Inspection Certificate als Akkreditiv-Dokument
- Rüge-Prozess: Standardprozess für alle Lieferungen dokumentieren (Eingangsinspektion)
- LkSG-Lieferantenklausel: Code of Conduct + Audit-Recht + Vertragsstrafe bei Verstoß
- EV-Modifikation: wenn EV unvermeidbar dann zeitlich begrenzen (max. bis Zahlungseingang)

## Output

- Importeur-Playbook-Struktur
- LkSG-Lieferantenklausel-Muster
- Qualitäts-Eingangs-Checkliste

## Quellenregel

CISG Art. 35, 38-39, 50: uncitral.un.org. LkSG: gesetze-im-internet.de. UCP 600: iccwbo.org. Incoterms 2020: iccwbo.org. Unsicherheit bleibt sichtbar.
