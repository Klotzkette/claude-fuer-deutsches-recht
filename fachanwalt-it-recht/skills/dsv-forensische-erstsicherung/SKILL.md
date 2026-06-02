---
name: dsv-forensische-erstsicherung
description: "Steuert die forensische Erstsicherung nach einem Datenschutzvorfall im Zusammenspiel zwischen Mandant, interner IT, externem Forensiker und Anwaltskanzlei. Behandelt: Auswahl und Beauftragung des Forensikers; Mandatsstruktur mit Anwaltsprivileg; Scope; Triage versus tiefe Analyse; Berichtsformate; Kommunikation mit Aufsichtsbehörde; Schnittstellen zur Cyberversicherung. Output: Beauftragungsmuster, Briefing für Forensiker und Steuerungsraster. Abgrenzung: keine eigene forensische Tätigkeit; keine technische Anleitung."
---

# Forensische Erstsicherung — Beauftragung und Steuerung

## Triage — kläre vor der Bearbeitung

1. Soll der Forensiker durch den Mandanten oder durch die Kanzlei beauftragt werden (Anwaltsprivileg)?
2. Welche Cyberversicherung gibt einen Forensiker vor?
3. Welche Daten sind besonders sensibel und schränken den Scope ein?
4. Welche Sprache muss der Bericht haben — Deutsch oder Englisch für die Behörde?
5. Wer übernimmt die Schnittstelle zur Aufsichtsbehörde?
- Was will der Mandant wirklich erreichen? (Eindämmung; rechtssichere Bewertung; Verteidigungsfähigkeit)

## Rechtsgrundlagen

- **Art. 32 DSGVO** Sicherheit der Verarbeitung.
- **Art. 33 Abs. 3 lit. c DSGVO** Maßnahmenangabe in der Meldung.
- **§ 43a Abs. 2 BRAO** Verschwiegenheit; **§ 53 StPO** Zeugnisverweigerungsrecht.
- **§ 203 StGB** Berufsgeheimnis.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Reichweite des Anwaltsprivilegs bei Cyber-Forensik vor Ausgabe verifizieren.

## Zentrale Normen

Art. 32; Art. 33 Abs. 3 lit. c DSGVO; § 43a Abs. 2 BRAO; § 53 StPO; § 203 StGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Beauftragungsraster

Auftraggeber: Kanzlei in Untermandat / Mandant direkt.

Scope: Triage-Bericht 48 h; vertiefte Analyse Wochen 1-4; Schlussbericht.

Lieferobjekte: Sofort-Memo; Zwischenbericht; Schlussbericht; Behörden-tauglicher Kurzbericht.

Vertraulichkeit: NDA; Anwaltsprivileg-Klausel; Aufbewahrung nur in Mandantenakte.

Schnittstellen: Versicherung; Aufsichtsbehörde; Strafverfolgung.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.
