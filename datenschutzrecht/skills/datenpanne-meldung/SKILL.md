---
name: datenpanne-meldung
description: Begleitet Verantwortliche und Berater bei der Prüfung der Meldepflicht nach Art. 33 DSGVO (72-Stunden-Frist an Aufsichtsbehörde) und der Benachrichtigungspflicht nach Art. 34 DSGVO (betroffene Personen), einschließlich Dokumentation. Lädt bei Datenpannen, Sicherheitsvorfällen, unberechtigten Zugriffen und Datenverlust.
language: de
triggers:
  - "Datenpanne"
  - "Data Breach"
  - "Sicherheitsvorfall"
  - "Art. 33 DSGVO"
  - "Art. 34 DSGVO"
  - "Datenschutzverletzung"
  - "Meldepflicht"
  - "72 Stunden"
  - "Aufsichtsbehörde melden"
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

- **Art. 4 Nr. 12 DSGVO**: Definition „Verletzung des Schutzes personenbezogener Daten" – Vernichtung, Verlust, Veränderung, unbefugte Offenlegung oder Zugang zu personenbezogenen Daten.
- **Art. 33 Abs. 1 DSGVO**: Meldepflicht des Verantwortlichen an zuständige Aufsichtsbehörde; Frist: 72 Stunden nach Kenntniserlangung; bei verspäteter Meldung: Begründungspflicht.
- **Art. 33 Abs. 3 DSGVO**: Inhalt der Meldung: Beschreibung des Vorfalls, Kategorien und Anzahl Betroffener, Datenkategorien und -mengen, Kontaktdaten DPO, wahrscheinliche Folgen, ergriffene/geplante Maßnahmen.
- **Art. 33 Abs. 4 DSGVO**: Nachlieferung von Informationen in Stufen zulässig, wenn nicht alle Informationen sofort verfügbar.
- **Art. 33 Abs. 5 DSGVO**: Dokumentationspflicht aller Verletzungen, auch wenn keine Meldung erforderlich (internes Register).
- **Art. 34 DSGVO**: Benachrichtigungspflicht gegenüber betroffenen Personen, wenn Verletzung voraussichtlich hohes Risiko für Rechte und Freiheiten natürlicher Personen birgt.
- **Art. 34 Abs. 3 DSGVO**: Ausnahmen von der Benachrichtigungspflicht (geeignete Schutzmaßnahmen, Unverhältnismäßigkeit des Aufwands, behördliche Anordnung).

### Leitentscheidungen

1. EuGH, Urt. v. 14.12.2023 – C-340/21 (Natsionalna agentsia za prihodite/VB), NJW 2024, 685 Rn. 55–79: Allein der unbefugte Zugang zu personenbezogenen Daten durch Dritte begründet keinen automatischen Schadensersatzanspruch; das nationale Gericht muss das tatsächliche Risiko zukünftiger Schäden prüfen. Für die Meldepflicht nach Art. 33 DSGVO ist jedoch schon die bloße Möglichkeit eines Risikos ausreichend, um die 72-Stunden-Frist auszulösen.

2. BVerwG, Urt. v. 27.04.2022 – 6 C 8.20, BVerwGE 175, 234 Rn. 38–42: Zur Kompetenz der deutschen Aufsichtsbehörden bei grenzüberschreitenden Datenschutzverstößen; Meldung an federführende Behörde nach Art. 56 DSGVO bei international tätigen Verantwortlichen, ohne dass nationale Zuständigkeit entfällt, wenn inländische Betroffene beschwert sind.

### Kommentarliteratur

1. Reif, in: Gola/Heckmann, DSGVO/BDSG, 3. Aufl. 2022, Art. 33 DSGVO Rn. 14–40: Ausführlich zur Schwellenwertprüfung „voraussichtlich kein Risiko für Rechte und Freiheiten" (Art. 33 Abs. 1 a.E. DSGVO); Abgrenzung meldepflichtiger von nicht meldepflichtiger Verletzung anhand der EDSA-Fallgruppen; zur Kenntniserlangung durch Auftragsverarbeiter.

2. Bergt, in: Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024, Art. 33 DSGVO Rn. 22–55: Zu gestufter Meldung, Nachreichung von Informationen, Inhalt der Meldung im Einzelnen und zur Frage, wann die 72-Stunden-Frist zu laufen beginnt (Kenntniserlangung des verantwortlichen Organs vs. beliebiger Mitarbeiter).

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

*Meldepflicht*: Eine Datenschutzverletzung i.S.d. Art. 4 Nr. 12 DSGVO (unbefugte Offenlegung) liegt vor. Angesichts von 4.000 Betroffenen und personenbezogenen Daten der Bestellhistorie besteht ein Risiko für Rechte und Freiheiten; die Ausnahme „kein Risiko" greift nicht. Meldung an LfDI ist spätestens bis 13.03.2025 erforderlich (Art. 33 Abs. 1 DSGVO; EDSA Guidelines 9/2022, Beispiel 9).

*Benachrichtigungspflicht*: Ob ein hohes Risiko i.S.d. Art. 34 Abs. 1 DSGVO vorliegt, hängt davon ab, ob Dritte die Daten gezielt ausgenutzt haben (z.B. Phishing). Bei bloßem Zugriff ohne Nachweis der Datennutzung ist die Schwelle zum „hohen Risiko" nach EDSA Guidelines 9/2022 noch nicht zwingend erreicht; Einzelfallbewertung erforderlich.

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

Alle Aussagen in Meldeformularen, Memos und Betroffenenbriefen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rechtsprechungsbelege im BGH-Stil und zwei Kommentarbelege im Bearbeiter-Stil. Die EDSA-Guidelines 9/2022 sind als EU-Soft-Law-Quelle stets anzugeben. Wo Rspr. fehlt, ausdrücklich auf Kommentarliteratur und EDSA-Leitlinien verweisen.
