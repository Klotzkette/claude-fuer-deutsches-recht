---
name: datenpanne-meldung
description: "Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung Behordenmeldung Betroffenenbenachrichtigung Dokumentation. Output: Meldeschreiben an Aufsichtsbehoerde Betroffenenbenachrichtigung Dokumentationsprotokoll. Abgrenzung: nicht für praeventive Massnahmen (dsfa-erstellung)."
---

# Datenpannen-Meldung (Art. 33/34 DSGVO)

## Zweck

Dieser Skill unterstützt beim strukturierten Umgang mit Verletzungen des Schutzes personenbezogener Daten (Art. 4 Nr. 12 DSGVO). Er führt durch die dreistufige Prüfung: (1) Liegt eine meldepflichtige Datenschutzverletzung vor? (2) Muss die Aufsichtsbehörde innerhalb von 72 Stunden informiert werden? (3) Besteht zusätzlich eine Benachrichtigungspflicht gegenüber Betroffenen? Anwendungsfälle: Ransomware-Angriff, versehentlich offengelegter Datenexport, gestohlener Laptop, Fehlversand personenbezogener Daten, unbefugter Mitarbeiterzugriff.

## Eingaben

Das Modell benötigt:

- **Beschreibung des Vorfalls**: Was ist wann und wie passiert? (Zeitpunkt der Entdeckung, vermutlicher Zeitpunkt des Eintritts)
- **Art der betroffenen Daten**: Kategorien (Art. 9/10 DSGVO?), Datenmenge, Anzahl betroffener Personen (geschätzt)
- **Betroffene Personen**: Kunden, Mitarbeiter, Minderjährige, vulnerable Gruppen?
- **Auswirkungen**: Welche Konsequenzen (Diskriminierung, Identitätsdiebstahl, finanzielle Schäden, Rufschädigung) drohen?
- **Zugang/Kontrolle**: Haben Unbefugte Daten eingesehen, kopiert, vernichtet oder verändert?
- **Bereits getroffene Maßnahmen**: Was hat der Mandant bereits unternommen?
- **Entdeckungsdatum**: Wann hat der Verantwortliche Kenntnis erlangt? (72-Stunden-Frist ab diesem Zeitpunkt)
- **Auftragsverarbeiter beteiligt?**: Liegt ein Vorfall beim AVV-Partner vor (Art. 33 Abs. 2 DSGVO)?

## Rechtlicher Rahmen

### Primärnormen

- **Art. 4 Nr. 12 DSGVO**: Definition "Verletzung des Schutzes personenbezogener Daten" – Vernichtung, Verlust, Veränderung, unbefugte Offenlegung oder Zugang zu personenbezogenen Daten.
- **Art. 33 Abs. 1 DSGVO**: Meldepflicht des Verantwortlichen an zuständige Aufsichtsbehörde; Frist: 72 Stunden nach Kenntniserlangung; bei verspäteter Meldung: Begründungspflicht.
- **Art. 33 Abs. 3 DSGVO**: Inhalt der Meldung: Beschreibung des Vorfalls, Kategorien und Anzahl Betroffener, Datenkategorien und -mengen, Kontaktdaten DPO, wahrscheinliche Folgen, ergriffene/geplante Maßnahmen.
- **Art. 33 Abs. 4 DSGVO**: Nachlieferung von Informationen in Stufen zulässig, wenn nicht alle Informationen sofort verfügbar.
- **Art. 33 Abs. 5 DSGVO**: Dokumentationspflicht aller Verletzungen, auch wenn keine Meldung erforderlich (internes Register).
- **Art. 34 DSGVO**: Benachrichtigungspflicht gegenüber betroffenen Personen, wenn Verletzung voraussichtlich hohes Risiko für Rechte und Freiheiten natürlicher Personen birgt.
- **Art. 34 Abs. 3 DSGVO**: Ausnahmen von der Benachrichtigungspflicht (geeignete Schutzmaßnahmen, Unverhältnismäßigkeit des Aufwands, behördliche Anordnung).

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### EDSA-Leitlinien

EDSA, Guidelines 9/2022 on personal data breach notification under GDPR, angenommen 28.03.2023: Enthält Fallkatalog typischer Datenpannen (Ransomware, Fehlversand, Datenverlust) mit Musterlösungen zur Risikoeinschätzung und Meldepflicht. Verbindliche Auslegungshilfe für Art. 33/34 DSGVO.

## Ablauf

**Schritt 1 – Sofortreaktion und Zeitsicherung**
- Exakten Zeitpunkt der Kenntniserlangung (durch wen, wie, wann) dokumentieren.
- 72-Stunden-Frist nach Art. 33 Abs. 1 DSGVO ab diesem Zeitpunkt berechnen.
- DPO (sofern bestellt, Art. 37 DSGVO) unverzüglich einbinden.

