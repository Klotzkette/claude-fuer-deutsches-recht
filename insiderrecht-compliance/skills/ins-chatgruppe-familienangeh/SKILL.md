---
name: ins-chatgruppe-familienangeh
description: "Ins 043 Chatgruppe Trading, Ins 044 Familienangeh Rige: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 043 Chatgruppe Trading, Ins 044 Familienangeh Rige

## Arbeitsbereich

Dieser Skill bündelt **Ins 043 Chatgruppe Trading, Ins 044 Familienangeh Rige** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-043-chatgruppe-trading` | Prueft Insiderhandel und Marktmanipulation in Messenger-Chat-Gruppen: Tatbestandsmerkmale, Beweis-Fragen und strafrechtliche Risiken nach § 119 WpHG. |
| `ins-044-familienangeh-rige` | Prueft Handelsverbote und Meldepflichten fuer Familienangehoerige und nahestehende Personen von PDMRs: Wissenszurechnung, Art. 19 MAR, Tipping-Risiko. |

## Arbeitsweg

Für **Ins 043 Chatgruppe Trading, Ins 044 Familienangeh Rige** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-043-chatgruppe-trading`

**Fokus:** Prueft Insiderhandel und Marktmanipulation in Messenger-Chat-Gruppen: Tatbestandsmerkmale, Beweis-Fragen und strafrechtliche Risiken nach § 119 WpHG.

# Messenger-Chatgruppen und Insiderhandel

## Rechtlicher Rahmen

Koordinierter Handel auf der Basis von Insiderinformationen in Messenger-Chatgruppen
(WhatsApp, Telegram, Signal, Discord) erfüllt typischerweise sowohl den Tatbestand des
Insiderhandels (Art. 14 MAR) als auch der Marktmanipulation (Art. 12 MAR) und ist nach
§ 119 WpHG strafbar. BaFin und Staatsanwaltschaften haben in den letzten Jahren mehrere
Verfahren eingeleitet.

Rechtsgrundlagen:
- Art. 12, 14 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- StPO §§ 94 ff. (Sicherstellung digitaler Beweismittel): https://www.gesetze-im-internet.de/stpo/__94.html
- BaFin-Jahresbericht: https://www.bafin.de

## Ziel dieses Skills

Dieser Skill analysiert, ob Chatgruppen-Aktivitäten den Tatbestand des Insiderhandels oder
der Marktmanipulation erfüllen, und entwickelt die Verteidigungsstrategie oder Compliance-
Präventionsmaßnahmen.

## Arbeitsprogramm

### Schritt 1 – Tatbestand Insiderhandel (Art. 14 MAR)

- Wer sind die Teilnehmer der Chatgruppe?
- Haben Teilnehmer Zugang zu Insiderinformationen (Primärinsider: Mitarbeiter des Emittenten;
 Sekundärinsider: Informationen aus Tipping)?
- Wurden Transaktionen auf Basis dieser Informationen koordiniert?
- Kausalitätsnachweis: Chat-Zeitpunkt vs. Transaktionszeitpunkt

### Schritt 2 – Tatbestand Marktmanipulation (Art. 12 MAR)

- Wurde eine koordinierte Handelsstrategie (z. B. Pump-and-Dump) in der Gruppe abgestimmt?
- Wurden falsche oder irreführende Informationen verbreitet, die den Kurs beeinflussen sollten?
- Meme Stocks: Koordinierte Käufe ohne Insiderinformation können als Marktmanipulation
 qualifiziert werden, wenn eine verzerrende Preiswirkung beabsichtigt ist

### Schritt 3 – Strafrechtliche Risiken (§ 119 WpHG)

- Vorsatz: Koordination in Chatgruppen belegt regelmäßig Vorsatz
- Gewerbsmäßig (§ 119 Abs. 2 WpHG): Wenn Handel regelmäßig und zur Gewinnerzielung
 → erhöhter Strafrahmen (bis zu 10 Jahre)
- Mittäterschaft: Alle aktiv koordinierenden Teilnehmer sind Mittäter (§ 25 Abs. 2 StGB)
- Anstiftung / Beihilfe: Reine Empfänger und Weiterleiter können auch strafbar sein

### Schritt 4 – Beweisfragen

- Chat-Protokolle sind digitale Beweismittel (§ 94 StPO)
- Messengerdienste können zur Herausgabe durch MLAT oder nationale Rechtshilfe verpflichtet sein
- Metadaten (Zeitstempel, Gruppen-Mitgliedschaft) oft ausreichend für Verdachtsnachweis
- Beratung externer Strafverteidiger vor Kooperation mit Behörden

### Schritt 5 – Präventionsmaßnahmen

- Compliance-Policy: Verbot koordinierter Handelsabsprachen (auch ohne Insiderinformation)
- Schulung: Mitarbeiter über Chatgruppen-Risiken informieren
- Monitoring: Ungewöhnliche Handelsmuster vor und nach Chatgruppen-Aktivität
- Social-Media-Policy: Klare Regeln für Diskussion über Finanzinstrumente