**Schritt 2 – Vorfallscharakterisierung**
- Prüfen: Verletzung i.S.d. Art. 4 Nr. 12 DSGVO (Vernichtung/Verlust/Veränderung/Offenlegung)?
- Art des Schadens klassifizieren: Vertraulichkeitsverletzung (Offenlegung), Integritätsverletzung (Manipulation), Verfügbarkeitsverletzung (Vernichtung/Verlust).

**Schritt 3 – Risikoeinschätzung (Schwellenwertprüfung)**
- Kein Risiko: Keine Meldepflicht (Art. 33 Abs. 1 a.E. DSGVO), nur interne Dokumentation.
- Risiko vorhanden: Meldung an Aufsichtsbehörde nach Art. 33 DSGVO.
- Hohes Risiko: Zusätzlich Benachrichtigung Betroffener nach Art. 34 DSGVO.
- Faktoren: Sensibilität der Daten (Art. 9/10 DSGVO-Kategorien erhöhen Risiko), Anzahl Betroffener, Identifizierbarkeit, finanzieller/sozialer Schaden, EDSA-Guidelines 9/2022.

**Schritt 4 – Meldung an Aufsichtsbehörde**
- Zuständige Behörde bestimmen: LfDI/LDA des Bundeslandes des Verantwortlichen (Hauptniederlassung); BfDI für Bundesbehörden und Telekommunikation.
- Online-Meldetools nutzen (jede LfDI unterhält eigenes Meldeportal).
- Inhalt nach Art. 33 Abs. 3 DSGVO: Art der Verletzung, Kategorien/Anzahl Betroffener, Datenkategorien/-mengen, Kontakt DPO/Datenschutzbeauftragter, Folgen, Maßnahmen.
- Teilmeldung zulässig (Art. 33 Abs. 4 DSGVO); Nachlieferung dokumentieren.

**Schritt 5 – Betroffenenbenachrichtigung (bei hohem Risiko)**
- Inhalt nach Art. 34 Abs. 2 DSGVO: Klare Beschreibung der Verletzung, Kontaktdaten DPO, wahrscheinliche Folgen, Abhilfemaßnahmen.
- Sprache: klar und verständlich, kein Fachjargon (Art. 12 Abs. 1 DSGVO).
- Ausnahmen prüfen: Verschlüsselung (Art. 34 Abs. 3 lit. a), öffentliche Bekanntmachung (lit. c), unverhältnismäßiger Aufwand.

**Schritt 6 – Interne Dokumentation**
- Eintrag in internes Verletzungsregister (Art. 33 Abs. 5 DSGVO): Auch bei nicht meldepflichtigen Vorfällen.
- Zeitstempel, Maßnahmen, Entscheidungsgrundlagen festhalten.

## Ausgabeformat

- **Risiko-Einschätzungsmatrix** (Tabelle): Datenkategorien × Risikograd × Meldepflicht × Benachrichtigungspflicht.
- **Meldeformular-Entwurf** (strukturierter Text nach Art. 33 Abs. 3 DSGVO).
- **Betroffenenbrief** (klare Sprache nach Art. 34 Abs. 2 DSGVO).
- **Internes Incident-Protokoll** (für Dokumentationspflicht Art. 33 Abs. 5 DSGVO).

## Beispiel

**Sachverhalt**: IT-Dienstleister des Unternehmens U meldet am 10.03.2025 um 09:00 Uhr, dass am 09.03.2025 um 22:00 Uhr unbekannte Dritte durch eine Sicherheitslücke auf eine Kundendatenbank mit 4.000 E-Mail-Adressen, Namen und Bestellhistorien zugegriffen haben.

**Gutachtenstil**:

*Fristbeginn*: Kenntniserlangung durch U am 10.03.2025 um 09:00 Uhr. Die 72-Stunden-Frist nach Art. 33 Abs. 1 DSGVO läuft bis zum 13.03.2025 um 09:00 Uhr.

*Meldepflicht*: Eine Datenschutzverletzung i.S.d. Art. 4 Nr. 12 DSGVO (unbefugte Offenlegung) liegt vor. Angesichts von 4.000 Betroffenen und personenbezogenen Daten der Bestellhistorie besteht ein Risiko für Rechte und Freiheiten; die Ausnahme "kein Risiko" greift nicht. Meldung an LfDI ist spätestens bis 13.03.2025 erforderlich (Art. 33 Abs. 1 DSGVO; EDSA Guidelines 9/2022, Beispiel 9).

*Benachrichtigungspflicht*: Ob ein hohes Risiko i.S.d. Art. 34 Abs. 1 DSGVO vorliegt, hängt davon ab, ob Dritte die Daten gezielt ausgenutzt haben (z.B. Phishing). Bei bloßem Zugriff ohne Nachweis der Datennutzung ist die Schwelle zum "hohen Risiko" nach EDSA Guidelines 9/2022 noch nicht zwingend erreicht; Einzelfallbewertung erforderlich.

*Dokumentation*: Unabhängig vom Ergebnis ist der Vorfall im internen Register nach Art. 33 Abs. 5 DSGVO zu dokumentieren.

## Risiken und typische Fehler

- **Fristversäumnis**: 72 Stunden ab Kenntniserlangung, nicht ab interner Aufklärung; Unkenntnis schützt nicht – der Verantwortliche muss organisatorisch sicherstellen, dass Vorfälle unverzüglich weitergeleitet werden.
- **Auftragsverarbeiter-Frist verwechseln**: AVV-Partner muss unverzüglich (ohne nennenswerte Verzögerung) an Verantwortlichen melden (Art. 33 Abs. 2 DSGVO); die 72-Stunden-Frist des Verantwortlichen beginnt mit dessen Kenntniserlangung.
- **Risikoeinschätzung zu lasch**: Keine Meldung trotz erkennbaren Risikos; Aufsichtsbehörden bewerten ex post streng, insb. bei Art. 9-Daten.
- **Unvollständige Meldung**: Teilmeldung ist zulässig, aber Nachlieferung muss dokumentiert und nachgereicht werden.
- **Betroffenenbenachrichtigung verzögert**: Bei hohem Risiko muss unverzüglich benachrichtigt werden (Art. 34 Abs. 1 DSGVO); keine 72-Stunden-Frist, aber kein Zuwarten auf Ermittlungsergebnis.
- **Fehlende interne Dokumentation**: Auch nicht meldepflichtige Vorfälle müssen ins interne Register; fehlendes Register ist eigenständiger Verstoß.
- **Bußgeldrisiko**: Verstöße gegen Art. 33/34 DSGVO sind nach Art. 83 Abs. 4 lit. a DSGVO mit bis zu 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes sanktionierbar.

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei neuen EuGH-Entscheidungen zum Schadensersatz nach Art. 82 DSGVO, EDSA-Updates zu den Guidelines 9/2022 sowie Änderungen der nationalen Meldeportale der Aufsichtsbehörden.

## Faktische Updates (Stand 05/2026)

- **NIS-2-UmsuCG (deutsches Umsetzungsgesetz):** in Kraft seit Ende 2025 (BSIG n. F.). Bei meldepflichtigen Datenpannen, die zugleich Cyber-Sicherheitsvorfaelle bei wichtigen oder besonders wichtigen Einrichtungen sind, parallel zur DSGVO-Meldung an die Aufsichtsbehoerde die BSI-Meldung nach § 32 BSIG n. F. binnen 24 h (Fruehwarnung), 72 h (Vorfallsmeldung) und 1 Monat (Abschlussbericht) abgeben. Quelle: BGBl 2025, BSI-Portal bsi.bund.de.
- **Art. 82 DSGVO — Schadensersatz EuGH-Linie:** Der blosse Kontrollverlust kann immateriellen Schaden begruenden, ein automatischer Anspruch entsteht aber nicht. Verschulden des Verantwortlichen wird vermutet, Entlastung moeglich. Konkrete Aktenzeichen vor Zitat live ueber curia.europa.eu pruefen.
- **EDSA Guidelines 9/2022 zu Datenpannen:** Endfassung (angenommen 28.03.2023) ist verbindliche Auslegungshilfe; enthaelt Fallkatalog Ransomware, Phishing, Exfiltration, Fehlversand, Diebstahl mit konkreten Risikoampeln. Quelle: edpb.europa.eu/our-work-tools/our-documents/guidelines.
- **BfDI / Landesdatenschutzbehoerden:** Bei standortuebergreifenden Vorfaellen Federfuehrung nach Art. 56 DSGVO (One-Stop-Shop) klaeren. BfDI für Bundes- und TK-/Postwesen; LDA-Bayern, LfDI BW etc. für privatwirtschaftliche Verantwortliche.

**Querverweise:**
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Datenpannen mit Drittlandbezug (Benachrichtigungspflicht des Importeurs)
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — Nachträgliche DSFA-Prüfung nach Datenpanne; Vorab-Konsultation Art. 36 DSGVO
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — Meldepflicht des Auftragsverarbeiters nach Art. 33 Abs. 2 DSGVO im AVV-Kontext

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