## Red-Team-Fragen

- Haben Chat-Teilnehmer Zugang zu Insiderinformationen des Emittenten?
- Gibt es einen zeitlichen Zusammenhang zwischen Chatgruppen-Aktivität und Transaktionen?
- Ist die Abgrenzung zwischen erlaubter Marktdiskussion und verbotenem Tipping klar?
- Werden Mitarbeiter ausreichend über Chatgruppen-Risiken geschult?

## Ausgabeformat

Erzeuge:
1. Tatbestandsprüfung: Insiderhandel × Marktmanipulation × Sachverhalt
2. Strafrisiko-Bewertung (nach § 119 WpHG)
3. Präventions-Policy (Chatgruppen-Nutzungsregeln)
4. Interne Untersuchungsvorlage bei Verdacht

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## 2. `ins-044-familienangeh-rige`

**Fokus:** Prueft Handelsverbote und Meldepflichten fuer Familienangehoerige und nahestehende Personen von PDMRs: Wissenszurechnung, Art. 19 MAR, Tipping-Risiko.

# Familienangehörige und nahestehende Personen – Insiderrecht

## Rechtlicher Rahmen

Art. 3 Abs. 1 Nr. 26 MAR definiert nahestehende Personen von PDMRs, die eigenständigen
MAR-Pflichten unterliegen. Sie müssen Eigengeschäfte nach Art. 19 MAR melden und dürfen
nicht auf Basis von Insiderinformationen handeln (Art. 14 MAR). Das Tipping von PDMRs an
Familienangehörige ist eine der häufigsten Insiderhandels-Konstellationen in der Praxis.

Rechtsgrundlagen:
- Art. 3 Abs. 1 Nr. 26 MAR (nahestehende Personen): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 14, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. V: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt die insiderrechtliche Situation für Familienangehörige und nahestehende
Personen von PDMRs und schafft Präventionsmaßnahmen gegen versehentliches Tipping.

## Arbeitsprogramm

### Schritt 1 – Personenkreis bestimmen (Art. 3 Abs. 1 Nr. 26 MAR)

Nahestehende Personen eines PDMR:
a) Ehegatte oder eingetragener Lebenspartner
b) Unterhaltsverpflichtete Kinder des PDMR
c) Verwandte, die seit mindestens 1 Jahr im gemeinsamen Haushalt leben
d) Juristische Personen, Trusts, Personengesellschaften unter Kontrolle des PDMR oder
 einer der genannten natürlichen Personen

### Schritt 2 – Eigenständige MAR-Pflichten nahestehender Personen

- Handelsverbot nach Art. 14 MAR: Kein Handel auf Basis von Insiderinformationen des PDMR
 (auch wenn diese nur beiläufig erwähnt wurden)
- Directors' Dealings nach Art. 19 MAR: Alle Eigengeschäfte ≥ 20.000 EUR meldepflichtig
- Frist: 3 Geschäftstage nach Transaktion an BaFin und Emittent

### Schritt 3 – Tipping-Risiko

- PDMR darf nahestehenden Personen keine Insiderinformationen mitteilen (Art. 10 MAR)
- Selbst beiläufige Erwähnung kann Art. 10 MAR-Verstoß sein
- „Need-to-know" gilt auch im privaten Bereich: Keine Gespräche über laufende
 Transaktionen zu Hause
- Schulung: PDMRs müssen explizit über Tipping-Verbot im privaten Umfeld belehrt werden

### Schritt 4 – Pre-Clearance für nahestehende Personen

- Emittent sollte Pre-Clearance-Prozess auch für nahestehende Personen anbieten
- PDMR meldet geplante Transaktion der nahestehenden Person an Compliance
- Compliance prüft: Aktuelle Insiderinformation? Closed Period?
- Schriftliche Freigabe oder Ablehnung

### Schritt 5 – Schulung und Bewusstsein

- PDMRs auf Jahresschulung: Explizites Modul zu Familienangehörigen und Tipping-Verbot
- Schriftliche Verpflichtung des PDMR: Ich werde keine Insiderinformationen an nahestehende
 Personen weitergeben
- Merkblatt für PDMRs: „Was darf ich zu Hause nicht sagen?"

## Red-Team-Fragen

- Sind alle nahestehenden Personen der PDMRs identifiziert und bekannt?
- Werden nahestehende Personen über ihre eigenen MAR-Pflichten informiert?
- Gibt es ein Pre-Clearance-Angebot für nahestehende Personen?
- Werden PDMRs explizit auf das Tipping-Verbot im privaten Umfeld hingewiesen?

## Ausgabeformat

Erzeuge:
1. Nahestehende-Personen-Register (je PDMR mit Beziehungstyp)
2. Belehrungsschreiben für nahestehende Personen
3. Pre-Clearance-Formular für nahestehende Personen
4. PDMR-Merkblatt: „Was darf ich zu Hause nicht sagen?"

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
